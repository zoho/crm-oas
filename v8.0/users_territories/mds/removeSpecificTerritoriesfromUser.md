# DELETE /users/{user}/territories/{territory}
**Operation:** `removeSpecificTerritoriesfromUser` — Remove territory from a user
> To remove a specific territory from a user in your Zoho CRM organization.

**Parameters:**
- `user` (path, string/int64, required): Specify the unique ID of the user. Valid user IDs can be retrieved using the [Get Users](users.json#$.paths./{users}.get) API.
- `territory` (path, string/int64, required): Specify the unique ID of the territory. Valid territory IDs can be retrieved using the [Get Territories](user_territories.json#$.paths./{users}/{user}/territories.get) API.

**Responses:**

- **200**: Returns the removal result for the territory in a **territories** array. — Schema: `SuccessResponse` [application/json]
    > Represents the response containing the per-territory operation results.
    schema: `SuccessResponse`
    - `territories` (array of object) [minItems=0, maxItems=200, uniqueItems] **REQ** — Represents the list of per-territory operation results.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory operation. Possible values: SUCCESS - The territory operation completed successfully.
      - `details` (object) **REQ** — Represents the additional details for the operation result.
        - `id` (string/int64) **REQ** — Represents the unique ID of the territory on which the operation was performed.
      - `message` (string) **REQ** [maxLen=1000] — Represents the message describing the result of the territory operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory operation. Possible values: success - The operation completed successfully.

- **400**: The territory ID in the request URL is invalid. Resolution: A valid territory ID must be specified. Valid territory IDs can be retrieved using the[Get Territories](user_territories.json#$.paths./{users}/{user}/territories/.get) API. — Schema: `CommonUrlErrorResponse` [application/json]
    > Represents a top-level error response for invalid path parameters, including a resource path index in the error details.
    schema: `CommonUrlErrorResponse`
    - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code for the request failure. Possible values: INVALID_DATA - One or more path parameters in the request URL are invalid. NOT_ALLOWED - The operation is not permitted for the specified user.
    - `details` (object) **REQ** — Represents additional details about the error, including the path parameter index.
      - `resource_path_index` (integer/int32) — Represents the zero-based index of the path parameter that caused the error.
    - `message` (string) [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: error - The request failed.

**Scopes:** ZohoCRM.settings.territories.DELETE, ZohoCRM.users.DELETE
