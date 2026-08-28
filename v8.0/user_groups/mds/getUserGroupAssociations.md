# GET /settings/user_groups/{group}/actions/associations
**Operation:** `getUserGroupAssociations` — Get associations for a user group
> To retrieve the list of CRM resources, such as sharing rules, workflows, assignment rules, and approval processes, that are associated with a specific user group in your Zoho CRM organization.

**Parameters:**
- `group` (path, string, required) [enum=['1234567890']]: Specify the unique ID of the user group to operate on. From API v9 onwards, UUID format is also accepted. Example: `1234567890`.

**Responses:**

- **200**: Returns the list of CRM resources, such as sharing rules, workflows, and assignment rules, that are associated with the specified user group. [application/json]
    > Response schema containing the list of CRM resources associated with the specified user group.
    - `associations` (array of object) [maxItems=200] **REQ** — Represents the array of CRM resources associated with the specified user group. 
      - `resource` (object) **REQ** — Represents the CRM resource that is associated with the user group. 
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the associated resource. 
        - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the associated resource (such as a sharing rule or workflow). 
      - `details` (object) **REQ** — Represents the CRM module details for this association. 
        - `module` (object) **REQ** — Represents the CRM module in which the associated resource is defined. 
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the module containing the associated resource. 
          - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the module containing the associated resource. 
      - `type` (string) **REQ** [maxLen=255] — Represents the category of CRM resource associated with the user group, such as **sharing rules**, **workflows**, or **automation rules**. 

- **400**: The group ID in the URL is invalid. **Resolution:** Provide a valid numeric user group ID in the **group** path parameter. — Schema: `Error Response Core` [application/json]
    > Response schema for an invalid group ID error.
    title: Error Response Core
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request failure. 
Possible values:
**INVALID_DATA** - The group ID in the URL is invalid.
    - `details` (object) **REQ** — Represents additional details about the request error. 
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the path segment where the invalid resource ID was found. 
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the request failure. 
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the request. 
Possible values:
**error** - The request failed because the group ID is invalid.

- **404**: The request URL does not match any configured endpoint pattern. **Resolution:** Verify the URL follows the pattern /settings/user_groups/{group}/actions/associations. [application/json]
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
