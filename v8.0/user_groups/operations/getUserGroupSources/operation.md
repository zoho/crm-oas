# GET /settings/user_groups/{group}/sources
**Operation:** `getUserGroupSources` — Get sources for a user group
> To retrieve the paginated list of member sources configured for a specific user group in your Zoho CRM organization.

**Parameters:**
- `group` (path, string, required) [enum=['1234567890']]: Specify the unique ID of the user group to operate on. From API v9 onwards, UUID format is also accepted. Example: `1234567890`.
- `filters` (query, string, optional) [maxLen=250]: Filter criteria to narrow the results. Specify conditions as a structured filter expression. Maximum 250 characters.
- `include` (query, string, optional) [enum=['sources_count', 'sources']]: Specify additional related data to include in the response.
Possible values:
**sources** - Include the list of sources for each group.
**sources_count** - Include the count of sources for each group.
- `type` (query, string, optional) [enum=['users', 'roles', 'territories', 'groups']]: Filter sources by source type.
Possible values:
**users** - Return only user-type sources.
**roles** - Return only role-type sources.
**territories** - Return only territory-type sources.
**groups** - Return only group-type sources.
- `user_type` (query, string, optional) [maxLen=100]: Filter user-type sources by the user's status or type classification.
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve paginated results. Default is 1. Minimum value is 1.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of records to return per page. Default is 200. Maximum value is 200.

**Responses:**

- **200**: Returns the paginated list of member sources configured for the specified user group. [application/json]
    > Response schema containing the paginated list of member sources for the user group.
    - `sources` (array of object) [maxItems=200] **REQ** — Represents the array of member sources configured for the user group. 
      - `source` (object) **REQ** — Represents the identifier and name of the source. 
        - `name` (string) **REQ** [maxLen=250] — Represents the name of the source configured as a member. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user, role, territory, or group configured as a member source. 
      - `type` (string) **REQ** [enum=['users', 'roles', 'territories', 'groups']] — Represents the type of this member source. 
Possible values:
**users** - Individual CRM users.
**roles** - CRM roles.
**territories** - CRM territories.
**groups** - CRM user groups.
      - `subordinates` (boolean) — Indicates whether users in subordinate roles are included for role-type sources. Present when configured during group creation or update.
      - `sub_territories` (boolean) — Indicates whether members from sub-territories are included for territory-type sources. Present when configured during group creation or update.
    - `info` (object) **REQ** — Represents pagination information for the response. 
      - `per_page` (integer/int32) **REQ** — Represents the maximum number of member source records returned per page. 
      - `count` (integer/int32) **REQ** — Represents the total number of member sources returned in the current response. 
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response. 
      - `more_records` (boolean) **REQ** — Indicates whether additional member source records are available beyond the current page. 

- **204**: The specified user group has no member sources configured.

- **400**: The request failed due to an invalid group ID or an invalid query parameter value. **Resolution:** Verify the group ID and ensure the **type** parameter uses a valid value (users, roles, territories, or groups). [application/json]
    > Response schema for a failed sources request, covering both invalid group ID and parameter pattern errors.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request failure. 
Possible values:
**INVALID_DATA** - The group ID in the URL is invalid.
        - `details` (object) **REQ** — Represents additional details about the request error. 
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path segment where the invalid resource ID was found. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the request failure. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. 
Possible values:
**error** - The request failed because the group ID is invalid.
        - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code for the failed pattern validation. 
Possible values:
**PATTERN_NOT_MATCHED** - The query parameter value does not match the expected pattern.
        - `details` (object) **REQ** — Represents additional details about the pattern validation failure. 
          - `regex` (string) **REQ** [const=users|roles|groups|territories] — Represents the regex pattern that the parameter value failed to match. 
          - `param_name` (string) **REQ** [const=type] — Represents the name of the query parameter that failed the pattern validation. 
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the pattern validation failure. 
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. 
Possible values:
**error** - The request failed because the parameter value did not match the allowed pattern.

**Scopes:** ZohoCRM.settings.user_groups.READ
