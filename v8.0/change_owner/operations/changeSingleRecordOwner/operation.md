# POST /{module}/{record}/actions/change_owner
**Operation:** `changeSingleRecordOwner` — Change Owner
> To change the owner of a specific record in the specified CRM module in your Zoho CRM organization. Note: The module name `Deals` is accepted and internally resolved to `Potentials`. `Meetings` is internally resolved to `Events`.

**Parameters:**
- `module` (path, string, required) [maxLen=255]: Specify the API name of the module.
- `record` (path, string, required) [maxLen=19, pattern=^[0-9]+$]: Specify the ID of the record for which you want to change the owner.
- `notify` (query, boolean, optional): Deprecated — use the `notify` field in the request body instead.
- `owner_id` (query, string, optional) [maxLen=19]: Deprecated — use the `owner.id` field in the request body instead.
- `related_modules` (query, string, optional) [maxLen=2000]: Deprecated — use the `related_modules` array in the request body instead.

**Request Body** (required) — application/json
  > Specify the owner details for the single record owner change request.
  - `owner` (object) **REQ** — Specify the details of the new owner for the record.
    - `id` (string) **REQ** [maxLen=19] — Specify the user ID of the new owner.
  - `notify` (boolean) [nullable] — Specify whether to notify the new owner via email when the record is assigned.\nPossible values:\n**true** - The new owner is notified via email.\n**false** - The new owner is not notified via email.
  - `related_modules` (array of object) [maxItems=5] — Specify the related modules for which you want to transfer record ownership along with the main record.
    - `api_name` (string) [enum=['Tasks', 'Events', 'Calls', 'Contacts', 'Deals']] — Specify the API name of the related module for which the records are transferred.\nPossible values:\n**Tasks**\n**Events**\n**Calls**\n**Contacts**\n**Deals**
    - `id` (string) [maxLen=19] — Specify the record ID of the related module record to transfer to the new owner.

**Responses:**

- **200**: Returns the result of the owner change operation for the specified record. [application/json]
    > Successful owner change response
    - `data` (array of object) [maxItems=1] — Data containing the result of the owner change operation
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code indicating the outcome of the request. Possible values: **SUCCESS** - The owner change operation completed successfully.
      - `details` (object) **REQ** — Represents the details of the record for which the owner change was applied.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the record for which the owner change was applied.
      - `message` (string) **REQ** [maxLen=500] — Represents a brief message confirming the outcome of the owner change operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success** - The owner change operation completed without errors.

- **400**: Invalid request. The module is unsupported, the data is invalid, or a required field is missing.\n**Resolution:** The module API name in the request URL must be valid and the owner ID must be specified correctly. [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED', 'INVALID_DATA', 'INVALID_MODULE', 'API_NOT_SUPPORTED']] — Represents the error code indicating the cause of the failure. \nPossible values:\n**NOT_SUPPORTED** - The specified module or operation is not supported.\n**INVALID_DATA** - The input data is invalid.\n**INVALID_MODULE** - The module API name in the request URL is invalid.\n**API_NOT_SUPPORTED** - The Change Owner API is not supported in the requested API version (minimum version 3 required for customer calls).
        - `details` (object) **REQ** — Represents additional context about the error.
          - `resource_path_index` (integer/int32) — Represents the index of the resource path in the request that caused the error.
          - `supported_version` (integer/int32) — Represents the minimum supported API version. Returned with the API_NOT_SUPPORTED error code.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. \nPossible values:\n**error** - The request encountered an error and did not complete.
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_SUPPORTED', 'MANDATORY_NOT_FOUND']] — Represents the error code indicating the cause of the failure. \nPossible values:\n**INVALID_DATA** - The input data provided is invalid.\n**NOT_SUPPORTED** - The specified module or operation is not supported.\n**MANDATORY_NOT_FOUND** - A required field is missing from the request.
        - `details` (object) **REQ** — Represents additional context about the invalid or missing field.
          - `api_name` (string) **REQ** [maxLen=200] — Represents the API name of the field that caused the error.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field in the request body that caused the error.
          - `owner_status` (string) [maxLen=200] — Represents the owner-restriction context that triggered the owner validation error. Possible values: **include_subordinate_owners** - Indicates that ownership can be assigned only to users who are subordinates of the current user based on the role or territory hierarchy. **inactive** - Indicates that the new owner's user account is not active. Returned only when the error is caused by a subordinate-owner or inactive-owner permission check.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. \nPossible values:\n**error** - The request encountered an error and did not complete.
        - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code indicating the cause of the failure. \nPossible values:\n**EXPECTED_FIELD_MISSING** - A required field in the related modules object is missing from the request.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. \nPossible values:\n**error** - The request encountered an error and did not complete.
        - `details` (object) **REQ** — Represents the details about the missing expected fields.
          - `expected_fields` (array of object) [maxItems=100] **REQ** — Represents the list of expected fields that are missing from the request.
            - `api_name` (string) **REQ** [maxLen=200] — Represents the API name of the missing expected field.
            - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the missing expected field in the request body.
        - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code indicating the cause of the failure. \nPossible values:\n**AMBIGUITY_DURING_PROCESSING** - The request contains ambiguous data that cannot be resolved.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. \nPossible values:\n**error** - The request encountered an error and did not complete.
        - `details` (object) **REQ** — Represents the details about the ambiguous data in the request.
          - `ambiguity_due_to` (array of object) [maxItems=100] **REQ** — Represents the list of fields that contain ambiguous values in the request.
            - `api_name` (string) **REQ** [maxLen=200] — Represents the API name of the field containing ambiguous data.
            - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field containing ambiguous data in the request body.
        - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Error code indicating the record is in a stop-processing state. Possible values: **CANNOT_PROCESS** - The record's privacy settings block the Change Owner action.
        - `details` (object) **REQ** — Additional context identifying the affected record.
          - `id` (string) [maxLen=19] — The ID of the record that is in stop-processing state.
          - `index` (integer/int32) — The zero-based index of the record in the request.
        - `message` (string) **REQ** [maxLen=500] — Error message describing why the Change Owner action was blocked.
        - `status` (string) **REQ** [enum=['error']] — Response status. Possible values: **error** - The operation did not complete.
        - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Error code indicating the record is locked. Possible values: **RECORD_LOCKED** - The record is locked and cannot be reassigned.
        - `details` (object) **REQ** — Additional context identifying the locked record.
          - `id` (string) **REQ** [maxLen=19] — The ID of the locked record.
          - `action` (string) **REQ** [maxLen=100] — The action that caused the locking conflict, for example **merge** or **record_locking**.
        - `message` (string) **REQ** [maxLen=500] — Error message describing why the Change Owner action was blocked.
        - `status` (string) **REQ** [enum=['error']] — Response status. Possible values: **error** - The operation did not complete.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating the ownership restriction. Possible values: **NOT_ALLOWED** - Service Provider users can only be assigned as owner of Tasks, Events, Calls, and Appointments.
        - `details` (object) **REQ** — Additional context identifying the owner field that caused the error.
          - `api_name` (string) **REQ** [maxLen=200] — Represents the API name of the field that caused the error.
          - `json_path` (string) **REQ** [maxLen=500] — Represents the JSON path to the field in the request body that caused the error.
        - `message` (string) **REQ** [maxLen=500] — Error message describing the ownership restriction.
        - `status` (string) **REQ** [enum=['error']] — Response status. Possible values: **error** - The operation did not complete.

- **403**: Permission denied to change record ownership in this module.\n**Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code indicating the cause of the permission failure. \nPossible values:\n**NO_PERMISSION** - The user's CRM profile lacks the required permission to change record ownership.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the permission issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. \nPossible values:\n**error** - The request encountered an error and did not complete.
        - `details` (object) **REQ** — Represents the additional details about the missing permissions.
          - `permissions` (array of string) [maxItems=1] **REQ** — Represents the list of required permissions that the user's profile is missing.
            items: [maxLen=200]
        - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Represents the error code indicating that the Change Owner operation cannot be performed on the module. Possible values: **CANNOT_PERFORM_ACTION** - The specified module does not permit the Change Owner action.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing why the Change Owner operation cannot be performed on the specified module.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - The request encountered an error and did not complete.
        - `details` (object) — Represents additional context about the operation that is not allowed on the module.
        - `code` (string) **REQ** [enum=['CANNOT_ASSIGN']] — Error code indicating the type of error
        - `details` (object) **REQ** — Additional details about the error
          - `permissions` (array of string) [maxItems=1] **REQ** — List of permissions that the transferee lacks for the module, causing the error
            items: [maxLen=250]
        - `message` (string) **REQ** [maxLen=500] — Error message describing the issue
        - `status` (string) **REQ** [enum=['error']] — Status of the response
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating the target user is closed or deleted. Possible values: **INVALID_DATA** - The supplied owner ID refers to a closed or deleted user.
        - `details` (object) **REQ** — Additional context identifying the invalid owner field.
          - `api_name` (string) **REQ** [maxLen=200] — The API name of the field that contains the invalid owner reference.
          - `json_path` (string) **REQ** [maxLen=500] — The JSON path to the field that contains the invalid owner reference.
          - `owner_status` (string) **REQ** [enum=['deleted']] — Indicates the state of the target user. Possible values: **deleted** - The user account is closed or deleted.
        - `message` (string) **REQ** [maxLen=500] — Error message describing why the owner assignment was rejected.
        - `status` (string) **REQ** [enum=['error']] — Response status. Possible values: **error** - The operation did not complete.

**Scopes:** ZohoCRM.change_owner.CREATE
