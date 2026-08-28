# POST /{module}/actions/mass_delete
**Operation:** `massDelete` — Delete records in bulk by record IDs or Custom View
> To delete records in bulk from a specified module in your Zoho CRM organization, either by providing record IDs for synchronous deletion or a Custom View ID for asynchronous batch deletion.

**Parameters:**
- `module` (path, string, required) [minLen=1, enum=[20 values]]: Specify the API name of the CRM module for the mass delete operation. Make a [Get Modules API](modules.yaml#$.paths./settings/modules.get) call for valid values.

**Request Body** (required) — application/json
> The request body must contain either an **ids** array to delete specific records or a **cvid** field to delete records from a Custom View.
  - `ids` (array) [minItems=1, maxItems=500] — Specify the list of record IDs to delete. Use the [Get Records API](record.yaml#$.paths./{module}.get) to get the valid records ID. 
  - `cvid` (string/string) [pattern=^[0-9]+$] — Specify the unique ID of the Custom View for which you want
to delete records. Use the [Get Custom
Views](custom_views.yaml#$.paths./settings/custom_views.get)
API for valid values.


> Note:

> The cvid key is supported for mass delete via API in the
following editions:

> - Enterprise

> - Ultimate

> - CRM Plus

> - Zoho One Enterprise

  - `territory` (object) — The unique ID of the territory whose records you want to delete. This key is valid only when you provide a custom view ID. 
  oneOf:
      - `ids` (array of string/string) [minItems=1, maxItems=500] **REQ** — Specify the list of record IDs to delete. Use the [Get Records API](record.yaml#$.paths./{module}.get) to get the valid record values. 
        items: [pattern=^[0-9]+$]
      - `cvid` (string/string) **REQ** [pattern=^[0-9]+$] — Specify the unique ID of the Custom View for which you want to delete records.  Refer to the [Get Custom Views](custom_views.yaml#$.paths./settings/custom_views.get) resource for valid values.
      - `territory` (object) — Specify the territory filter to restrict the delete operation to records within a specific territory. Only valid when using **cvid**.
        - `id` (string/string) **REQ** [pattern=^[0-9]+$] — Specify the unique ID of the territory for which you want to delete records. Refer to the [Get Territories](territories.yaml#$.paths./settings/territories.get) resource for valid values.
        - `include_child` (boolean) — Specify whether to include records from child
territories in the delete operation.

Possible values:

**true** - Include records from child territories.

**false** - Restrict the delete operation to records
in the specified territory only.


**Responses:**

- **200**: Returns the result of the mass delete operation, either a per-record deletion status for ID-based requests or a job ID for custom-view-based requests. [application/json]
    > Represents the success response payload for a mass delete operation.
    - `data` (array of object) [minItems=1, maxItems=500] **REQ** — Contains the array of success responses for record deletions or batch job scheduling. 
      oneOf:
          - `status` (string) **REQ** [const=success] — Represents the status of the response. 
          - `code` (string) **REQ** [const=SUCCESS] — Represents the success code for the response. 
          - `message` (string) **REQ** [const=record is deleted] — Represents the success message for the response. 
          - `details` (object) **REQ** — Contains the details of the deleted record, including the record ID. 
            - `id` (string/string) **REQ** [pattern=^[0-9]+$] — Represents the ID of the deleted record. 
          - `status` (string) **REQ** [const=success] — Represents the status of the response. 
          - `code` (string) **REQ** [const=SUCCESS] — Represents the success code for the response. 
          - `message` (string) **REQ** [const=mass delete scheduled successfully] — Represents the success message for the response. 
          - `details` (object) **REQ** — Contains the details of the scheduled batch delete job, including the job ID. 
            - `job_id` (string/string) **REQ** [pattern=^[0-9]+$] — Represents the unique ID of the scheduled mass delete job. Use this ID with the [Mass Delete Status API](mass_delete.yaml
#$.paths./{module}/actions/mass_delete.get) to track the job progress. 

- **207**: Returns a multi-status response when record deletion is partially successful. Each item in the **data** array independently indicates success or failure for the corresponding record. [application/json]
    > Represents the multi-status response payload when some records were deleted and others failed validation.
    - `data` (array of object) [minItems=1, maxItems=500] **REQ** — Contains the array of per-record results for the mass delete operation. Each item independently indicates success or failure for the corresponding record. 
      oneOf:
          - `status` (string) **REQ** [const=success] — Represents the status of the response. 
          - `code` (string) **REQ** [const=SUCCESS] — Represents the success code for the response. 
          - `message` (string) **REQ** [const=record is deleted] — Represents the success message for the response. 
          - `details` (object) **REQ** — Contains the details of the successfully deleted record, including the record ID. 
            - `id` (string/string) **REQ** [pattern=^[0-9]+$] — Represents the ID of the successfully deleted record. 
          - `status` (string) **REQ** [const=error] — Represents the status of the response. 
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the response. 
          - `message` (string/string) **REQ** — Represents the error message describing the reason for the deletion failure. 
          - `details` (object) **REQ** — Contains the details of the record that failed deletion, including the record ID. 
            - `id` (string/string) **REQ** [pattern=^[0-9]+$] — Represents the ID of the record that failed deletion. 

- **400**: The request is invalid due to a missing required field, invalid data
type, unsupported module, or no records found in the Custom View.

**Resolution:** The request body must include either a valid **ids**
array or a valid **cvid** key, and the module API name in the
request path must be supported.
 [application/json]
    > Represents the error response payload for an invalid request. Contains one of the possible error scenarios.
    oneOf:
        - `status` (string) **REQ** [const=error] — Represents the status of the error response. 
        - `code` (string) **REQ** [const=MANDATORY_NOT_FOUND] — Represents the error code for the response. 
        - `message` (string) **REQ** [const=required field not found] — Represents the error message for the response. 
        - `details` (object) **REQ** — Contains additional details about the error, including the name and expected data type of the missing field. 
          - `api_name` (string/string) — Represents the API name of the missing required field. 
          - `expected_data_type` (string/string) — Represents the expected data type of the missing required field. 
        - `status` (string) **REQ** [const=error] — Represents the status of the error response. 
        - `code` (string) **REQ** [const=ALREADY_SCHEDULED] — Represents the error code returned when a mass delete job is already running for the provided Custom View. 
        - `message` (string/string) **REQ** — Represents the error message indicating that a mass delete job is already scheduled for the provided Custom View. 
        - `details` (object) **REQ** — Represents additional details about the scheduling conflict, including the request parameter that triggered the error. 
          - `api_name` (string/string) **REQ** [enum=['cvid']] — Represents the API name of the key that caused the scheduling conflict. 
        - `status` (string) **REQ** [const=error] — Represents the status of the error response.
        - `code` (string) **REQ** [const=INVALID_DATA] — Represents the error code for the response. 
        - `message` (string/string) **REQ** — Represents the error message for the response. 
        - `details` (object) **REQ** — Contains additional details about the invalid field, including its name, JSON path, and ID.
          - `api_name` (string/string) **REQ** — Represents the API name of the invalid field. 
          - `json_path` (string/string) **REQ** — Represents the JSON path to the invalid field in the request. 
          - `id` (string/string) **REQ** [pattern=^[0-9]+$] — Represents the invalid record ID that triggered the error. 
        - `status` (string) **REQ** [const=error] — Represents the status of the error response. 
        - `code` (string) **REQ** [const=INVALID_MODULE] — Represents the error code for the response. 
        - `message` (string) **REQ** [const=the module name given seems to be invalid] — Represents the error message for the response.
        - `details` (object) **REQ** — Contains additional details about the error, including the index of the invalid path segment. 
          - `resource_path_index` (integer/int32) **REQ** [const=0] — Represents the index of the resource path segment that contains the invalid module name. 
        - `status` (string) **REQ** [const=error] — Represents the status of the error response. 
        - `code` (string) **REQ** [const=NOT_SUPPORTED] — Represents the error code for the response. 
        - `message` (string/string) **REQ** — Represents the error message for the response. 
        - `details` (object) **REQ** — Contains additional details about the error, including the index of the unsupported resource path segment. 
          - `resource_path_index` (integer/int32) **REQ** [const=0] — Represents the index of the unsupported resource path segment. 
        - `status` (string) **REQ** [const=error] — Represents the status of the error response. 
        - `code` (string) **REQ** [const=NO_RECORDS_FOUND] — Represents the error code for the response. 
        - `message` (string) **REQ** [const=no record found to update] — Represents the error message for the response. 
        - `details` (object) **REQ** — Contains additional details about the error.

- **403**: The current user does not have permission to delete records in the specified module.
Resolution: Request the mass delete permission for this module from your CRM administrator.
 [application/json]
    > Represents the error response returned when the current user lacks the permission required to delete records in the specified module.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the failed request.

Possible values:

**NO_PERMISSION** - The current user does not have
permission to delete records in this module.

    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the missing permission.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request failed due to an error.

    - `details` (object) **REQ** — Represents the additional error details about the missing permission.
      - `permissions` (array of string) [maxItems=1] **REQ** — Represents the list of permission keys required to perform this operation.
        items: [maxLen=255]

**Scopes:** ZohoCRM.mass_delete.DELETE
