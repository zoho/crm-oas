# PUT /{moduleName}/{recordId}/Locking_Information__s/{lockId}
**Operation:** `updateReasonofLockedRecord` — Update locking reason of a locked record
> To update the locking reason of a locked record in the specified module of your Zoho CRM account.

**Parameters:**
- `moduleName` (path, string, required) [maxLen=255]: The unique identifier of the record whose locking reason needs to be updated. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module IDs.
- `recordId` (path, string, required) [maxLen=32]: The unique identifier of the record whose locking reason needs to be updated.
- `lockId` (path, string, required) [maxLen=32]: Specify the unique identifier of the lock record to be removed or updated.

**Request Body** (required) — application/json
> The request body must contain a data array with one object.
  > The request body must contain a data array with one object specifying the updated locking reason.
  - `data` (array of object) [maxItems=1] **REQ** — Specify the locking information details for the record.
    - `Locked_Reason__s` (string) **REQ** [maxLen=3000] — Specify the reason for locking the record.

**Responses:**

- **200**: Returns a success response after the locking reason update completes. [application/json]
    > Contains the success response for the lock reason update operation.
    - `data` (array of object) [maxItems=1] **REQ** — Contains the response details for the update operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the update operation.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the response code for the update operation.
      - `message` (string) **REQ** [maxLen=255] — Represents the response message for the update operation.
      - `details` (object) **REQ** — Contains the details of the successfully updated locked record, including its unique identifier and audit timestamps.
        anyOf:
            - `id` (string) **REQ** [maxLen=255] — Contains the details of the successfully updateed record.
            - `Created_Time` (string/date-time) — Contains the details of the successfully updateed record.
            - `Modified_Time` (string/date-time) — Contains the details of the successfully updateed record.
            - `Modified_By` (object) — Contains the details of the successfully updateed record.
              - `name` (string) **REQ** [maxLen=255] — Contains the details of the successfully updateed record.
              - `id` (string) **REQ** [maxLen=255] — Contains the details of the successfully updateed record.
            - `Created_By` (object) — Contains the details of the successfully updateed record.
              - `name` (string) **REQ** [maxLen=255] — Contains the details of the successfully updateed record.
              - `id` (string) **REQ** [maxLen=255] — Contains the details of the successfully updateed record.
            - `id` (string) **REQ** [maxLen=255] — Contains the details of the successfully updateed record.

- **400**: The request contains invalid or missing parameters. **Resolution:** Verify that the module name, record ID, lock ID, and request body are valid. [application/json]
    > Error response returned when the request contains invalid or missing parameters for the update locking reason operation.
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
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this response.
        - `details` (object) **REQ** — Represents additional details about the error.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.
        - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.

- **403**: The update operation is not permitted for this record. **Resolution:** Verify that you have the required permission and that the record is locked manually. [application/json]
    > Error response indicating insufficient permissions or security restrictions.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
    - `code` (string) **REQ** [enum=['NO_PERMISSION', 'NOT_ALLOWED']] — Represents the error code for this response.
    - `message` (string) **REQ** [maxLen=256] — Represents the error message providing details about the failure.
    - `details` (object) **REQ** — Represents additional details about the error.
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path segment where the error occurred.

**Scopes:** ZohoCRM.settings.modules.ALL
