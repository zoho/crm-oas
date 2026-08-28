# DELETE /{moduleName}/{recordId}/Locking_Information__s/{lockId}
**Operation:** `removeLockFromLockedRecord` — Remove lock from a locked record
> To remove the lock from a locked record in the specified module of your Zoho CRM account.

**Parameters:**
- `moduleName` (path, string, required) [maxLen=256]: The ID of the locked record from which the lock is to be removed. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name.
- `recordId` (path, string, required) [maxLen=32]: The ID of the locked record from which the lock is to be removed.
- `lockId` (path, string, required) [maxLen=32]: Specify the unique identifier of the lock record to be removed or updated.

**Responses:**

- **200**: Returns a success response when the lock is removed from the record successfully. [application/json]
    > Contains the success response for the unlock operation.
    - `data` (array of object) [maxItems=1] **REQ** — Contains the response details for the unlock operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the unlock operation.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code for the unlock operation.
      - `message` (string) **REQ** [maxLen=256] — Represents the response message for the unlock operation.
      - `details` (object) **REQ** — Contains the details of the unlocked record, including its unique identifier and audit timestamps.
        anyOf:
            - `id` (string) **REQ** [maxLen=32] — Contains the details of the successfully unlocked record.
            - `Created_Time` (string/date-time) — Contains the details of the successfully unlocked record.
            - `Modified_Time` (string/date-time) — Contains the details of the successfully unlocked record.
            - `Modified_By` (object) — Contains the details of the successfully unlocked record.
              - `name` (string) **REQ** [maxLen=256] — Contains the details of the successfully unlocked record.
              - `id` (string) **REQ** [maxLen=32] — Contains the details of the successfully unlocked record.
            - `Created_By` (object) — Contains the details of the successfully unlocked record.
              - `name` (string) **REQ** [maxLen=256] — Contains the details of the successfully unlocked record.
              - `id` (string) **REQ** [maxLen=32] — Contains the details of the successfully unlocked record.
            - `id` (string) **REQ** [maxLen=32] — Contains the details of the successfully unlocked record.

- **400**: The request contains invalid or missing parameters. **Resolution:** Verify that the module name, record ID, and lock ID in the request are valid. [application/json]
    > Error response returned when the request contains invalid or missing parameters for the remove lock operation.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `data` (array of object) [maxItems=1] **REQ** — Contains the list of error details for the failed operation.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for this response.
          - `details` (object) **REQ** — Represents additional details about the error.
            - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the missing mandatory field.
            - `json_path` (string) **REQ** [maxLen=256] — Represents the JSON path to the missing mandatory field in the request payload.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message providing details about the failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [enum=['relation not found']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [enum=['Required Record Locking Configuration is not present']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [enum=['the related id given seems to be invalid']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.

- **403**: The unlock operation is not permitted for this record. **Resolution:** Verify that you have the required permission and that the record was not locked automatically. [application/json]
    > Error response indicating insufficient permissions or security restrictions.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
    - `code` (string) **REQ** [enum=['NO_PERMISSION', 'NOT_ALLOWED']] — Represents the error code for this response.
    - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
    - `details` (object) **REQ** — Represents additional details about the error.
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.

**Scopes:** ZohoCRM.settings.modules.DELETE
