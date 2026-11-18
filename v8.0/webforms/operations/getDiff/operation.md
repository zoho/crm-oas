# GET /settings/webforms/diff
**Operation:** `getDiff` — Get webform diff
> Retrieves the field-level differences between two webforms in
the CRM organization. The base_form and variant_form query parameters 
identify the two forms to compare. The response lists all fields that 
differ between the two forms, including added, removed, and modified 
fields.

 **Notes:**
  - The base and variant forms must belong to the same module.
  - The base and variant forms must not be the same Webform.
  - If there are no differences between the base and variant forms, the response returns an empty array.


**Parameters:**
- `base_form` (query, number, required) [enum=[111111000000114140]]: Specify the ID of the base webform for comparison in an A/B testing diff request. Use the [Get Webforms API](webforms.yaml#$.paths./settings/webforms.get) to retrieve the webform ID.
- `variant_form` (query, number, required) [enum=[111111000000114400]]: Specify the ID of the variant webform for comparison in an A/B testing diff request.

**Schemas:**
`DiffFieldsNested`:
  > Represents the configuration of a field modified in the comparison between the base and variant webforms.
  - `help` (object `HelpNested`) — Represents the help text configuration for a webform field, including the text, URL, and status.
  - `display_label` (string) [maxLen=255] — Represents the display label of the field as shown on the webform.
  - `type` (string) **REQ** [maxLen=255, enum=['general', 'advanced', 'portal']] — Represents the type classification of the field as configured on the webform.
  - `field` (object) — Represents the field reference object identifying the CRM field associated with this diff entry.
    - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM field.
    - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the CRM field.
    - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM field.
  - `field_info` (object) — Represents the field metadata object containing additional information about the CRM field in this diff entry.
    - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the CRM field in the diff field metadata.
    - `type` (string) **REQ** [maxLen=255] — Represents the data type of the field as defined in the CRM module configuration.
  - `required` (boolean) — Indicates whether the field is required on the webform. Possible values: true - The field is required. false - The field is not required.
  - `hidden` (boolean) — Indicates whether the field is hidden on the webform. Possible values: true - The field is hidden. false - The field is visible.
`ErrorResponse`:
  > Represents a generic API error response containing an error code, status, message, and details.
  - `code` (string) **REQ** [enum=[18 values]] — Represents the error code that identifies the type of error returned by the API.
  - `details` (object) **REQ** — Represents additional details providing context about the error, such as the invalid field name or parameter.
  - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the reason for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.
`HelpNested`:
  > Represents the help text configuration for a webform field, including the text, URL, and status.
  - `text` (string) **REQ** [maxLen=255] — Represents the help text displayed to the visitor alongside the webform field.
  - `url` (string) **REQ** [maxLen=255] — Represents the URL linked to the help content for the webform field.
  - `status` (string) **REQ** [maxLen=255] — Represents the status of the help text configuration for the webform field.

**Responses:**

- **200**: Returns the diff result between the specified base and variant webform, including modified, added, and removed fields. — Schema: `GetdiffResponse200` [application/json]
    > Represents the diff response comparing the base and variant webforms, including the list of structural differences.
    schema: `GetdiffResponse200`
    - `diff` (array of object `DiffNested`) [maxItems=1] **REQ** — Contains the list of diff objects representing the differences between the base and variant webforms.
      schema: `DiffNested`
      - `modified_fields` (array of object `DiffFieldsNested`) [maxItems=50, nullable] **REQ** — Contains the list of fields modified in the variant webform compared to the base webform.
      - `added_fields` (array of object `DiffFieldsNested`) [maxItems=50, nullable] **REQ** — Contains the list of fields added to the variant webform compared to the base webform.
      - `button_attributes` (array of object `ButtonAttributesNested1`) [maxItems=2, nullable] **REQ** — Contains the button attribute differences between the base and variant webforms.
        schema: `ButtonAttributesNested1`
        - `name` (string) [maxLen=255] — Represents the internal name identifier of the button attribute configuration within the webform.
        - `label` (string) [maxLen=255] — Specifies the display label shown on the button in the webform.
      - `form_attributes` (object `FormAttributesNested2`) **REQ** — Field: form_attributes
        schema: `FormAttributesNested2`
        - `color` (string) [maxLen=255] — Specifies the background color of the webform.
        - `width` (string) [maxLen=255] — Specifies the width of the webform.
        - `align` (string) [maxLen=255] — Specifies the horizontal alignment of the webform content.
        - `font_attributes` (object) — Represents the nested font attribute settings applied to the webform text.
          - `color` (string) [maxLen=255] — Represents the nested font attribute settings applied to the webform text.
          - `size` (string) [maxLen=255] — Represents the nested font attribute settings applied to the webform text.
          - `family` (string) [maxLen=255] — Represents the nested font attribute settings applied to the webform text.
      - `removed_fields` (array of object `DiffFieldsNested`) [maxItems=50, nullable] **REQ** — Contains the list of fields removed from the variant webform compared to the base webform.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: One or more required query parameters are missing or contain invalid values.
**Resolution:** The request must include valid base_form and variant_form query parameters, each containing a distinct webform ID that belongs to the correct module. [application/json]
    > Represents the error response returned when the webform diff request contains invalid or missing parameters.
    anyOf:
        - `webforms` (array of object `ErrorResponse`) [maxItems=25] **REQ** — Represents the list of error objects returned when the diff request fails due to invalid or missing parameters.
      - `ErrorResponse` — Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied.
**Resolution:** An administrator must grant the user's CRM profile the required permission (Crm_Implied_Web_To_Cases) to access webform diff comparison. — Schema: `ErrorResponse` [application/json]
    > Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.READ
