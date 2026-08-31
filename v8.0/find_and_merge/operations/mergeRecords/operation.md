# POST /{module}/{masterRecordId}/actions/merge
**Operation:** `mergeRecords` — Merge Records
> To merge duplicate records in your Zoho CRM organization into a single master record. Supports field-level value selection from child records and file attachment management. If a child record has more than 1000 related records, the merge processes asynchronously and returns a job_id for status tracking.

**Parameters:**
- `masterRecordId` (path, string, required) [maxLen=50, pattern=^[0-9]+$]: Specify the unique identifier of the master record to be retained after the merge operation. 
- `module` (path, string, required) [enum=['Accounts', 'Contacts', 'Leads', 'Deals', 'Cases', 'Campaigns']]: Specify the CRM module name containing the records to be merged.
Possible values:
**Accounts** - Accounts module.
**Contacts** - Contacts module.
**Leads** - Leads module.
**Deals** - Deals module.
**Vendors** - Cases module.
Additionally, **custom modules** are also supported in this API.  

- `feature` (query, string, optional) [enum=['web_record_approval']]: Triggers the web record approval flow instead of the standard merge flow.

**Request Body** (required) — application/json
> The request body contains the data required to perform the operation.  
  > Specify the merge configuration for the records to be consolidated.
  - `merge` (array of object) [maxItems=1] **REQ** — Specify the configurations for the merge. The array must contain exactly one object. 
    - `data` (array of object) [minItems=1, maxItems=2] **REQ** — Specify the child records to be merged into the master record. The array must contain a minimum of one and a maximum of two child record objects. 
      - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Specify the unique identifier of the child record to be merged. 
      - `_fields` (array of object) [maxItems=100] — Specify the API names of the fields from the child record whose values you wish to merge into the master record. 
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the fields in the child record that you want to include in the merge. 
        - `_data` (object) — It represents the unique ID of a file or attachment. This field is specifically used for File Upload and Image Upload fields in a record. Use [GET Records API](record.yaml#$.paths./{module}.get) to retrieve the unique IDs of the files or attachments. 
          oneOf:
              type: array of object [maxItems=50]
                - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Specify the unique numeric identifier of the file or image attachment. 
              type: null — Set to null to delete all file or image attachments for this field in the merged record. 
    - `master_record_fields` (array of object) [maxItems=100] — Specify the fields from the master record whose values should be retained in the merged record. Use this for file upload or image upload fields in the master record. 
      - `api_name` (string) **REQ** [maxLen=100] — Specify the API name of the master record field to retain in the merged record. 
      - `_data` (object) — Specify the file or image attachment IDs to retain for this master record field, or set to null to delete all attachments for this field in the merged record. 

> Notes
> - If an image upload or file upload is not specified, all the images/files in the master record will be retained.
> - If **'_data': null** is provided, all the images/files for that specific field will be deleted.
> - If a child record has more than **1000 records** in any of its related lists, then the merge action will be **scheduled**. This meas that it performs an asynchronous action, and the response to your request will not be available immediately. Instead, you will receive a unique **job_id** in the response. You can use this job_id to retrieve the status of your merge action. For details, please refer to the [Get Records Merge Status API](find_and_merge.yaml#$.paths./{module}/{masterRecordId}/actions/merge.get).
> - The **merge** JSON array can only contain one object, while the **data** JSON array can have a maximum of two child records. Exceeding these limits will result in errors.
> - Each field should only be mentioned once across the **master_record_fields** and **data** arrays.
> - Only open deals can be merged; closed deals will trigger an error.
> - The closing date, stage, probability, and expected revenue fields will be automatically populated based on the master record and should not be specified in the request.
> - Records currently locked or in an approval/review process cannot be merged. 

        oneOf:
            type: array of object [maxItems=50]
              - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Specify the unique identifier of the file or image attachment to retain. 
            type: null — Set to null to delete all file or image attachments for this master record field in the merged record. 

**Responses:**

- **201**: Returns the result of a merge operation that was either completed synchronously (with SUCCESS code and merged record ID) or scheduled for asynchronous processing (with SCHEDULED code and job_id).  [application/json]
    > Response when the merge operation was initiated - either completed synchronously or scheduled asynchronously. 
    oneOf:
        - `merge` (array of object) [maxItems=1] **REQ** — Contains the list of merge operation results indicating whether the merge completed or was scheduled.  
          oneOf:
              - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code for a completed merge. 
Possible values: 
**SUCCESS** - The records were merged successfully.

              - `details` (object) **REQ** — Contains the details of the completed merge, including the ID of the master record retained after the merge.  
                - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the unique identifier of the master record retained after the merge. 
              - `message` (string) **REQ** [maxLen=500] — Represents the success message for the completed merge operation. 
              - `status` (string) **REQ** [enum=['success']] — Represents the status of the merge operation. 
Possible values:
**success** - The merge completed successfully.

              - `code` (string) **REQ** [enum=['SCHEDULED']] — Represents the code indicating that the merge was scheduled for background processing. 
Possible values:
**SCHEDULED** - The merge operation was queued for asynchronous processing.

              - `details` (object) **REQ** — Contains the details of the scheduled merge, including the job ID for tracking the merge status.
                - `job_id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the unique identifier of the scheduled merge job. Use this ID with the [Get Merge Job Status API](find_and_merge.yaml#$.paths./{module}/{masterRecordId}/actions/merge.get) to check the status of the merge. 
              - `message` (string) **REQ** [maxLen=500] — Represents the message about the scheduled merge operation.
              - `status` (string) **REQ** [enum=['success']] — Represents the status of the scheduling operation. 
Possible values:
**success** - The merge was successfully scheduled.


- **400**: Shows a bad request due to validation errors, invalid data, or business rule violations. Returns either a standard top-level error object or a merge array with per-operation error details. [application/json]
    > Error response for a merge request that failed due to validation errors, invalid data, or business rule violations.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'INVALID_MODULE', 'NOT_ALLOWED']] — Represents the error code that identifies the type of failure. 
Possible values:
**INVALID_DATA** - The request contains invalid or malformed data.
**INVALID_MODULE** - The specified module name is not valid.
**NOT_ALLOWED** - The requested operation is not permitted.

        - `details` (object) — Contains additional context information about the error, such as the field name, JSON path, and constraint limits that caused the validation failure.
          - `resource_path_index` (integer/int32) — Represents the zero-based index of the path parameter that caused the error.
          - `api_name` (string) [maxLen=100] — Represents the API name of the field or resource that caused the validation error.
          - `json_path` (string) [maxLen=200] — Represents the JSON path to the field in the request that caused the validation error.
          - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that caused the validation error.
          - `minimum_length` (integer/int32) — Represents the minimum required length for the field that caused the validation error.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message that describes the issue in detail. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request. 
Possible values:
**error** - The request failed due to a validation error or other issue.

        - `merge` (array of object) [maxItems=10] **REQ** — Contains the list of error details for each merge operation that failed validation. 
          - `code` (string) **REQ** [enum=[6 values]] — Represents the error code that identifies the type of failure for the merge operation. 
Possible values:
**MANDATORY_NOT_FOUND** - A required field or property is missing from the request.
**NOT_ALLOWED** - The operation is not permitted due to a business rule constraint.
**INVALID_DATA** - The request contains invalid or malformed data.
**DUPLICATE_DATA** - Duplicate values were detected for a field that must be unique.
**DEPENDENT_FIELD_MISSING** - A field that depends on another field is missing from the request.
**LIMIT_EXCEEDED** - A size or count limit has been exceeded.

          - `details` (object) — Contains detailed error information for the failed merge operation, including the field name, JSON path, and constraint limits.
            - `api_name` (string) [maxLen=100] — Represents the API name of the field that caused the validation error.
            - `json_path` (string) [maxLen=200] — Represents the JSON path to the field in the request that caused the validation error.
            - `resource_path_index` (integer/int32) — Represents the zero-based index of the path parameter that caused the error.
            - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field that caused the validation error.
            - `minimum_length` (integer/int32) — Represents the minimum required length for the field that caused the validation error.
            - `MAXIMUM_SIZE` (string) [maxLen=50] — Represents the maximum allowed total file size for the file upload or image upload field that caused the limit exceeded error.
            - `limit_due_to` (array of object) [maxItems=20] — Contains the list of fields that contributed to the file size limit being exceeded.
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that contributed to the file size limit being exceeded. 
              - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field that contributed to the file size limit being exceeded. 
            - `data` (array of object) [maxItems=10] — Contains the list of child records that are associated with CPQ rules, preventing the merge operation.
              - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the unique identifier of the child record that has CPQ associations. 
              - `_associated_places` (array of object) [maxItems=50] — Contains the list of CPQ configurations and rules that are associated with the record, preventing the merge.
                - `type` (string) **REQ** [maxLen=100] — Represents the type of CPQ association, such as the product configurator or pricing rule category. 
                - `resources` (array of object) [maxItems=50] **REQ** — Contains the list of CPQ resources that reference this record, such as product configurators or pricing rules.
                  - `id` (string) **REQ** [maxLen=50, pattern=^[0-9]+$] — Represents the unique identifier of the CPQ resource. 
                  - `name` (string) **REQ** [maxLen=200] — Represents the name of the CPQ resource that references this record. 
            - `dependee` (object) — Contains the information about the field that the missing dependent field depends on.
              - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that the missing dependent field depends on. 
              - `json_path` (string) **REQ** [maxLen=200] — Represents the JSON path to the field that the missing dependent field depends on. 
          - `message` (string) **REQ** [maxLen=500] — Represents the error message for the failed merge operation. 
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the merge operation. 
Possible values:
**error** - The operation failed due to a validation error.


**Scopes:** ZohoCRM.modules.custom.CREATE, ZohoCRM.modules.leads.CREATE, ZohoCRM.modules.contacts.CREATE, ZohoCRM.modules.accounts.CREATE, ZohoCRM.modules.potentials.CREATE, ZohoCRM.modules.vendors.CREATE
