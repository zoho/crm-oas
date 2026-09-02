# GET /settings/user_groups/{group}/actions/sources_count
**Operation:** `getUserGroupSourcesCount` — Get source counts for a user group
> To retrieve the count of member sources by type (users, roles, territories, and groups) for a specific user group in your Zoho CRM organization.

**Parameters:**
- `group` (path, string, required) [enum=['1234567890']]: Specify the unique ID of the user group to operate on. From API v9 onwards, UUID format is also accepted. Example: `1234567890`.

**Responses:**

- **200**: Returns the count of each type of member source configured in the specified user group. [application/json]
    > Response schema containing the source counts for the specified user group.
    - `sources_count` (array of object) [maxItems=1] **REQ** — Represents the array containing the member source counts for the specified user group. 
      - `territories` (integer/int32) — Represents the number of territory sources in this user group. Present when territory sources are configured.
      - `roles` (integer/int32) — Represents the number of role sources in this user group. Present when role sources are configured.
      - `groups` (integer/int32) — Represents the number of group sources in this user group. Present when group sources are configured.
      - `users` (object) — Represents the count of individual user sources by status. Present when user sources are configured.
        - `inactive` (integer/int32) **REQ** — Represents the number of inactive users in this user group. 
        - `deleted` (integer/int32) **REQ** — Represents the number of deleted users in this user group. 
        - `active` (integer/int32) **REQ** — Represents the number of active users in this user group. 

- **204**: The specified user group has no member sources configured.

- **400**: The group ID in the URL is invalid. **Resolution:** Provide a valid numeric user group ID in the **group** path parameter. [application/json]
    > Response schema for an invalid group ID error.
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request failure. 
Possible values:
**INVALID_DATA** - The group ID in the URL is invalid.
    - `details` (object) **REQ** — Represents additional details about the request error. 
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path segment where the invalid resource ID was found. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the request failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. 
Possible values:
**error** - The request failed because the group ID is invalid.

- **404**: The request URL does not match any configured endpoint pattern. **Resolution:** Verify the URL follows the pattern /settings/user_groups/{group}/actions/sources_count. [application/json]
    > Response schema for an invalid URL pattern error.
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for the URL pattern failure. 
Possible values:
**INVALID_URL_PATTERN** - The request URL does not match any configured API endpoint.
    - `details` (object) **REQ** — Represents additional details about the URL pattern error. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the URL pattern failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. 
Possible values:
**error** - The request URL pattern was invalid.

**Scopes:** ZohoCRM.settings.user_groups.READ
