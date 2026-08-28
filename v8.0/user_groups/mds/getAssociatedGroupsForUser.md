# GET /users/{user}/actions/associated_groups
**Operation:** `getAssociatedGroupsForUser` — Get associated groups for a user
> To retrieve the paginated list of user groups associated with a specific user in your Zoho CRM organization, with optional inclusion of member sources and source counts.

**Parameters:**
- `user` (path, string, required) [enum=['3652397000000186017']]: 

Specifies the unique ID of the user whose associated groups you want to retrieve. Use the [Get Users](users#$.paths./users.get) API to obtain user IDs. From API v9 onwards, UUID format is also accepted.
- `include` (query, string, optional) [enum=['sources_count', 'sources']]: Specify additional related data to include in the response.
Possible values:
**sources** - Include the list of sources for each group.
**sources_count** - Include the count of sources for each group.
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve paginated results. Default is 1. Minimum value is 1.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of records to return per page. Default is 200. Maximum value is 200.

**Responses:**

- **200**: Returns a paginated list of user groups associated with the specified user. [application/json]
    > Response schema containing the paginated list of user groups associated with the specified user.
    - `user_groups` (array of object) [maxItems=200] **REQ** — Represents the array of user groups associated with the specified user. 
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
      - `sources` (array of object) [maxItems=200] — Represents the array of member sources configured for this user group. Present when the **include** query parameter includes **sources**.
        - `source` (object) **REQ** — Represents the identifier and name of the source. 
          - `name` (string) **REQ** [maxLen=250] — Represents the name of the source configured as a member. 
          - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the source configured as a member. 
        - `type` (string) **REQ** [enum=['users', 'roles', 'territories', 'groups']] — Represents the type of this member source. 
Possible values:
**users** - Individual CRM users.
**roles** - CRM roles.
**territories** - CRM territories.
**groups** - CRM user groups.
        - `subordinates` (boolean) — Indicates whether users in subordinate roles are included for role-type sources. Present when configured.
        - `sub_territories` (boolean) — Indicates whether members from sub-territories are included for territory-type sources. Present when configured.
    - `info` (object) **REQ** — Represents pagination information for the response. 
      - `per_page` (integer/int32) **REQ** — Represents the maximum number of user group records returned per page. 
      - `count` (integer/int32) **REQ** — Represents the total number of user groups returned in the current response. 
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response. 
      - `more_records` (boolean) **REQ** — Indicates whether additional user group records are available beyond the current page. 

- **400**: The user ID in the URL is invalid. **Resolution:** Provide a valid numeric CRM user ID in the **user** path parameter. [application/json]
    > Response schema for an invalid user ID error.
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request failure. 
Possible values:
**INVALID_DATA** - The user ID in the URL is invalid.
    - `details` (object) **REQ** — Represents additional details about the request error. 
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path segment where the invalid resource ID was found. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the request failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. 
Possible values:
**error** - The request failed because the user ID is invalid.

- **404**: The request URL does not match any configured endpoint pattern. **Resolution:** Verify the URL follows the pattern /users/{user}/actions/associated_groups. [application/json]
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
