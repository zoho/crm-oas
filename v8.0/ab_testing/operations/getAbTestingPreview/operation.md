# GET /settings/AB_testing/{id}/actions/preview
**Operation:** `getAbTestingPreview` — Get AB Testing form preview
> To retrieve the HTML preview details of the base form and variant forms configured for a specific Webform A/B Testing in your Zoho CRM organization.

**Parameters:**
- `id` (path, string, required) [maxLen=19]: Specify the unique [AB Testing ID](ab_testing.yaml#$.paths./settings/AB_testing.get).
- `module` (query, string, required) [enum=['Leads']]: Specify the module API name for the AB test operation. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name. 
Possible values:
**Leads** - Target the Leads module.

**Schemas:**
`ModuleNested`:
  > Represents the CRM module associated with an AB test, identified by its API name and ID.
  - `api_name` (string) [maxLen=50] — Represents the API name of the CRM module associated with the AB test.
  - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the CRM module associated with the AB test.
`VariantFormPreViewNested`:
  > Represents the HTML preview data for a webform, including embed, iframe, and source code formats.
  - `source_code` (string) [maxLen=50000] — Represents the full HTML source code of the webform.
  - `embed_code` (string) [maxLen=2000] — Represents the embeddable script code for the webform.
  - `iframe_code` (string) [maxLen=2000] — Represents the iframe embed code for displaying the webform.
  - `code_formats` (array of string) [maxItems=3] — Represents the list of embed code formats available for this webform.
    items: [maxLen=255]
  - `module` (object `ModuleNested`) — Represents the CRM module associated with an AB test, identified by its API name and ID.
  - `name` (string) [maxLen=100] — Represents the name of the webform.
  - `active` (boolean) — Indicates whether the webform is currently active.
Possible values:
**true** - The webform is active.
**false** - The webform is inactive.
  - `id` (string) [maxLen=19] — Represents the unique identifier of the webform.

**Responses:**

- **200**: Returns the HTML preview details of the base form and variant forms configured for the specified Webform A/B test. — Schema: `GetpreviewResponse200` [application/json]
    > Successful response returned when retrieving the HTML preview of an AB test's forms.
    schema: `GetpreviewResponse200`
    - `AB_testing` (array of object `GetpreviewResponseNested`) [maxItems=1] — Represents the list of AB test preview data, including HTML code for each form.
      schema: `GetpreviewResponseNested`
      - `id` (string) [maxLen=19] — Represents the unique identifier of the AB test included in the preview response.
      - `variant_form` (array of object `VariantFormPreViewNested`) [maxItems=2] — Represents the list of variant webform previews included in the AB test, each with embed, iframe, and source code formats.
      - `base_form` (object `VariantFormPreViewNested`) — Field: base_form
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains invalid data, an invalid module name, or a missing required parameter.
**Resolution:** The mandatory **module** query parameter must be specified with a valid CRM module API name, and the A/B testing ID in the request URL must be a valid record ID. [application/json]
    > Represents the error response for invalid or missing request parameters, including invalid data, an invalid module name, or a missing required parameter.

    anyOf:
      - `ErrorResponseCore1388195357` — Error response returned when a path segment in the request URL contains invalid data.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a resource path in the request URL contains invalid data.
Possible values:
**INVALID_DATA** - The value at the specified resource path index is not valid.
        - `details` (object) **REQ** — Represents the details of the invalid resource path error, including the index of the invalid path segment.
          - `resource_path_index` (integer/int32) — Represents the index of the path segment in the request URL that contains the invalid value.
        - `message` (string) **REQ** [enum=[3 values]] — Represents the error message indicating that the resource path data is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to an invalid resource path.
      - `ErrorResponseCore1335454202` — Error response returned when the module name in the request is not a valid Zoho CRM module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned when the module name in the request is not valid.
Possible values:
**INVALID_MODULE** - The module name specified in the request is not a valid Zoho CRM module.
        - `details` (object) **REQ** — Represents the details of the invalid module error.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message indicating that the module name is not valid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to an invalid module name.
      - `ErrorResponseCore216006943` — Error response returned when a required query parameter is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when a required query parameter is missing from the request.
Possible values:
**REQUIRED_PARAM_MISSING** - A required parameter is absent from the request.
        - `details` (object) **REQ** — Represents the details of the missing parameter error, including the name of the required parameter.
          - `param_name` (string) [maxLen=255] — Represents the name of the required query parameter that is missing from the request.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that a required parameter is missing from the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a missing required parameter.
      - `ErrorResponseCore94581445` — Error response returned when a required query parameter is missing from the request.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code returned when a required query parameter is missing from the request.
Possible values:
**REQUIRED_PARAM_MISSING** - A required parameter is absent from the request.
        - `details` (object) **REQ** — Represents the details of the missing parameter error, including the name of the required parameter.
          - `param_name` (string) [maxLen=255] — Represents the name of the required query parameter that is missing from the request.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Represents the error message indicating that a required parameter is missing from the request.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a missing required parameter.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to access the Webform A/B Testing preview details.
**Resolution:** The CRM administrator must enable the Webform A/B Testing permission for the user's profile on the specified module. — Schema: `PermissionDeniedErrorResponse` [application/json]
    > Error response returned when the requesting user lacks the required CRM permission to perform the action.
    schema: `PermissionDeniedErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when the requesting user lacks the required CRM permission.
Possible values:
**NO_PERMISSION** - The user's CRM profile does not include the required permission for this action.
    - `details` (object) **REQ** — Represents the details of the permission denied error, including the list of required CRM permissions.
      - `permissions` (array of string) [maxItems=25] — Represents the list of CRM permissions required to perform this action.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating that the user does not have permission to perform this action.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to insufficient CRM permissions.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.abtest.READ
