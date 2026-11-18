# GET /settings/wizards
**Operation:** `getAllWizards` — Get all wizard configurations
> To retrieve the wizard configurations available in your Zoho CRM organization. The response can be filtered by module using the `**module**` query parameter.

**Parameters:**
- `module` (query, string, optional) [maxLen=50]: Specify the API name of the module for which you want to retrieve wizards. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Responses:**

- **200**: Returns the list of wizards configured in the Zoho CRM organization, including their basic details such as associated module, assigned profiles, and portal types. [application/json]
    > Contains a list of wizard objects returned for the account.
    - `wizards` (array of object) [maxItems=25] **REQ** — Contains the list of wizards configured in the Zoho CRM organization.
      - `created_time` (string/date-time) **REQ** — Represents the creation date and time of the wizard.
      - `modified_time` (string/date-time) **REQ** — Represents the last modification date and time of the wizard.
      - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the wizard, localized based on the active language setting in the user's CRM environment.
      - `portal_user_types` (array of object) [maxItems=50, nullable] **REQ** — Contains the client portal user types associated with the wizard. Returns null if no portal user types are configured.
        - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the client portal, translated into the user's language where a translation is available.
        - `name` (string) **REQ** [maxLen=255] — Internal name of the client portal.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique numeric identifier of the client portal user type.
      - `module` (object) **REQ** — Represents the CRM module associated with the wizard. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
        - `api_name` (string) **REQ** [maxLen=255] — API name of the module associated with the wizard.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the module.
      - `name` (string) **REQ** [maxLen=30] — Represents the unique name of the wizard used in API requests and responses.
      - `modified_by` (object) **REQ** — Represents the details of the user who last modified the wizard.
        - `name` (string) **REQ** [maxLen=255] — Represents the full name of the user who last modified the wizard, as it appears in Zoho CRM.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique numeric identifier of the user who last modified the wizard.
      - `profiles` (array of object) [maxItems=50, nullable] **REQ** — Contains the list of CRM profiles associated with the wizard. Returns null when no profiles are associated.
        - `name` (string) **REQ** [maxLen=255] — Name of the profile.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the profile.
        - `display_label` (string) [maxLen=255] — Represents the display label of the profile, translated into the user's language where a translation is available.
      - `active` (boolean) **REQ** — Indicates whether the wizard is currently enabled.

Possible values:
true - The wizard is active and available for use.
false - The wizard is inactive and not available for use.

      - `source` (string) [maxLen=50, enum=['crm', 'platform_plugin', 'marketplace_plugin']] — Indicates the origin from which the wizard originates.

Possible values:
crm - Created natively within Zoho CRM.
platform_plugin - Created via a Zoho platform plugin.
marketplace_plugin - Created through a Zoho Marketplace plugin.

      - `containers` (array of object) [maxItems=7] **REQ** — Contains the list of containers within the wizard, each defining a layout and the screens through which users progress.
        - `layout` (object) **REQ** — Represents the layout associated with the container, from which the wizard fields are sourced.
          - `name` (string) **REQ** [maxLen=50] — Name of the layout.
          - `display_label` (string) **REQ** [maxLen=50] — Represents the display label of the layout, localized based on the active language setting.
          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the layout.
        - `screens` (array of object) [maxItems=75] **REQ** — Contains the list of screens that define the step-by-step flow a user navigates within this container.
          - `api_name` (string) **REQ** [maxLen=255] — Represents the programmatic name used to identify the screen in API requests and responses.
          - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the screen.
          - `display_label` (string) **REQ** [maxLen=255] — Represents the display label of the screen, localized based on the active language setting.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the container.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Numeric unique identifier of the wizard.
      - `created_by` (object) **REQ** — Represents the user who originally created the wizard, including their identifier and display name.
        - `name` (string) **REQ** [maxLen=255] — Represents the full name of the user who created the wizard, as it appears in Zoho CRM.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique numeric identifier of the user who created the wizard.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Returns no content when no wizards match the specified criteria or no wizards have been configured in the Zoho CRM organization.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The module API name provided in the request is not recognized.
**Resolution:** The module API name in the request URL must be valid. [application/json]
    > Represents the error response returned when the request contains an invalid module name or query parameters.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the request status.
Possible values:
error - Indicates the request failed.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this response.
Possible values:
INVALID_MODULE - Indicates the specified module is invalid.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the request failed.
        - `details` (object) **REQ** — Additional information about the error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **401**: Authentication credentials are missing or invalid.
**Resolution:** A new access token must be generated with the correct scope and valid credentials for this API. [application/json]
    > Represents the error response returned when the request cannot be authenticated due to missing, invalid, or insufficient credentials.
    oneOf:
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code for this response.
Possible values:
OAUTH_SCOPE_MISMATCH - Indicates the OAuth token does not have the required scope to access this resource.
        - `details` (object) **REQ** — Represents additional information about the error.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the request failed.
        - `status` (string) **REQ** [enum=['error']] — Represents the request status.
Possible values:
error - Indicates the request failed.
        - `code` (string) **REQ** [enum=['INVALID_TOKEN']] — Represents the error code for this response.
Possible values:
INVALID_TOKEN - Indicates the provided authentication token is invalid.
        - `details` (object) **REQ** — Represents additional information about the error.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the request failed.
        - `status` (string) **REQ** [enum=['error']] — Represents the request status.
Possible values:
error - Indicates the request failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: The authenticated user's profile does not have permission to retrieve wizard configurations.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response returned when the authenticated user does not have permission to retrieve wizards.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response.
Possible values:
NO_PERMISSION - Indicates the user does not have the required permissions to access this resource.
    - `details` (object) **REQ** — Represents additional information about the permission requirements that caused the request to be rejected.
      - `permissions` (array of string) [maxItems=50] **REQ** — Contains the list of permissions required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the request failed.
    - `status` (string) **REQ** [enum=['error']] — Represents the request status.
Possible values:
error - Indicates the request failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **404**: The request URL does not match a recognized API endpoint pattern.
**Resolution:** The request URL must match a valid API endpoint pattern. [application/json]
    > Represents the error response returned when the requested URL does not match a recognized pattern.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the request status.
Possible values:
error - Indicates the request failed.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for this response.
Possible values:
INVALID_URL_PATTERN - Indicates the requested URL does not match a recognized pattern.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the resource could not be found.
        - `details` (object) **REQ** — Represents additional context about the error, if available.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.wizards.READ
