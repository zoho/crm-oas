# GET /settings/portals/{portal}
**Operation:** `getPortal` — Specific Portal
> To retrieve the complete configuration of a specific portal in the Zoho CRM organization, including its SAML authentication settings, active status, and creation metadata.

**Parameters:**
- `portal` (path, string, required) [maxLen=60]: Specify the API name of the portal to retrieve or update. Use the Get Portals operation to retrieve the list of available portals and their names.

**Responses:**

- **200**: Returns the complete configuration of the specified portal, including SAML settings and metadata. [application/json]
    > Represents the 200 response schema for getting a portal by identifier, containing the full portal configuration.
    - `portals` (array of object) [maxItems=100] **REQ** — Represents the list of portal objects returned by the response.
      - `name` (string) [maxLen=50] — Represents the unique name of the portal.
      - `created_time` (string/date-time) **REQ** — Represents the timestamp when the portal was first added.
      - `modified_time` (string/date-time) **REQ** — Represents the timestamp when the portal configuration was last modified.
      - `modified_by` (object) **REQ** — Represents the Zoho CRM user who last modified this portal.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified this portal.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who last modified this portal.
      - `created_by` (object) **REQ** — Represents the Zoho CRM user who created this portal.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the CRM user who created this portal.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM user who created this portal.
      - `zaid` (string) **REQ** [maxLen=255] — Represents the Zoho account ID (`zaid`) associated with the portal.
      - `active` (boolean) **REQ** — Indicates whether the portal is active.
      - `saml_configuration` (object) **REQ** — Represents the SAML authentication configuration for the portal.
        - `login_url` (string) **REQ** [maxLen=2048] — Represents the SAML SSO login URL where the portal redirects users for authentication.
        - `logout_url` (string) **REQ** [maxLen=2048, pattern=http[s]://www[.][a-z]{7}[.]com] — Represents the SAML SSO logout URL where the portal redirects users when they sign out. Must begin with `https://www.`.
        - `public_key` (string) **REQ** [maxLen=5000, enum=[1 values]] — Represents the SAML X.509 public key certificate used to verify assertions from the identity provider.
        - `active` (boolean) **REQ** [enum=[True]] — Indicates whether the SAML configuration is active for the portal. Possible values: **true** - SAML SSO is enabled.
        - `modified_by` (object) — Represents the Zoho CRM user who last modified this SAML configuration.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the user who last modified this SAML configuration.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who last modified this SAML configuration.
        - `created_by` (object) — Represents the Zoho CRM user who created this SAML configuration.
          - `name` (string) **REQ** [maxLen=255] — Represents the name of the CRM user who created this SAML configuration.
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM user who created this SAML configuration.
      - `login_url` (string) [maxLen=2048] — Represents the login URL for the portal. Displayed on the portal login page.
      - `acs_url` (string) [maxLen=2048] — Represents the Assertion Consumer Service (ACS) URL for the portal.
      - `admin_zuid` (integer/int32) — Represents the Zoho account zone ID of the portal administrator.
      - `default_relay_state_url` (string) [maxLen=2048] — Represents the default relay state URL used after a successful SAML login.
      - `issuer` (string) [maxLen=2048] — Represents the SAML issuer identifier (entity ID) for the portal.
      - `single_logout_url` (string) [maxLen=2048] — Represents the single logout URL (SLO) used to terminate SAML sessions across all service providers.

- **204**: No portal has been created for this organization. The response body is empty.

- **400**: The API is not supported in the current environment. Resolution: Retry the request in a production environment. [application/json]
    > Represents the API_NOT_SUPPORTED error returned when the Get Portal API is called in a sandbox environment.
    - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code for this response.
Possible values: **API_NOT_SUPPORTED** - the API is not supported in the current environment. 
    - `details` (object) **REQ** — Represents additional error context.
      - `unsupported_environment` (string) [maxLen=255] — Represents the environment type that does not support this API.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the failure.
    - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. 

- **403**: The authenticated user does not have the required `ZohoCRM.settings.clientportal.READ` permission. Resolution: Ensure the access token includes the correct scope. [application/json]
    > Represents the NO_PERMISSION error returned when the authenticated user lacks the required portal read permission.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
Possible values: **NO_PERMISSION** - the authenticated user lacks the required permission. 
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing permission.
    - `details` (object) **REQ** — Represents additional context about the missing permission.
      - `permissions` (array of string) [maxItems=100] — Represents the list of required permission identifiers that the user lacks.
        items: [maxLen=255]
    - `status` (string) **REQ** [enum=['error']] — Represents the overall response status.
Possible values: **error** - the request failed. 

**Scopes:** ZohoCRM.settings.clientportal.READ
