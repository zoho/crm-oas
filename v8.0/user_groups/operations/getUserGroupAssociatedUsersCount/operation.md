# GET /settings/user_groups/actions/associated_users_count
**Operation:** `getUserGroupAssociatedUsersCount` — Get associated users count per user group
> To retrieve the count of users associated with user groups in your Zoho CRM organization, optionally filtered by group criteria.

**Parameters:**
- `filters` (query, string, optional) [maxLen=250]: Filter criteria to narrow the results. Specify conditions as a structured filter expression. Maximum 250 characters.
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve paginated results. Default is 1. Minimum value is 1.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of records to return per page. Default is 200. Maximum value is 200.

**Responses:**

- **200**: Returns a paginated list of user groups with the count of users associated with each group. [application/json]
    > Response schema containing the paginated associated user counts per user group.
    - `associated_users_count` (array of object) [maxItems=200] **REQ** — Represents the array of user group entries with their associated user counts. 
      - `user_group` (object) **REQ** — Represents the user group details for this entry. 
        - `name` (string) **REQ** [maxLen=512] — Represents the name of the user group. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user group. 
      - `count` (integer/int32) **REQ** — Represents the number of users associated with this user group. 
    - `info` (object) **REQ** — Represents pagination information for the response. 
      - `per_page` (integer/int32) **REQ** — Represents the maximum number of user group entries returned per page. 
      - `count` (integer/int32) **REQ** — Represents the total number of user group entries returned in the current response. 
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response. 
      - `more_records` (boolean) **REQ** — Indicates whether additional user group entries are available beyond the current page. 

- **204**: No user groups match the provided filter criteria.

- **404**: The request URL does not match any configured endpoint pattern. **Resolution:** Verify the URL follows the pattern /settings/user_groups/actions/associated_users_count. [application/json]
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
