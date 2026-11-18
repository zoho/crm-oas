# GET /settings/AB_testing/{id}
**Operation:** `getABTestingById` — Get AB Testing configuration by ID

> To retrieve the details of a specific AB Testing configuration
 by ID in your Zoho CRM organization.

 The following keys are returned only by this endpoint (retrieving a specific
 A/B Testing) and are not returned when listing all Webform A/B Testing configurations:
   - form_fields, form_attributes, button_attributes, encrypted_form_id, and tracking_code inside each variant_form object.
   - winner_confidence inside base_form and each variant_form object.
   - pause_resume_info at the root level.


**Parameters:**
- `id` (path, string, required) [maxLen=19]: Specify the unique [AB Testing ID](ab_testing.yaml#$.paths./settings/AB_testing.get).
- `module` (query, string, optional) [enum=['Leads']]: Specify the module API name to filter AB test configurations. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name. 
Possible values:
**Leads** - Filter by the Leads module.

**Schemas:**
`ModuleNested`:
  > Represents the CRM module associated with an AB test, identified by its API name and ID.
  - `api_name` (string) [maxLen=50] — Represents the API name of the CRM module associated with the AB test.
  - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the CRM module associated with the AB test.

**Responses:**

- **200**: Returns the AB Testing configuration details for the specified ID, including base form, variant forms, traffic allocation, test conditions, and winner configuration.
 — Schema: `Get111111000000002652Response200` [application/json]
    > Successful response returned when retrieving the details of a specific AB test configuration by ID.
    schema: `Get111111000000002652Response200`
    - `AB_testing` (array of object `AbTestingNested`) [maxItems=1] — Represents the list of AB test configurations returned for the specified AB test ID.
      schema: `AbTestingNested`
      - `dynamic_allocation_by_zia` (boolean) — Indicates whether the traffic allocation between the base form and variant forms is managed dynamically by Zia, the AI assistant.
Possible values:
**true** - Zia dynamically adjusts traffic allocation based on performance.
**false** - Traffic is allocated according to the manually configured split.
      - `code` (string) [maxLen=255] — Represents the response code returned for the AB test operation.
      - `base_form` (object `BaseFormNested`) **REQ** — Represents the base webform in an AB test, including its traffic allocation, performance metrics, and embed code formats.
        schema: `BaseFormNested`
        - `embed_code` (string) [maxLen=255] — Represents the embeddable script code for the webform.
        - `leading` (boolean) — Indicates whether the base form is currently leading in the AB test based on performance metrics.
Possible values:
**true** - The base form is leading.
**false** - The base form is not leading.
        - `module` (object `ModuleNested`) — Represents the CRM module associated with an AB test, identified by its API name and ID.
        - `active` (boolean) — Indicates whether the base webform is currently active.
Possible values:
**true** - The webform is active and accepting submissions.
**false** - The webform is inactive.
        - `iframe_code` (string) [maxLen=255] — Represents the iframe embed code for displaying the webform.
        - `code_formats` (array of string) [maxItems=3] — Represents the list of embed code formats available for this webform.
          items: [maxLen=255]
        - `winner` (boolean) — Indicates whether the base webform has been declared the winner of the AB test.
Possible values:
**true** - The base webform is the declared winner.
**false** - The base webform has not been declared the winner.
        - `old_traffic` (null) — Represents the previous traffic allocation percentage for the base webform before the most recent update. Returns null when no previous allocation exists.
        - `name` (string) [maxLen=255] — Represents the name of the base webform.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the base webform.
        - `no_of_submission` (integer/int32) — Represents the total number of form submissions received by the base webform during the AB test.
        - `winner_confidence` (null) — Represents the statistical confidence level for declaring the base webform as the winner. Returns null when the confidence has not been calculated.
        - `source_code` (string) [maxLen=255] — Represents the full HTML source code of the base webform.
        - `no_of_visits` (integer/int32) — Represents the total number of visitor sessions on the base webform during the AB test.
        - `traffic` (integer/int32) **REQ** — Represents the percentage of visitor traffic allocated to the base webform.
      - `notify` (boolean) — Indicates whether notifications are enabled for this AB test.
Possible values:
**true** - Notifications are sent when the test reaches a significant milestone.
**false** - No notifications are sent.
      - `traffic_diversion` (null) — Represents the traffic diversion configuration for the AB test, if applicable. Returns null when no traffic diversion is configured.
      - `variant_form` (array of object `VariantFormNested`) [maxItems=2] **REQ** — Represents the list of variant webforms included in the AB test, each with its own traffic allocation and performance data.
        schema: `VariantFormNested`
        - `embed_code` (string) [maxLen=255] — Represents the embeddable script code for the variant webform.
        - `encrypted_form_id` (string) [maxLen=255] — Represents the encrypted identifier of the variant webform, used for analytics and tracking.
        - `leading` (boolean) — Indicates whether the variant form is currently leading in the AB test based on performance metrics.
Possible values:
**true** - The variant form is leading.
**false** - The variant form is not leading.
        - `module` (object `ModuleNested`) — Represents the CRM module associated with an AB test, identified by its API name and ID.
        - `button_attributes` (array of object `ButtonAttributesNested`) [maxItems=2] **REQ** — Represents the list of button configurations for the variant webform, including submit and reset buttons.
          schema: `ButtonAttributesNested`
          - `color` (string) [maxLen=255] — Represents the color of the button, specified as a hex code or color name.
          - `name` (string) **REQ** [maxLen=255] — Represents the label text displayed on the button.
        - `active` (boolean) — Indicates whether the variant webform is currently active.
Possible values:
**true** - The webform is active and accepting submissions.
**false** - The webform is inactive.
        - `form_attributes` (object `FormAttributesNested`) — Represents the visual styling configuration of a webform variant, including width, color, font attributes, and alignment.
          schema: `FormAttributesNested`
          - `width` (integer/int32) [enum=[600, 700, 800, 900]] — Represents the width of the webform in pixels.
Possible values:
**600** - 600 pixels.
**700** - 700 pixels.
**800** - 800 pixels.
**900** - 900 pixels.
          - `font_attributes` (object `FontAttributesNested`) — Represents the font styling configuration for a webform, including size, color, and font family.
            schema: `FontAttributesNested`
            - `size` (integer/int32) — Represents the font size used for the form text, in points.
            - `color` (string) [maxLen=255] — Represents the font color of the form text, specified as a hex code or color name.
            - `family` (string) [maxLen=255] — Represents the font family used for the form text.
          - `display_form_name` (boolean) — Indicates whether the form name is displayed on the webform.
Possible values:
**true** - The form name is displayed.
**false** - The form name is not displayed.
          - `color` (string) [maxLen=255] — Represents the background color of the webform, specified as a hex code or color name.
          - `align` (string) [maxLen=255, enum=['right', 'left', 'top']] — Represents the alignment of the webform on the page.
Possible values:
**right** - Align the form to the right.
**left** - Align the form to the left.
**top** - Align the form to the top.
        - `tracking_code` (string) [maxLen=2000] — Represents the analytics tracking script injected into the variant webform for visitor tracking.
        - `iframe_code` (string) [maxLen=255] — Represents the iframe embed code for displaying the variant webform.
        - `code_formats` (array of string) [maxItems=3] — Represents the list of embed code formats available for this variant webform.
          items: [maxLen=255]
        - `winner` (boolean) — Indicates whether the variant webform has been declared the winner of the AB test.
Possible values:
**true** - The variant webform is the declared winner.
**false** - The variant webform has not been declared the winner.
        - `old_traffic` (null) — Represents the previous traffic allocation percentage for the variant webform before the most recent update. Returns null when no previous allocation exists.
        - `name` (string) [maxLen=255] — Represents the name of the variant webform.
        - `id` (string) [maxLen=19] — Represents the unique identifier of the variant webform.
        - `no_of_submission` (integer/int32) — Represents the total number of form submissions received by the variant webform during the AB test.
        - `form_fields` (array of object `FormFieldsNested`) [maxItems=5] **REQ** — Represents the list of form fields included in the variant webform.
          schema: `FormFieldsNested`
          - `type` (string) **REQ** [maxLen=255, enum=['general', 'advanced', 'portal']] — Represents the category of the webform field.
Possible values:
**general** - A standard CRM field.
**advanced** - A specialized or custom field.
**portal** - A portal-specific field.
          - `help` (object) [nullable] — Represents the help configuration for the field, including help text and an optional URL. Returns null when no help is configured.
          - `field` (object `FieldNested`) — Represents a CRM field included in a webform, identified by its API name, field label, and ID.
            schema: `FieldNested`
            - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM field included in the webform.
            - `field_label` (string) [maxLen=255] — Represents the display label of the CRM field as shown on the webform.
            - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the CRM field.
          - `hidden` (boolean) [nullable] — Indicates whether the field is hidden on the webform.
Possible values:
**true** - The field is hidden from visitors.
**false** - The field is visible to visitors.
          - `date_format` (string) [maxLen=50, nullable] — Represents the date format used for date fields in the webform. Returns null when no date format is specified.
          - `required` (boolean) [nullable] — Indicates whether the field is required on the webform.
Possible values:
**true** - The field must be filled in before the form can be submitted.
**false** - The field is optional.
          - `field_name` (string) [maxLen=255, nullable] — Represents the display name of the field as shown on the webform.
          - `site_key` (string) [maxLen=50, nullable] — Represents the site key used to render the reCAPTCHA widget on the webform.
          - `secret_key` (string) [maxLen=50, nullable] — Represents the secret key used for reCAPTCHA verification on the webform.
          - `recaptcha_label` (string) [maxLen=50, nullable] — Represents the label displayed for the reCAPTCHA field on the webform.
          - `theme` (string) [maxLen=5, enum=['dark', 'light'], nullable] — Represents the visual theme applied to the reCAPTCHA widget.
Possible values:
**dark** - The reCAPTCHA uses a dark color scheme.
**light** - The reCAPTCHA uses a light color scheme.
          - `privacy_value` (string) [maxLen=2000, nullable] — Represents the privacy policy content displayed in the privacy policy field on the webform.
          - `default_value` (string) [maxLen=32000, nullable] — Represents the default value pre-populated in the hidden field on the webform.
          - `field_info` (object `AdvanceFieldNested`) — Represents an advanced or custom field type included in a webform variant.
            schema: `AdvanceFieldNested`
            - `type` (string) **REQ** [maxLen=255] — Represents the API name that identifies the type of the advanced webform field.
            - `field_label` (string) [maxLen=255] — Represents the display label of the advanced webform field.
        - `winner_confidence` (null) — Represents the statistical confidence level for declaring the variant webform as the winner. Returns null when the confidence has not been calculated.
        - `source_code` (string) [maxLen=255] — Represents the full HTML source code of the variant webform.
        - `no_of_visits` (integer/int32) — Represents the total number of visitor sessions on the variant webform during the AB test.
        - `traffic` (integer/int32) **REQ** — Represents the percentage of visitor traffic allocated to the variant webform.
      - `pause_resume_info` (null) — Represents information about a pause or resume action on the AB test, if applicable. Returns null when no pause or resume action has occurred.
      - `id` (string) [maxLen=19] — Represents the unique identifier of the AB test configuration.
      - `traffic` (integer/int32) — Represents the total percentage of visitor traffic allocated to this AB test.
      - `created_time` (string) [maxLen=255] — Represents the creation date and time of the AB test configuration.
      - `complete_restart_info` (null) — Represents information about a complete restart of the AB test, if applicable. Returns null when no restart has occurred.
      - `started_time` (string) [maxLen=255] — Represents the actual date and time when the AB test started running.
      - `module` (object `ModuleNested`) **REQ** — Represents the CRM module associated with an AB test, identified by its API name and ID.
      - `suggestion` (null) — Represents the AI-generated suggestion for the AB test, if available. Returns null when no suggestion is available.
      - `created_by` (object `CreatedByNested`) — Represents the CRM user who created the AB test configuration.
        schema: `CreatedByNested`
        - `name` (string) [maxLen=255] — Represents the full name of the user who created the AB test.
        - `id` (string) [maxLen=19] — Represents the unique identifier of the user who created the AB test.
      - `start_time` (string) [maxLen=255] — Represents the scheduled start time of the AB test.
      - `visitors` (integer/int32) — Represents the total number of visitors who have been exposed to the AB test.
      - `condition` (object `ConditionNested`) **REQ** — Represents the condition that determines when an AB test ends, including the condition type, period, unit, and remaining time.
        schema: `ConditionNested`
        - `visitors` (integer/int32) — Represents the target number of visitor sessions required to complete the AB test when the condition type is **visits**.
        - `unit` (integer/int32) — Represents the numeric value of the test condition, such as the number of days, weeks, months, or visitor sessions.
        - `period` (string) [maxLen=255, enum=['days', 'weeks', 'months']] — Represents the time period unit used for a duration-based test condition.
Possible values:
**days** - The duration is measured in days.
**weeks** - The duration is measured in weeks.
**months** - The duration is measured in months.
        - `from` (string/date-time) [maxLen=25] — Represents the start date and time of the AB test when the condition type is **range**.
        - `to` (string/date-time) [maxLen=25] — Represents the end date and time of the AB test when the condition type is **range**.
        - `type` (string) **REQ** [maxLen=255, enum=['duration', 'range', 'visits']] — Represents the type of condition used to determine when the AB test ends.
Possible values:
**duration** - The test runs for a fixed period.
**range** - The test runs between a start and end date.
**visits** - The test ends after a target number of visitor sessions.
        - `remaining` (integer/int32) — Represents the number of days or visits remaining before the AB test condition is met.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the AB test configuration.
      - `days` (integer/int32) — Represents the number of days the AB test has been running.
      - `winner_configuration` (object `WinnerConfigurationNested`) — Represents the winner declaration configuration for an AB test, including automatic announcement settings and the conversion percentage difference threshold.
        schema: `WinnerConfigurationNested`
        - `announce_automatically` (boolean) [enum=[True, False]] — Indicates whether the winning form is announced automatically when the conversion percentage difference threshold is met.
Possible values:
**true** - The winner is announced automatically.
**false** - The winner must be announced manually.
        - `conversion_percentage_difference` (integer/int32) — Represents the minimum conversion rate percentage difference required to automatically declare a winner. Required when **announce_automatically** is **true**.
      - `status` (string) **REQ** [maxLen=255, enum=['drafted', 'running', 'scheduled', 'completed', 'launched', 'paused']] — Represents the current lifecycle status of the AB test.
Possible values:
**drafted** - The test exists but has not started.
**running** - The test actively distributes traffic.
**scheduled** - The test starts at a future date.
**paused** - The test has stopped temporarily.
**completed** - The test has finished and results are available.
**launched** - The winning form has launched.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: No AB Testing configuration found for the specified ID.

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The module name is invalid or the required module parameter is missing.
**Resolution:** The module API name in the request must be valid, and the module query parameter must be included.
 [application/json]
    > Represents the error response body when the request fails due to a missing or invalid module parameter.

    anyOf:
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
      - `ErrorResponseCore1335454202` — Error response returned when the module name in the request is not a valid Zoho CRM module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned when the module name in the request is not valid.
Possible values:
**INVALID_MODULE** - The module name specified in the request is not a valid Zoho CRM module.
        - `details` (object) **REQ** — Represents the details of the invalid module error.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message indicating that the module name is not valid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to an invalid module name.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to retrieve the AB Testing configuration.
**Resolution:** The CRM administrator must grant the required permission to the user's profile.
 — Schema: `PermissionDeniedErrorResponse` [application/json]
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
