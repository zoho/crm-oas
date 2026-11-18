# GET /settings/webforms/{id}/actions/preview
**Operation:** `getWebformPreview` — Retrieve webform source code and embed options

> To retrieve the HTML source code and embed options for a specific webform configured in your Zoho CRM organization.


**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specify the unique [Webform ID](webforms.yaml#$.paths./settings/webforms.get).
- `module` (query, string, required) [enum=['Leads']]: Specify the module API name of the CRM module for which the webform is being created or updated. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Schemas:**
`ErrorResponse`:
  > Represents a generic API error response containing an error code, status, message, and details.
  - `code` (string) **REQ** [enum=[18 values]] — Represents the error code that identifies the type of error returned by the API.
  - `details` (object) **REQ** — Represents additional details providing context about the error, such as the invalid field name or parameter.
  - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the reason for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.

**Responses:**

- **200**: Returns the source code and embed options for the specified webform, including the embed code, available code formats, associated module details, form name, active status, smart URL, type, source code, and iframe code.
 — Schema: `GetpreviewResponse200` [application/json]
    > Represents the webform preview response, including the source code and embed code options for the webform.
    schema: `GetpreviewResponse200`
    - `webforms` (array of object `WebformsNested5`) [maxItems=1] **REQ** — Contains the list of webform objects with their embed code and source code information.
      schema: `WebformsNested5`
      - `embed_code` (string) **REQ** [maxLen=2000] — Represents the HTML embed code used to embed the webform into an external web page.
      - `code_formats` (array of string) [maxItems=5] **REQ** — Contains the list of embed code format options available for the webform.
        items: [maxLen=255]
      - `module` (object `ModuleNested`) **REQ** — Represents the CRM module associated with the webform, including its API name and identifier.
        schema: `ModuleNested`
        - `api_name` (string) **REQ** [maxLen=50] — Represents the display name of the user who created the webform.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the user who created the webform.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the webform.
      - `active` (boolean) **REQ** — Indicates whether the webform is active. Possible values: true - The webform is active. false - The webform is inactive.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the webform.
      - `smart_url` (string) **REQ** [maxLen=255] — Represents the smart URL generated for the webform, which can be shared directly with visitors.
      - `type` (string) **REQ** [maxLen=255] — Represents the type of the form. Possible values: webform - A standard webform. portalform - A portal form for registered portal users.
      - `source_code` (string) **REQ** [maxLen=200000] — Represents the raw HTML source code of the webform.
      - `iframe_code` (string) **REQ** [maxLen=200000] — Represents the iframe embed code used to embed the webform in an iframe on an external web page.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Occurs when the request contains invalid or missing parameters, such as an unrecognized module value, a malformed or invalid form identifier, or a required query parameter that is absent.
 — Schema: `ErrorResponse` [application/json]
    > Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: permission denied.
**Resolution:** The Zoho CRM administrator must grant the required permission to the user's profile. — Schema: `ErrorResponse` [application/json]
    > Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.READ
