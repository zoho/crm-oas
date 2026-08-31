# GET /users/{userId}/actions/validate_before_transfer
**Operation:** `getValidateBeforeTransferStatus` — Validate user before transfer
> Validates whether the specified user has open records, assignments, criteria configurations, subordinates, or alerts before transferring the user's data. Use this operation to check the user's dependencies before initiating a transfer.

**Parameters:**
- `userId` (path, string/int64, required) [pattern=^[0-9]+$]: Represents the unique identifier of the user whose data is to be transferred and whose account is to be deleted. Use the [Get Users API](users.yaml#$.paths./users.get) API to get the valid values.

**Responses:**

- **200**: The pre-transfer validation details were retrieved successfully. [application/json]
    > Represents the response body for the pre-transfer validation request, containing details about the user's records, assignments, criteria, subordinates, and alerts.
    - `validate_before_transfer` (array of object) [maxItems=1] **REQ** — Represents the list of pre-transfer validation results for the specified user. The array contains a maximum of one object.
      - `id` (string) [maxLen=19] — Represents the unique identifier of the user being validated.
      - `name` (string) [maxLen=250] — Represents the name of the user being validated.
      - `assignment` (boolean) — Indicates whether assignments exist for the user. 
      - `criteria` (boolean) — Indicates whether criteria configurations exist for the user. 
      - `subordinates` (boolean) — Indicates whether subordinates exist for the user. 
      - `alert` (boolean) — Indicates whether alerts exist for the user. 

- **400**: The request failed due to an invalid user ID or request parameters. [application/json]
    > Represents the error response returned when the provided user ID is invalid.
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the failed request. 
    - `details` (object) **REQ** — Represents additional details about the error, including the index of the resource path that caused the failure.
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path that contains the invalid value.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.

- **403**: Shows the error response body of a request when the user attempts to validate their own account before transfer. [application/json]
    > Represents the error response returned when the user attempts to validate their own account before transfer.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API request.
    - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the disallowed self-check.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the issue.
    - `details` (object) **REQ** — Represents additional details about the error, including the index of the resource path that caused the failure.
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource path that contains the invalid value.

**Scopes:** ZohoCRM.change_owner.READ
