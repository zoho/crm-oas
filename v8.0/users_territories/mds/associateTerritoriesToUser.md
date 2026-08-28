# PUT /users/{user}/territories
**Operation:** `associateTerritoriesToUser` — Add territories to a user
> To associate one or more territories with a specific user in your Zoho CRM organization.

**Parameters:**
- `user` (path, string/int64, required): Specify the unique ID of the user. Valid user IDs can be retrieved using the [Get Users](users.json#$.paths./{users}.get) API.

**Request Body** (required) — application/json
> The request body must contain a **territories** array with the territory IDs to associate with the user.
  > Specify the data required to associate territories with a user.
  - `territories` (array of object) [maxItems=200] **REQ** — JSON array specifying the territories to associate with the user.
    - `id` (string/int64) **REQ** — Specify the unique ID of the territory. Valid territory IDs can be retrieved using the [Get Territories](user_territories.json#$.paths./{users}/{user}/territories.get) API.

**Responses:**

- **200**: Returns a **territories** array containing the association result for each requested territory. — Schema: `SuccessResponse` [application/json]
    > Represents the response containing the per-territory operation results.
    schema: `SuccessResponse`
    - `territories` (array of object) [minItems=0, maxItems=200, uniqueItems] **REQ** — Represents the list of per-territory operation results.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory operation. Possible values: SUCCESS - The territory operation completed successfully.
      - `details` (object) **REQ** — Represents the additional details for the operation result.
        - `id` (string/int64) **REQ** — Represents the unique ID of the territory on which the operation was performed.
      - `message` (string) **REQ** [maxLen=1000] — Represents the message describing the result of the territory operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory operation. Possible values: success - The operation completed successfully.

- **400**: One or more territories in the request have validation errors. Resolution: Check the **code** field in each **territories** item for the specific error type and resolve accordingly. — Schema: `CommonErrorResponse` [application/json]
    > Represents the error response containing per-territory validation failure details.
    schema: `CommonErrorResponse`
    - `territories` (array of object) [minItems=0, maxItems=200, uniqueItems] **REQ** — Represents the list of per-territory validation errors.
      - `code` (string) **REQ** [enum=['INVALID_DATA', 'DUPLICATE_DATA', 'PERMISSION_DENIED']] — Represents the error code for the territory validation failure. Possible values: INVALID_DATA - The territory ID is invalid. DUPLICATE_DATA - The territory is already associated with the user. PERMISSION_DENIED - The user lacks the required permission for the territory.
      - `details` (object) **REQ** — Represents additional details about the territory validation error.
        - `api_name` (string) [maxLen=255] — Represents the API field name associated with the validation error.
        - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that caused the validation error.
      - `message` (string) [maxLen=1000] — Represents the error message describing the territory validation failure.
      - `status` (string) **REQ** [enum=['error']] — Represents the status of the territory operation. Possible values: error - The territory operation failed.

- **403**: The logged-in user cannot update their own territory associations. Resolution: Territory associations for the currently logged-in user must be managed by a different user with the required permissions. — Schema: `CommonUrlErrorResponse` [application/json]
    > Represents a top-level error response for invalid path parameters, including a resource path index in the error details.
    schema: `CommonUrlErrorResponse`
    - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code for the request failure. Possible values: INVALID_DATA - One or more path parameters in the request URL are invalid. NOT_ALLOWED - The operation is not permitted for the specified user.
    - `details` (object) **REQ** — Represents additional details about the error, including the path parameter index.
      - `resource_path_index` (integer/int32) — Represents the zero-based index of the path parameter that caused the error.
    - `message` (string) [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: error - The request failed.

**Scopes:** ZohoCRM.settings.territories.UPDATE, ZohoCRM.users.UPDATE
