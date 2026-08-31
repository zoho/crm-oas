# GET /settings/call_preferences
**Operation:** `getCallPreferences` — Call Preferences
> To retrieve the current Call Preferences configuration for your Zoho CRM organization. The response reports whether the **From Number** and **To Number** fields are currently enabled on records in the Calls module.

**Responses:**

- **200**: Returns the current Call Preferences configuration for the Zoho CRM organization, reporting whether the **From Number** and **To Number** fields are enabled on records in the Calls module. [application/json]
    > Returned when the Call Preferences configuration is successfully retrieved. Contains the **call_preferences** object with the current visibility setting for each preference.
    - `call_preferences` (object) — Contains the current Call Preferences configuration for your Zoho CRM organization in the **Calls** module.
      - `show_from_number` (boolean) **REQ** — Indicates whether the **From Number** field is currently enabled on records in the Calls module. 
**Possible values:**
**true** - The **From Number** field is enabled and appears on Call records.
**false** - The **From Number** field is disabled and is hidden from Call records.
      - `show_to_number` (boolean) **REQ** — Indicates whether the **To Number** field is currently enabled on records in the Calls module. 
**Possible values:**
**true** - The **To Number** field is enabled and appears on Call records.
**false** - The **To Number** field is disabled and is hidden from Call records.

- **403**: The user does not have permission to access call preferences. [application/json]
    > Represents the error response returned when the user does not have permission to perform this operation.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the authorization failure. The value is **NO_PERMISSION**.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the authorization failure.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status. The value is **error**.
    - `details` (object) **REQ** — Represents the error details with authorization information.
      - `permissions` (array of string) [maxItems=10] — Represents the list of permissions required for this operation.
        items: [maxLen=255]

**Scopes:** ZohoCRM.settings.modules.read
