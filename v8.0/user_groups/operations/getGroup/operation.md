# GET /settings/user_groups/{group}
**Operation:** `getGroup` — Get a user group
> To retrieve the details of a specific user group in your Zoho CRM organization by its unique ID, with optional inclusion of member source counts.

**Parameters:**
- `group` (path, string, required) [enum=['1234567890']]: Specify the unique ID of the user group to operate on. From API v9 onwards, UUID format is also accepted. Example: `1234567890`.
- `include` (query, string, optional) [enum=['sources_count', 'sources']]: Specify additional related data to include in the response.
Possible values:
**sources** - Include the list of sources for each group.
**sources_count** - Include the count of sources for each group.
- `filters` (query, string, optional) [maxLen=250]: Filter criteria to narrow the results. Specify conditions as a structured filter expression. Maximum 250 characters.
- `ids` (query, string, optional) [maxLen=250]: Specify a comma-separated list of unique user group IDs to filter the results by.
- `name` (query, string, optional) [maxLen=250]: Specify the name of the user group to filter the results by.

**Responses:**

- **200**: Returns the details of the specified user group, including name, description, creation and modification metadata, and optional source counts. [application/json]
    > Response schema containing the details of the specified user group.
    - `user_groups` (array of object) [maxItems=200] **REQ** — Represents an array containing the details of the specified user group. 
      - `created_by` (object) **REQ** — Represents the user who created this user group. 
        - `name` (string) **REQ** [maxLen=512] — Represents the name of the user who created this group. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user who created this group. 
      - `modified_by` (object) **REQ** — Represents the user who last modified this user group. 
        oneOf:
            - `name` (string) **REQ** [maxLen=512] — Represents the name of the user who last modified this group. 
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user who last modified this group. 
            type: null — Indicates that this group has not been modified since creation.
      - `modified_time` (object) **REQ** — Represents the date and time when the user group was last modified. 
        oneOf:
            type: string/date-time — Represents the timestamp of the last modification in ISO 8601 format.
            type: null — Indicates that the group has not been modified since creation.
      - `created_time` (string/date-time) **REQ** — Represents the date and time of user group creation, in ISO 8601 format. 
      - `description` (object) **REQ** — Represents the text description of the user group. Present in the response when a description was provided during group creation.
        oneOf:
            type: string [maxLen=250] — Represents the text description of the user group.
            type: null — Indicates that no description was provided for the user group.
      - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the user group. 
      - `name` (string) **REQ** [maxLen=250] — Represents the name of the user group. 
      - `sources_count` (object) — Represents the count of member sources by type for this user group. Present when the **include** query parameter includes **sources_count**.
        - `territories` (integer/int32) — Represents the number of territory sources in this user group. Present when **sources_count** is included.
        - `roles` (integer/int32) — Represents the number of role sources in this user group. Present when **sources_count** is included.
        - `groups` (integer/int32) — Represents the number of group sources in this user group. Present when **sources_count** is included.
        - `users` (integer/int32) — Represents the count of individual user sources in this group, broken down by user status. Present when **sources_count** is included.
    - `info` (object) — Represents pagination information for the response. 
      - `per_page` (integer/int32) **REQ** — Represents the maximum number of user group records returned per page. 
      - `count` (integer/int32) **REQ** — Represents the total number of user groups returned in the current response. 
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response. 
      - `more_records` (boolean) **REQ** — Indicates whether additional user group records are available beyond the current page. 

- **204**: The specified user group was not found or has no data to return.

- **400**: The group ID in the URL is invalid. **Resolution:** Provide a valid numeric user group ID in the **group** path parameter. [application/json]
    > Response schema for an invalid group ID error.
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request failure. 
Possible values:
**INVALID_DATA** - The group ID in the URL is invalid or does not reference an existing user group.
    - `details` (object) **REQ** — Represents additional details about the request error. 
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path segment where the invalid resource ID was found. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the request failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request operation. 
Possible values:
**error** - The request failed due to an invalid group ID.

- **404**: The request URL does not match any configured endpoint pattern. **Resolution:** Verify the request URL follows the pattern /settings/user_groups/{group}. [application/json]
    > Response schema for an invalid URL pattern error.
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN', 'URL_RULE_NOT_CONFIGURED']] — Represents the error code for the URL pattern failure. 
Possible values:
**INVALID_URL_PATTERN** - The request URL does not match any configured API endpoint.
**URL_RULE_NOT_CONFIGURED** - The URL routing rule for this endpoint is not configured.
    - `details` (object) **REQ** — Represents additional details about the URL pattern error. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the URL pattern failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request operation. 
Possible values:
**error** - The request URL pattern was invalid.

**Scopes:** ZohoCRM.settings.user_groups.READ
