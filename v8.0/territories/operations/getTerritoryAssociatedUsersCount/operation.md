# GET /settings/territories/actions/associated_users_count
**Operation:** `getTerritoryAssociatedUsersCount` — Get territory-associated user counts

> To retrieve the number of users associated with each territory in your Zoho CRM organization.


**Tags:** Territories

**Parameters:**
- `page` (query, integer/int32, optional) [min=1]: Page Number
- `per_page` (query, integer/int32, optional) [min=1, max=2000]: Per Page Number

**Responses:**

- **200**: Returns the list of territories with the count of users associated with each territory.
 — Schema: `TerritoryAssociatedUsersCountResponse` [application/json]
    > Represents the response containing the count of users associated with each territory.
    schema: `TerritoryAssociatedUsersCountResponse`
    - `associated_users_count` (array of object) [minItems=1, maxItems=200] **REQ** — Represents the list of objects containing the count of users associated with each territory.
      - `count` (integer/int32) **REQ** [min=0] — Represents the total number of users associated with the territory.
      - `territory` (object) **REQ** — Represents the territory object associated with the user count.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the territory.
        - `name` (string) **REQ** [maxLen=50] — Represents the display name of the territory.
    - `info` (object) **REQ** — Represents the pagination metadata for the response.
      - `per_page` (integer/int32) **REQ** [min=1, max=2000] — Represents the number of records returned per page.
      - `count` (integer/int32) **REQ** [min=0] — Represents the total number of records available in the current response.
      - `page` (integer/int32) **REQ** [min=1] — Represents the current page number in the paginated response.
      - `more_records` (boolean) **REQ** — Represents whether additional records are available beyond the current page.

- **204**: Indicates that the request was processed successfully but no territory user count data was returned.


- **400**: The territory feature is not enabled for this organization.
**Resolution:** The CRM administrator must enable Territory Management for the organization in Zoho CRM settings. — Schema: `TerritoryFeatureNotEnabledError` [application/json]
    > Represents the error response when the territory feature is not enabled for the organization.
    schema: `TerritoryFeatureNotEnabledError`
    - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
    - `details` (object) **REQ** — Represents additional details about the error.
    - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failure due to missing, expired, or invalid OAuth token.
**Resolution:** A new access token must be generated with the required scope for this API. — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.READ
