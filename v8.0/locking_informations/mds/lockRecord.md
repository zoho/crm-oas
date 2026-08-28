# POST /{moduleName}/{recordId}/Locking_Information__s
**Operation:** `lockRecord` — Lock a record
> To lock a record in the specified module of your Zoho CRM account with a reason for locking.

**Parameters:**
- `recordId` (path, string, required) [maxLen=32]: Specify the unique identifier of the record for which you want to manage the lock.
- `moduleName` (path, string, required) [maxLen=256]: The API name of the module to which the locked record belongs. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name.

**Request Body** (required) — application/json
  > Specify the request payload for the locking operation.
  - `data` (array of object) [maxItems=1] **REQ** — Specify the locking information details for the record.
    - `Locked_Reason__s` (string) **REQ** [maxLen=3000] — Specify the reason for locking the record.

**Responses:**

- **201**: Returns a success response when the record is locked successfully. [application/json]
    > Contains the success response for the lock operation.
    - `data` (array of object) [maxItems=1] **REQ** — Contains the response details for the lock operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the lock operation.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code for the lock operation.
      - `message` (string) **REQ** [maxLen=255] — Represents the response message for the lock operation.
      - `details` (object) **REQ**
        oneOf:
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the newly created locking information record.
            - `Created_Time` (string/date-time) **REQ** — Represents the timestamp of the locking information record creation.
            - `Modified_Time` (string/date-time) **REQ** — Represents the timestamp when the locking information record was last modified.
            - `Modified_By` (object) **REQ** — Represents the details of the user who last modified the record.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified the record.
              - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who last modified the record.
            - `Created_By` (object) **REQ** — Represents the details of the user who created the record.
              - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who created the record.
              - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who created the record.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the newly created locking information record.

- **400**: The request contains invalid or missing parameters. **Resolution:** Verify that the module name, record ID, and request body are valid. [application/json]
    oneOf:
        - `data` (array of object) [maxItems=1] **REQ** — Contains the list of error details for the failed operation.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message providing details about the failure.
          - `details` (object) **REQ** — Represents additional details about the error.
            - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the missing mandatory field.
            - `json_path` (string) **REQ** [maxLen=256] — Represents the JSON path to the missing mandatory field in the request payload.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code for this response.
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `details` (object) **REQ**
          oneOf:
              - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this response.
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.

- **403**: The lock operation is not permitted for this record. **Resolution:** Verify that the record is not already locked and that manual locking is enabled for the module. [application/json]
    > A JSON object containing the error response when the lock operation is not allowed.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
    - `code` (string) **REQ** [enum=['NOT_ALLOWED', 'NO_PERMISSION']] — Represents the error code for this response.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message providing details about the failure.
    - `details` (object) **REQ** — Represents additional details about the error.
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.

**Scopes:** ZohoCRM.settings.modules.CREATE
