# POST /write
**Operation:** `createBulkWriteJob` — Create a bulk write job
> To create a bulk write job in your Zoho CRM organization that creates, updates, or upserts records in a target module from a previously uploaded file. The job is processed asynchronously; the response returns the job identifier that the get job details operation uses to poll job status, and an optional callback URL is notified on completion or failure.

**Request Body** (required) — application/json
> The request body must contain a resource array. You can include a maximum of 100 objects per request.
  > Defines the payload for creating a bulk write job, including the operation type, optional callback configuration, and the list of resource configurations.
  - `character_encoding` (string) [maxLen=50, nullable] — Specify the character encoding of the uploaded file. Zoho CRM auto-detects the encoding when this value is omitted; supply a value to override auto-detection and force the file to be read with the specified charset.
  - `operation` (string) **REQ** [enum=['insert', 'update', 'upsert']] — Specify the type of bulk write operation to perform on the file.
Possible values:
insert - Creates the records from the file as new records in the target module.
update - Updates existing records in the target module without creating new ones.
upsert - Updates existing records and creates new records that do not exist already.
  - `callback` (object) — Specify the callback configuration that Zoho CRM uses to notify your endpoint when the bulk write job completes or fails.
    - `url` (string/uri) **REQ** — Specify the URL that receives the job completion notification. The URL must accept the HTTP POST method and be reachable from Zoho CRM servers.
    - `method` (string) **REQ** [enum=['post']] — Specify the HTTP method that Zoho CRM uses to invoke the callback URL.
Possible values:
post - Sends the job completion notification as an HTTP POST request.
  - `resource` (array of object) [maxItems=100] **REQ** — Specify the list of resource configurations to process in the bulk write job. Each entry describes the target module, the uploaded file to read, and the field mappings to apply.
    - `type` (string) **REQ** [enum=['data']] — Specify the type of the resource being imported.
Possible values:
data - Indicates that the resource contains record data to be written into the target module.
    - `file_names` (array of string) [maxItems=10] **REQ** — Specify the names of the files inside the uploaded archive that the bulk write job must process.
      items: [maxLen=255]
    - `module` (object) **REQ** — Specify the target CRM module into which the records from the uploaded file are written.
      - `api_name` (string) **REQ** [maxLen=100] — Specify the API name of the target CRM module into which records are imported. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
    - `file_id` (string) **REQ** [maxLen=100] — Specify the identifier of the previously uploaded file that the bulk write job must read. Obtain this value from the response of the bulk upload file API.
    - `ignore_empty` (boolean) — Specify whether to skip empty cells in the uploaded file when updating records.
Possible values:
true - Ignores empty values in a column and updates only the fields that carry a non-empty value.
false - Updates the target field with the empty value supplied in the file.
    - `find_by` (string) **REQ** [enum=['id']] — Specify the field that the bulk write job uses to locate existing records when performing an update or upsert operation.
Possible values:
id - Matches records by their unique record ID in the target module.
    - `field_mappings` (array of object) [maxItems=500] — Specify the mapping between columns in the uploaded file and fields on the target module. When omitted, Zoho CRM auto-maps columns to fields whose API names match the CSV header.
      - `api_name` (string) **REQ** [maxLen=100] — Specify the API name of the field on the target module to populate with the column value. Refer to the [Fields API](fields.yaml#$.paths./settings/fields.get) resource for valid values.
      - `index` (integer/int32) **REQ** — Specify the zero-based column index in the uploaded file whose value populates the mapped field.

**Responses:**

- **201**: Returns the details of the bulk write job that was scheduled, including its unique identifier and the user who created it. [application/json]
    > Represents the success envelope that Zoho CRM returns after scheduling a bulk write job. Contains the overall status, response code, message, and the details of the newly scheduled job.
    - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the bulk write job creation request. 
Possible values:
success - Indicates that Zoho CRM scheduled the bulk write job successfully.
    - `code` (string) **REQ** [enum=['SUCCESS', 'FILE_UPLOAD_SUCCESS']] — Represents the response code returned for the bulk write job creation. 
Possible values:
**SUCCESS** - Indicates that the bulk write job was scheduled successfully.
**FILE_UPLOAD_SUCCESS** - Indicates that the file associated with the job was uploaded successfully.
    - `message` (string) **REQ** [enum=['success', 'file uploaded.']] — Represents the response message for the bulk write job creation. 
Possible values:
**success** - Confirms that Zoho CRM scheduled the bulk write job.
**file uploaded** - Confirms that Zoho CRM accepted the uploaded file for the job.
    - `details` (object) **REQ** — Represents the details of the newly scheduled bulk write job. 
      - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the newly scheduled bulk write job. Use this value to query the job status through the get job details operation. 
      - `created_by` (object) **REQ** — Represents the Zoho CRM user who created the bulk write job. 
        - `id` (string) **REQ** [maxLen=100] — Represents the unique identifier of the Zoho CRM user who created the bulk write job. Refer to the [Users API](users.yaml#$.paths./users.get) endpoint for details. 
        - `name` (string) [maxLen=100] — Represents the display name of the Zoho CRM user who created the bulk write job. Refer to the [Users API](users.yaml#$.paths./users.get) endpoint for details.

- **400**: The request payload failed validation. Resolution: The cause is identified by the **code** in the response. The offending field, mapping, callback configuration, or file reference must be corrected before retrying the request. [application/json]
    > Represents the validation error envelope returned for a failed bulk write job creation. Resolves to one of the documented error variants based on the failure cause.
    oneOf:
        - `code` (string) [enum=['INVALID_CALLBACK_URL']] — Represents the error code returned for this failure mode.
Possible values:
**INVALID_CALLBACK_URL** - Indicates that the supplied callback URL is invalid.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['INVALID_DATA']] — Represents the error code returned for this failure mode.
Possible values:
**INVALID_DATA** - Indicates that one of the supplied values is invalid or has an unsupported type.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned for this failure mode.
Possible values:
**MANDATORY_NOT_FOUND** - Indicates that a mandatory key was omitted from the request payload.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [enum=[2 values]] — Represents the message returned for the missing mandatory key.
Possible values:
**Required key parent_column_index** is not available - Returned when the parent_column_index key is missing for a lookup mapping.
**Required key find_by is not available** - Returned when the find_by key is missing for an update or upsert operation.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['COEXISTENCE_NOT_ALLOWED']] — Represents the error code returned for this failure mode.
Possible values:
**COEXISTENCE_NOT_ALLOWED** - Indicates that two mutually exclusive keys were supplied together in the request.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['FILE_NOT_SUPPORTED']] — Represents the error code returned for this failure mode.
Possible values:
**FILE_NOT_SUPPORTED** - Indicates that the uploaded file format is not supported by the bulk write job.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['FILE_NOT_FOUND']] — Represents the error code returned for this failure mode.
Possible values:
**FILE_NOT_FOUND** - Indicates that no uploaded file exists for the supplied file ID.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['INVALID_REQUEST']] — Represents the error code returned for this failure mode.
Possible values:
**INVALID_REQUEST** - Indicates that the request payload is malformed or does not conform to the documented contract.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['MANDATORY_FIELDS_NOT_MAPPED']] — Represents the error code returned for this failure mode.
Possible values:
**MANDATORY_FIELDS_NOT_MAPPED** - Indicates that one or more mandatory fields on the target module were not mapped in the field_mappings array.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['INVALID_CALLBACK_METHOD']] — Represents the error code returned for this failure mode.
Possible values:
**INVALID_CALLBACK_METHOD** - Indicates that the supplied callback HTTP method is not supported.
        - `details` (object) — Provides additional context about the invalid callback method, including the list of supported callback methods.
          - `supported_callback_methods` (array of string) [maxItems=10] — Lists the HTTP methods that the callback URL is allowed to use.
            items: [maxLen=50]
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
error - Indicates that the request failed.
        - `code` (string) [enum=['MISSING_REQUIRED_KEY']] — Represents the error code returned for this failure mode.
Possible values:
**MISSING_REQUIRED_KEY** - Indicates that a required key is missing at the JSON path identified in the error details.
        - `details` (object) — Provides additional context about the missing required key, including the JSON path that identifies its location in the request payload.
          - `json_path` (string) [maxLen=500] — Represents the JSON path in the request payload at which the required key was expected.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['MODULE_NOT_AVAILABLE']] — Represents the error code returned for this failure mode.
Possible values:
**MODULE_NOT_AVAILABLE** - Indicates that the supplied module API name does not match any module available in the Zoho CRM organization.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.
        - `code` (string) [enum=['REQUEST_BODY_NOT_SUPPORTED']] — Represents the error code returned for this failure mode.
Possible values:
**REQUEST_BODY_NOT_SUPPORTED** - Indicates that the request body content type is not supported by this operation.
        - `details` (object) — Provides additional context about the failure, when available.
        - `message` (string) [maxLen=1000] — Represents the error message returned for the failure, describing the validation problem.
        - `status` (string) [enum=['error']] — Represents the response status for this failure.
Possible values:
**error** - Indicates that the request failed.

**Scopes:** ZohoCRM.bulk.CREATE
