# DELETE /users/{user}/territories
**Operation:** `removeTerritoriesfromUser` — Remove territories from a user
> To remove one or more territories from a user in your Zoho CRM organization.

**Parameters:**
- `user` (path, string/int64, required): Specify the unique ID of the user. Valid user IDs can be retrieved using the [Get Users](users.json#$.paths./{users}.get) API.
- `ids` (query, string, required) [maxLen=2000, pattern=^[0-9]+(,[0-9]+)*$]: Specify the territory IDs to remove from the user. Accepts comma-separated values. Maximum: 100. Valid territory IDs can be retrieved using the [Get Territories](user_territories.json#$.paths./{users}/{user}/territories.get) API.

**Responses:**

- **200**: Returns a **territories** array containing the removal result for each specified territory. — Schema: `SuccessResponse` [application/json]
    > Represents the response containing the per-territory operation results.
    schema: `SuccessResponse`
    - `territories` (array of object) [minItems=0, maxItems=200, uniqueItems] **REQ** — Represents the list of per-territory operation results.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory operation. Possible values: SUCCESS - The territory operation completed successfully.
      - `details` (object) **REQ** — Represents the additional details for the operation result.
        - `id` (string/int64) **REQ** — Represents the unique ID of the territory on which the operation was performed.
      - `message` (string) **REQ** [maxLen=1000] — Represents the message describing the result of the territory operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory operation. Possible values: success - The operation completed successfully.

- **400**: One or more territory IDs in the request are invalid. Resolution: Valid territory IDs must be specified in the **ids** parameter. Valid territory IDs can be retrieved using the [Get Territories](user_territories.json#$.paths./{users}/{user}/territories.get) API. — Schema: `CommonErrorResponse` [application/json]
    > Represents the error response containing per-territory validation failure details.
    schema: `CommonErrorResponse`
    - `territories` (array of object) [minItems=0, maxItems=200, uniqueItems] **REQ** — Represents the list of per-territory validation errors.
      - `code` (string) **REQ** [enum=['INVALID_DATA', 'DUPLICATE_DATA', 'PERMISSION_DENIED']] — Represents the error code for the territory validation failure. Possible values: INVALID_DATA - The territory ID is invalid. DUPLICATE_DATA - The territory is already associated with the user. PERMISSION_DENIED - The user lacks the required permission for the territory.
      - `details` (object) **REQ** — Represents additional details about the territory validation error.
        - `api_name` (string) [maxLen=255] — Represents the API field name associated with the validation error.
        - `json_path` (string) [maxLen=1000] — Represents the JSON path to the field that caused the validation error.
      - `message` (string) [maxLen=1000] — Represents the error message describing the territory validation failure.
      - `status` (string) **REQ** [enum=['error']] — Represents the status of the territory operation. Possible values: error - The territory operation failed.

**Scopes:** ZohoCRM.settings.territories.DELETE, ZohoCRM.users.DELETE
