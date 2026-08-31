# GET /settings/data_sharing
**Operation:** `getDataSharing` — Data Sharing Settings
> To retrieve your organization's default data-sharing permissions for modules.

**Responses:**

- **200**: The data sharing settings were retrieved successfully. [application/json]
    > Response object containing the organization's default data sharing settings.
    - `data_sharing` (array of object) [maxItems=600] **REQ** — Contains the organization's default data-sharing permissions for each module.
      - `share_type` (string) **REQ** [enum=['private', 'public_read_write', 'public', 'public_read_only']] — Represents the access level for the module. **Possible values:** **private** - Only the record owner and their superior can view the records in the module. **public_read_only** - Users can view others' records but cannot modify or delete them. **public_read_write** - Users can view and modify others' records but cannot delete them. **public** - Users can view, modify, and delete others' records.
      - `public_in_portals` (boolean) **REQ** — Indicates whether the module is configured in public portals. **Possible values:** ** true** - The module is configured in public portals. **false** - The module is not configured in public portals.
      - `module` (object) **REQ** — Specifies the module's API name and ID.
        - `api_name` (string) **REQ** [maxLen=100] — Specifies the API name of the module.
        - `id` (string) **REQ** [maxLen=19] — Specifies the unique ID of the module.
      - `rule_computation_running` (boolean) **REQ** — Indicates whether a sharing rule computation is currently running for the module. If you rerun a rule configured for a module, this key is true until the process completes. If the value is false, no rules are currently running for the module. **Possible values:** **true** - A sharing rule computation is running for the module. **false** - No sharing rule computation is running for the module.

- **403**: The user does not have the required permission to retrieve data sharing settings. [application/json]
    > Error response returned when the user does not have the Crm_Implied_Manage_Data_Sharing permission to retrieve data sharing settings.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The error code identifying the type of error.
    - `details` (object) **REQ** — Object containing additional error details.
      - `permissions` (array of string) [maxItems=1] **REQ** — Array containing the list of missing permissions required to perform the operation.
        items: [enum=['Crm_Implied_Manage_Data_Sharing']]
    - `message` (string) **REQ** [enum=['permission denied']] — A message describing the error.
    - `status` (string) **REQ** [enum=['error']] — The status of the response.

**Scopes:** ZohoCRM.settings.data_sharing.READ, ZohoCRM.settings.data_sharing.ALL
