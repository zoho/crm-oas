# GET /settings/module/{moduleid}/actions/generate_link
**Operation:** `getGenerateLink` — Generate web-tab link for a module
> To generate the configured web-tab link for a specific module in your Zoho CRM organization. The moduleid path parameter must be the module's API name (e.g., Leads, Contacts, Custom_Module_1).

**Parameters:**
- `moduleid` (path, string, required) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*[A-Za-z0-9]$]: Specify the API name of the module for which the web tab link has to be generated. This is case-sensitive Case-sensitive and should start with a letter and contain only alphanumeric characters and underscores.

**Responses:**

- **200**: Returns the generated web-tab link for the specified module. — Schema: `ModuleWebTabLinkResponse` [application/json]
    > Represents the response containing the generated web tab link for a CRM module, with the link details available in the generate_link property.
    schema: `ModuleWebTabLinkResponse`
    - `generate_link` (object `ModuleWebTabLink`) **REQ** — Represents a web tab link associated with a CRM module, including the tab identifier (id, int64), display name(name), and configured URL(web_link).
      schema: `ModuleWebTabLink`
      - `name` (string) **REQ** [maxLen=50, minLen=3] — Represents the display name of the web tab.
      - `id` (string/int64) **REQ** [maxLen=20, minLen=18, pattern=\d+] — Represents the unique ID of the web tab.
      - `web_link` (string) **REQ** [maxLen=1000] — Represents the URL configured for the web tab.

- **400**: The module name given seems to be invalid.
**Resolution:** The module API name in the request path must match the API name of an existing module. [application/json]
    > Represents the error response returned when the provided module API name is invalid.
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned for the request.
    - `details` (object) **REQ** — Represents additional context about the cause of the error.
      - `param_name` (string) **REQ** [enum=['module']] — Represents the name of the invalid parameter in the request.
    - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message describing the issue with the request.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.

**Scopes:** ZohoCRM.settings.modules.READ
