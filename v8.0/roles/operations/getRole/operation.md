# GET /settings/roles/{role}
**Operation:** `getRole` — Get a role
> Returns the details of a single role, specified by its ID in the URL.

**Parameters:**
- `role` (path, string, required) [maxLen=19]: Specify the unique ID of the role for which you want to retrieve the details. Refer to the [Get Roles](roles.yaml#$.paths./settings/roles.get) resource for valid values.

**Responses:**

- **200**: Returns the details of the specified CRM role. [application/json]
    > Represents the successful response containing the details of the specified CRM role.
    - `roles` (array of object) [maxItems=1] **REQ** — Represents the list containing the requested CRM role. 
      - `display_label` (string) **REQ** [maxLen=200] — Represents the display label of the role as shown in the Zoho CRM user interface. 
      - `forecast_manager` (object) **REQ** — Represents the forecast manager assigned to this role. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the forecast manager assigned to the role. 
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the forecast manager assigned to the role. 
      - `reporting_to` (object) **REQ** — Represents the parent role to which this role reports in the CRM role hierarchy.  Refer to the [Get Roles](roles.yaml#$.paths./settings/roles.get) resource for valid values.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the parent role in the role hierarchy. 
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the parent role in the role hierarchy. 
      - `api_name` (string) [maxLen=100] — Represents the API name identifier for the role, used to reference the role programmatically.
      - `share_with_peers` (boolean) **REQ** — Indicates whether users assigned to this role can share records with users in peer roles at the same level. 
Possible values:
**true** - Users assigned to this role can share records with peer role users.
**false** - Users assigned to this role cannot share records with peer role users.
      - `description` (string) **REQ** [maxLen=255, nullable] — Represents the description of the role, providing additional context about its purpose and responsibilities. 
      - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the role. 
      - `name` (string) **REQ** [maxLen=200] — Represents the display name of the role. 
      - `created_by__s` (object) **REQ** — Represents the user who created this role. 
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who created the role. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user who created the role. 
      - `modified_by__s` (object) **REQ** — Represents the user who last modified this role. 
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who last modified the role. 
        - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the user who last modified the role. 
      - `modified_time__s` (string/date-time) **REQ** [nullable] — Represents the timestamp at which the role was last modified. 
      - `created_time__s` (string/date-time) **REQ** [nullable] — Represents the timestamp indicating when the role was added to the organization. 

- **204**: No content - the specified role was not found or the user does not have access to it.

**Scopes:** ZohoCRM.settings.roles.READ
