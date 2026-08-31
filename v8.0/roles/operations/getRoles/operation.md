# GET /settings/roles
**Operation:** `getRoles` — Get all roles
> Returns the list of all roles configured in your Zoho CRM organization.

**Responses:**

- **200**: Returns the list of all CRM roles configured in the organization. [application/json]
    > Represents the successful response for retrieving all CRM roles in the organization.
    - `roles` (array of object) [maxItems=250] **REQ** — Represents the list of CRM roles returned in the response. 
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
      - `description` (string) **REQ** [maxLen=1000, nullable] — Represents the description of the role, providing additional context about its purpose and responsibilities. 
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

**Scopes:** ZohoCRM.settings.roles.READ
