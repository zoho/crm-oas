# GET /settings/user_groups
**Operation:** `getUserGroups` — Get user groups
> To retrieve a paginated list of user groups configured in your Zoho CRM organization, with optional filtering by name or criteria, and optional inclusion of member source counts.

**Parameters:**
- `filters` (query, string, optional) [maxLen=250]: Filter criteria to narrow the results. Specify conditions as a structured filter expression. Maximum 250 characters.
- `include` (query, string, optional) [enum=['sources_count', 'sources']]: Specify additional related data to include in the response.
Possible values:
**sources** - Include the list of sources for each group.
**sources_count** - Include the count of sources for each group.
- `ids` (query, string, optional) [maxLen=250]: Specify a comma-separated list of unique user group IDs to filter the results by.
- `name` (query, string, optional) [maxLen=250]: Specify the name of the user group to filter the results by.
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve paginated results. Default is 1. Minimum value is 1.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of records to return per page. Default is 200. Maximum value is 200.

**Responses:**

- **200**: Returns a paginated list of user groups configured in your Zoho CRM organization. [application/json]
    > Represents the successful response for retrieving the list of user groups in the Zoho CRM organization, containing a paginated array of user group objects and pagination metadata.
    - `user_groups` (array of object) [maxItems=200] **REQ** — Represents the list of user group objects returned for the current page. 
      - `created_by` (object) **REQ** — Represents the CRM user who created this user group. 
        - `name` (string) **REQ** [maxLen=512] — Represents the display name of the CRM user who created the user group. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the CRM user who created the user group. 
      - `modified_by` (object) **REQ** — Represents the CRM user who last modified this user group, or null if the group has not been modified since creation. 
        oneOf:
            - `name` (string) **REQ** [maxLen=512] — Represents the display name of the CRM user who last modified the user group. 
            - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the CRM user who last modified the user group. 
            type: null — Indicates that the user group has not been modified since its creation.
      - `modified_time` (object) **REQ** — Represents the date and time at which the user group was last modified, in ISO 8601 format, or null if the group has not been modified since creation. 
        oneOf:
            type: string/date-time — Represents the date and time of the most recent modification to the user group, in ISO 8601 format.
            type: null — Indicates that the user group has not been modified since its creation.
      - `created_time` (string/date-time) **REQ** — Represents the date and time of user group creation, in ISO 8601 format. 
      - `description` (object) **REQ** — Represents the description of the user group, or null if no description was provided. 
        oneOf:
            type: string [maxLen=250] — Represents the text description of the user group.
            type: null — Indicates that no description was provided for this user group.
      - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user group. 
      - `name` (string) **REQ** [maxLen=250] — Represents the name of the user group. 
      - `sources_count` (object) — Represents the count of member sources for the user group, categorized by source type. Returned when the **include** parameter is set to **sources_count**.
        - `territories` (integer/int32) — Represents the number of CRM territories configured as member sources of this group.
        - `roles` (integer/int32) — Represents the number of CRM roles configured as member sources of this group.
        - `groups` (integer/int32) — Represents the number of other user groups configured as member sources of this group.
        - `users` (integer/int32) — Represents the count of CRM users configured as member sources of this group, categorized by user status.
    - `info` (object) **REQ** — Represents the pagination metadata for the current page of results. 
      - `per_page` (integer/int32) **REQ** — Represents the number of user group records returned per page. 
      - `count` (integer/int32) **REQ** — Represents the number of user group records returned in the current page. 
      - `page` (integer/int32) **REQ** — Represents the current page number in the paginated response. 
      - `more_records` (boolean) **REQ** — Indicates whether additional pages of user group records are available beyond the current page. 
Possible values:
**true** - More records are available on subsequent pages.
**false** - No more records remain after the current page.

- **204**: No user groups have been created for this Zoho CRM organization.

- **400**: The filters parameter contains invalid data. **Resolution:** Provide a valid filter expression in the **filters** parameter. [application/json]
    > Represents the error response returned when a request parameter contains invalid data.
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request validation failure. 
Possible values:
**INVALID_DATA** - One or more request parameters contain invalid data.
    - `details` (object) **REQ** — Represents additional details about the validation error, including the name of the parameter that caused the failure. 
      - `param_name` (string) **REQ** [maxLen=100] — Represents the name of the request parameter that contains invalid data. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request outcome. 
Possible values:
**error** - The request failed due to a validation error.

- **403**: The authenticated user does not have permission to access user groups. **Resolution:** Grant the **Crm_Implied_Manage_Groups** permission in the CRM profile settings. [application/json]
    > Represents the error response returned when the authenticated user lacks the required CRM permission to access user groups.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the authorization failure. 
Possible values:
**NO_PERMISSION** - The authenticated user does not have permission to access user groups.
    - `details` (object) **REQ** — Represents additional details about the authorization failure, including the missing permissions. 
      - `permissions` (string) **REQ** [maxLen=100] — Represents the name of the CRM permission that the authenticated user lacks to access user groups. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the authorization failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request outcome. 
Possible values:
**error** - The request failed due to an authorization error.

**Scopes:** ZohoCRM.settings.user_groups.READ
