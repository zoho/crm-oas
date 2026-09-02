# GET /users/{user}/territories/{territory}
**Operation:** `getSpecificTerritoryOfUser` — Specific territory of a user
> To retrieve a specific territory assigned to a user in your Zoho CRM organization.

**Parameters:**
- `user` (path, string/int64, required): Specify the unique ID of the user. Valid user IDs can be retrieved using the [Get Users](users.json#$.paths./{users}.get) API.
- `territory` (path, string/int64, required): Specify the unique ID of the territory. Valid territory IDs can be retrieved using the [Get Territories](user_territories.json#$.paths./{users}/{user}/territories.get) API.

**Responses:**

- **200**: Returns the details of a specific territory assigned to the user in a **territories** array. — Schema: `TerritoryGetResponse` [application/json]
    > Represents the response containing territories assigned to a user and pagination details.
    schema: `TerritoryGetResponse`
    - `territories` (array of object) [minItems=0, maxItems=200, uniqueItems] **REQ** — The JSON array representing the list of territories assigned to the user.
      - `id` (string/int64) **REQ** — Represents the unique ID of the territory.
      - `Manager` (object) **REQ** — Represents the manager of the territory. Valid user IDs and names can be retrieved using the [Get Users](users.json#$.paths./{users}.get) API.
        - `Name` (string) [maxLen=255] — Represents the full name of the territory manager.
        - `id` (string/int64) — Represents the unique ID of the territory manager.
      - `Reporting_To` (object) **REQ** — Represents the parent territory that this territory reports to in the hierarchy.
        - `Name` (string) **REQ** [maxLen=255] — Represents the name of the parent territory or reporting entity.
        - `id` (string/int64) **REQ** — Represents the unique ID of the parent territory or reporting entity.
      - `Name` (string) **REQ** [maxLen=255] — Represents the name of the territory.
    - `info` (object) **REQ** — Represents the pagination details for the response.
      - `count` (integer/int32) **REQ** — Represents the number of territory records returned in the current page. 
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response.
      - `per_page` (integer/int32) **REQ** — Represents the maximum number of records returned per page.
      - `more_records` (boolean) **REQ** — Indicates whether more territory records are available beyond the current page. Possible values: true - More records are available. false - No more records are available.

- **204**: The specified territory is not assigned to the user.

- **400**: The user ID in the request URL is invalid. Resolution: A valid user ID must be specified. Valid user IDs can be retrieved using the [Get Users](users.json#$.paths./{users}.get) API. — Schema: `CommonUrlErrorResponse` [application/json]
    > Represents a top-level error response for invalid path parameters, including a resource path index in the error details.
    schema: `CommonUrlErrorResponse`
    - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code for the request failure. Possible values: INVALID_DATA - One or more path parameters in the request URL are invalid. NOT_ALLOWED - The operation is not permitted for the specified user.
    - `details` (object) **REQ** — Represents additional details about the error, including the path parameter index.
      - `resource_path_index` (integer/int32) — Represents the zero-based index of the path parameter that caused the error.
    - `message` (string) [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: error - The request failed.

**Scopes:** ZohoCRM.settings.territories.READ, ZohoCRM.users.READ
