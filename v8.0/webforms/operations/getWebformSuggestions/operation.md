# GET /settings/webforms/{id}/actions/suggestions
**Operation:** `getWebformSuggestions` — Get optimization suggestions for a webform
> To retrieve AI-powered optimization suggestions for a specific webform in Zoho CRM, including recommended fields, format improvements, and variant configurations based on the webform performance data.


**Parameters:**
- `id` (path, string, required) [maxLen=18]: Specify the unique [Webform ID](webforms.yaml#$.paths./settings/webforms.get).

**Responses:**

- **200**: Returns a list of AI-generated suggestions for the specified webform, including the suggestion type, details about the reason for each suggestion, and the recommended variant configuration.
 — Schema: `GetsuggestionsResponse200` [application/json]
    > Represents a successful response for webform suggestions, containing the list of improvement suggestions.
    schema: `GetsuggestionsResponse200`
    - `webform_suggestions` (array of object `GETWebformSuggestionsNested`) [maxItems=1] **REQ** — Contains the list of webform suggestion objects for improving the webform's performance.
      schema: `GETWebformSuggestionsNested`
      - `suggestion_details` (object `GETSuggestionDetailsNested`) **REQ** — Represents the details of a webform suggestion, including the reason and suggested variant information.
        schema: `GETSuggestionDetailsNested`
        - `reason` (object `GETReasonNested`) **REQ** — Represents the reason data for a webform suggestion, including the conversion rate and list of low-filled fields.
          schema: `GETReasonNested`
          - `low_filled_rate_fields` (array of object `GETLowFilledRateFieldsNested`) [maxItems=2] **REQ** — Contains the list of CRM fields with low form-fill rates, used to identify underperforming fields on the webform.
            schema: `GETLowFilledRateFieldsNested`
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM field with a low form-fill rate.
            - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the CRM field with a low form-fill rate.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM field with a low form-fill rate.
          - `conversion_rate` (string) **REQ** [maxLen=255] — Represents the conversion rate of the webform, indicating the percentage of visitors who submitted the form.
        - `suggested_variant_info` (object `GETSuggestedVariantInfoNested`) **REQ** — Represents the suggested configuration for a variant webform, including button attributes, fields, and form attributes.
          schema: `GETSuggestedVariantInfoNested`
          - `button_attributes` (array of object `GETButtonAttributesNested`) [maxItems=2] **REQ** — Contains the list of button attribute configurations suggested for the variant webform.
            schema: `GETButtonAttributesNested`
            - `color` (string) **REQ** [maxLen=255] — Specifies the color applied to the button element within the webform.
            - `name` (string) **REQ** [maxLen=255] — Represents the internal name identifier of the button attribute within the webform.
          - `fields` (array of object `GETFieldsNested`) [maxItems=2] **REQ** — Contains the list of field configurations suggested for the variant webform.
            schema: `GETFieldsNested`
            - `help` (object `GETHelpNested`) **REQ** — Field: help
              schema: `GETHelpNested`
              - `text` (string) **REQ** [maxLen=255] — Represents the help text displayed to the visitor alongside the webform field.
              - `url` (null) **REQ** — Represents the URL linked to the help content for the webform field.
            - `hidden` (boolean) **REQ** — Indicates whether the field is hidden on the webform. Possible values: true - The field is hidden. false - The field is visible.
            - `advanced` (boolean) **REQ** — Indicates whether the field is configured as an advanced field on the webform. Possible values: true - The field is an advanced field. false - The field is not an advanced field.
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM field configured on the webform.
            - `field_label` (string) **REQ** [maxLen=255] — Represents the display label of the CRM field as shown on the webform.
            - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM field configured on the webform.
            - `required` (boolean) **REQ** — Indicates whether the field is required on the webform. Possible values: true - The field is required. false - The field is not required.
            - `field_name` (string) **REQ** [maxLen=255] — Represents the display name of the CRM field as shown on the webform.
          - `form_attributes` (object `GETFormAttributesNested`) **REQ** — Represents the visual configuration retrieved for the webform, including color, width, alignment, and font attributes.
            schema: `GETFormAttributesNested`
            - `color` (string) **REQ** [maxLen=255] — Specifies the background color of the webform.
            - `width` (integer/int32) **REQ** — Specifies the width of the webform in pixels.
            - `font_attributes` (object `GETFontAttributesNested`) **REQ** — Represents the font attribute settings applied to the webform text, including font size, color, and family.
              schema: `GETFontAttributesNested`
              - `size` (integer/int32) **REQ** — Specifies the font size applied to the text in the webform.
              - `color` (string) **REQ** [maxLen=255] — Specifies the font color applied to the text in the webform.
              - `family` (string) **REQ** [maxLen=255] — Specifies the font family applied to the text in the webform.
            - `align` (string) **REQ** [maxLen=255] — Specifies the horizontal alignment of the webform content.
      - `type` (string) **REQ** [maxLen=255] — Represents the type classification of the webform suggestion.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Indicates that the request was successful but no suggestions are currently available for the specified webform.

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The webform ID in the request path is invalid.
**Resolution:** The webform ID supplied in the request path must be a valid, existing webform ID in the Zoho CRM organization. — Schema: `ErrorResponseCore1126545123` [application/json]
    > Invalid webformId
    schema: `ErrorResponseCore1126545123`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code that identifies the type of error, such as an invalid webform ID.
    - `details` (object) **REQ** — Represents additional details providing context about the error, such as the path index of the invalid resource.
      - `resource_path_index` (integer/int32) **REQ** — Represents the index of the resource in the request path that caused the error.
    - `message` (string) **REQ** [enum=['The id given seems to be invalid.']] — Represents the error message describing the reason for the invalid webform ID failure.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied. The response details identify the specific missing permission.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `ErrorResponseCore470490972` [application/json]
    > Permission Denied
    schema: `ErrorResponseCore470490972`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the type of error, such as a permission denial.
    - `details` (object) **REQ** — Represents additional details about the permission denial, such as the permissions that are missing.
      - `permissions` (array of string) [maxItems=25] **REQ** — Contains the list of CRM permissions that the user's profile lacks for the requested operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the permission denial.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.READ
