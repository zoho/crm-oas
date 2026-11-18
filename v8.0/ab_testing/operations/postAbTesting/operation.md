# POST /settings/AB_testing
**Operation:** `postAbTesting` — Create AB testing configuration
> To create a Webform A/B Test in your Zoho CRM organization.
Webform A/B testing lets you run an experiment where two or more variations of a webform are shown to different segments of your website visitors, so you can compare their performance and identify the version that delivers the best results. This API creates the A/B test — you specify the base (original) webform, one or more variant webforms, the target traffic split, and how long the test should run. 
- **Key terminology:**
    - **Original form:** The existing webform you want to run the A/B test on.
      Referenced by base_form in the request.
    - **Variant:** A modified version of the original webform used for comparison.
      Configured under variant_form.
    - **Conversion rate:** The percentage of visitors who submitted the webform.
    - **Winner:** The webform with the highest conversion rate at the end of the test.


**Parameters:**
- `module` (query, string, required) [enum=['Leads']]: Specify the module API name for the AB test operation. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name. 
Possible values:
**Leads** - Target the Leads module.

**Schemas:**
`ErrorResponseCore1311222188`:
  > Error response returned when a field in the request body contains invalid data.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request body data is invalid.
Possible values:
**INVALID_DATA** - The value provided for the field does not meet the required constraints.
  - `details` (object) **REQ** — Represents the details of the invalid data error, including the field name, JSON path, and maximum allowed length.
    - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field value.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the invalid data.
    - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the invalid data.
  - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message indicating that the field data is invalid.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to invalid data.

**Request Body** — application/json `PostabtestingRequest`
> The request body must contain an AB_testing array with one object.
  > Request body schema for creating a new AB test configuration.
  - `AB_testing` (array of object `PostabtestingRequestBodyNested`) [maxItems=1] **REQ** — Represents the array of AB test configurations to create. The request body must contain a **AB_testing** array with one object.
    schema: `PostabtestingRequestBodyNested`
    - `dynamic_allocation_by_zia` (boolean) — Specify whether to enable Zia-based dynamic traffic allocation for the AB test.
Possible values:
**true** - Zia dynamically adjusts traffic allocation based on performance.
**false** - Traffic is allocated according to the manually configured split.
    - `base_form` (object `BaseFormNestedPost`) **REQ** — Represents the base webform configuration to include when creating an AB test, including the form ID and traffic allocation.
      schema: `BaseFormNestedPost`
      - `id` (string) [maxLen=255] — Specify the unique identifier of the base webform to include in the AB test.
      - `traffic` (integer/int32) — Specify the percentage of visitor traffic to allocate to the base webform.
    - `notify` (boolean) — Specify whether to enable notifications for this AB test.
Possible values:
**true** - Notifications are sent when the test reaches a significant milestone.
**false** - No notifications are sent.
    - `traffic_diversion` (null) — Specify the traffic diversion configuration for the AB test, if applicable. Set to null when no traffic diversion is required.
    - `variant_form` (array of object `VariantFormNestedPost`) [maxItems=2] **REQ** — Specify the list of variant webforms to include in the AB test, each with its own traffic allocation and appearance settings.
      schema: `VariantFormNestedPost`
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
      - `button_attributes` (array of object `ButtonAttributesNested`) [maxItems=2] — Specify the list of button configurations for the variant webform, including submit and reset buttons.
        schema: `ButtonAttributesNested`
        - `color` (string) [maxLen=255] — Represents the color of the button, specified as a hex code or color name.
        - `name` (string) **REQ** [maxLen=255] — Represents the label text displayed on the button.
      - `form_fields` (array of object `FormFieldsNested`) [maxItems=5] — Specify the list of form fields to include in the variant webform.
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
      - `traffic` (integer/int32) — Specify the percentage of visitor traffic to allocate to this variant webform.
    - `traffic` (integer/int32) — Specify the total percentage of visitor traffic to allocate to this AB test.
    - `module` (object `ModuleNested`) **REQ** — Represents the CRM module associated with an AB test, identified by its API name and ID.
      schema: `ModuleNested`
      - `api_name` (string) [maxLen=50] — Represents the API name of the CRM module associated with the AB test.
      - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the CRM module associated with the AB test.
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
    - `name` (string) **REQ** [maxLen=255] — Specify the name of the AB test configuration.
    - `winner_configuration` (object `WinnerConfigurationNested`) — Represents the winner declaration configuration for an AB test, including automatic announcement settings and the conversion percentage difference threshold.
      schema: `WinnerConfigurationNested`
      - `announce_automatically` (boolean) [enum=[True, False]] — Indicates whether the winning form is announced automatically when the conversion percentage difference threshold is met.
Possible values:
**true** - The winner is announced automatically.
**false** - The winner must be announced manually.
      - `conversion_percentage_difference` (integer/int32) — Represents the minimum conversion rate percentage difference required to automatically declare a winner. Required when **announce_automatically** is **true**.
    - `status` (string) **REQ** [maxLen=255, enum=['drafted', 'running', 'scheduled']] — Specify the initial status of the AB test.
Possible values:
**drafted** - Create the test without starting it.
**running** - Start the test immediately.
**scheduled** - Schedule the test to start at a future date.

**Responses:**

- **201**: Returns the unique ID of the newly created AB testing configuration. — Schema: `PostabtestingResponse201` [application/json]
    > Successful response returned after creating a new AB test configuration.
    schema: `PostabtestingResponse201`
    - `AB_testing` (array of object `AbTestingNested201`) [maxItems=1] — Represents the list of results for the AB test creation operation.
      schema: `AbTestingNested201`
      - `code` (string) [maxLen=255] — Represents the status code of the AB test operation result.
Possible values:
**SUCCESS** - The operation completed successfully.
      - `details` (object `DetailsNested`) — Represents the details returned in a successful AB test operation response, including the ID of the affected record.
        schema: `DetailsNested`
        - `id` (string) [maxLen=19] — Represents the unique identifier of the AB test record affected by the operation.
      - `message` (string) [maxLen=255] — Represents the message describing the result of the AB test operation.
      - `status` (string) [maxLen=255] — Represents the status of the AB test operation.
Possible values:
**success** - The AB test operation completed successfully.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request contains invalid data for the AB testing configuration.
**Resolution:** The request body must contain a valid AB_testing object. Ensure all required fields are provided with the correct data types and values. [application/json]
    > Represents one of the possible error response schemas returned when the AB testing configuration contains invalid data.
    anyOf:
      - `ErrorResponseCore1311222188` — Error response returned when a field in the request body contains invalid data.
        - `AB_testing` (array of object) [maxItems=25] **REQ** — Represents the list of AB testing error objects returned for invalid input.
          anyOf:
            - `AbtestingLimitExceeded` — Error response returned when the maximum number of allowed AB tests has been exceeded.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code returned when the AB testing limit has been exceeded.
Possible values:
**LIMIT_EXCEEDED** - The maximum number of allowed AB tests has been reached.
              - `details` (object) **REQ** — Represents the details of the AB testing limit exceeded error, including the limit count and type.
                - `limit` (integer/int32) — Represents the maximum number of AB tests allowed.
                - `type` (string) [maxLen=100] — Represents the type of limit that was exceeded.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that the AB testing limit has been exceeded.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because the AB testing limit was exceeded.
            - `ABTestNamePatternNotMatched` — Error response returned when the AB test name does not match the required pattern.
              - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code returned when the input value does not match the expected pattern.
Possible values:
**PATTERN_NOT_MATCHED** - The value provided for the field does not satisfy the required format.
              - `details` (object) **REQ** — Represents the details of the pattern mismatch validation error, including the name of the field and its JSON path.
                - `api_name` (string) [enum=['name']] — Represents the API name of the field for which the pattern validation failed.
                - `json_path` (string) [enum=['$.AB_testing[0].name']] — Represents the JSON path of the field in the request body for which the pattern validation failed.
              - `message` (string) **REQ** [enum=['Please check whether the input values are correct']] — Represents the error message indicating that the input value does not match the expected pattern.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a validation error.
            - `InvalidDataInTrafficDetails` — Error response returned when the traffic allocation value in the request is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the traffic allocation data in the request is invalid.
Possible values:
**INVALID_DATA** - The traffic value provided is not valid.
              - `details` (object) **REQ** — Represents the details of the traffic data validation error, including the field name and JSON path.
                - `api_name` (string) [enum=['traffic']] — Represents the API name of the traffic field that contains the invalid value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the traffic field in the request body that contains the invalid value.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that the traffic data is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to invalid traffic data.
            - `ErrorResponseCoreInvalidDataWidth` — Error response returned when the width value is not among the supported options.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the width value is not among the supported options.
Possible values:
**INVALID_DATA** - The width value is not a supported option.
              - `details` (object) **REQ** — Represents the details of the width validation error, including the field name, JSON path, and list of supported width values.
                - `api_name` (string) [maxLen=100] — Represents the API name of the field that contains the unsupported width value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the unsupported width value.
                - `supported_values` (array of integer/int32) [maxItems=5] — Represents the list of valid integer values accepted for the width field.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that the width value is not among the supported options.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because the width value is not supported.
            - `ErrorResponseCoreInvalidDataSupportedString` — Error response returned when a field value is not among the supported string options.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a field value is not among the supported string values.
Possible values:
**INVALID_DATA** - The field value is not a supported option.
              - `details` (object) **REQ** — Represents the details of the supported values validation error, including the field name, JSON path, and list of supported string values.
                - `api_name` (string) [maxLen=100] — Represents the API name of the field that contains the unsupported value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the unsupported value.
                - `supported_values` (array of string) [maxItems=5] — Represents the list of valid string values accepted by the field.
                  items: [maxLen=25]
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that the field value is not among the supported options.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because the field value is not supported.
            - `DuplicateDataABTestingNameError` — Error response returned when an AB test with the same name already exists in the module.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code returned when an AB test with the same name already exists in the module.
Possible values:
**DUPLICATE_DATA** - An AB test with the specified name already exists.
              - `details` (object) **REQ** — Represents the details of the duplicate data error, including the field name and JSON path of the conflicting value.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the duplicate value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the duplicate value.
              - `message` (string) **REQ** [enum=['ABTesting with the same name already exists in this module']] — Represents the error message indicating that an AB test with the same name already exists in this module.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a duplicate AB test name.
            - `ErrorResponseCoreInvalidData` — Error response returned when one or more fields in the request contain invalid data.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the request contains invalid data.
Possible values:
**INVALID_DATA** - The value provided for one or more fields is not valid.
              - `details` (object) **REQ** — Represents the details of the invalid data error, including the field name and its JSON path.
                - `api_name` (string) [maxLen=100] — Represents the API name of the field that contains invalid data.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains invalid data.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that the request data is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to invalid data.
            - `ErrorResponseCore210190878` — Error response returned when the number of months exceeds the allowed maximum of three.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the number of months specified exceeds the allowed maximum.
Possible values:
**INVALID_DATA** - The months value is greater than the allowed maximum of three.
              - `details` (object) **REQ** — Represents the details of the months limit validation error, including the field name and JSON path.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the out-of-range months value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the out-of-range months value.
              - `message` (string) **REQ** [enum=['months should be less than or equal to 3']] — Represents the error message indicating that the months value exceeds the allowed maximum of three.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because the months value exceeds the allowed maximum.
            - `ErrorResponseCore278210242` — Error response returned when the number of weeks exceeds the allowed maximum of 12.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the number of weeks specified exceeds the allowed maximum.
Possible values:
**INVALID_DATA** - The weeks value is greater than the allowed maximum of 12.
              - `details` (object) **REQ** — Represents the details of the weeks limit validation error, including the field name and JSON path.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the out-of-range weeks value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the out-of-range weeks value.
              - `message` (string) **REQ** [enum=['weeks should be less than or equal to 12']] — Represents the error message indicating that the weeks value exceeds the allowed maximum of 12.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because the weeks value exceeds the allowed maximum.
            - `ErrorResponseCore554143170` — Error response returned when the number of days exceeds the allowed maximum of 90.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the number of days specified exceeds the allowed maximum.
Possible values:
**INVALID_DATA** - The days value is greater than the allowed maximum of 90.
              - `details` (object) **REQ** — Represents the details of the days limit validation error, including the field name and JSON path.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the out-of-range days value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the out-of-range days value.
              - `message` (string) **REQ** [enum=['days should be less than or equal to 90']] — Represents the error message indicating that the days value exceeds the allowed maximum of 90.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because the days value exceeds the allowed maximum.
            - `ErrorResponseCore157494901` — Error response returned when the number of visits exceeds the allowed maximum of 100000.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the number of visits specified exceeds the allowed maximum.
Possible values:
**INVALID_DATA** - The visits value is greater than the allowed maximum of 100000.
              - `details` (object) **REQ** — Represents the details of the visits limit validation error, including the field name and JSON path.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the out-of-range visits value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the out-of-range visits value.
              - `message` (string) **REQ** [enum=['visits should be less than or equal to 100000']] — Represents the error message indicating that the visits value exceeds the allowed maximum of 100000.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because the visits value exceeds the allowed maximum.
            - `ErrorResponseCore1311222188` — Error response returned when a field in the request body contains invalid data.
            - `CannotCreateABTestDueToStatus` — Error response returned when a new AB test cannot be created because an existing test has not been launched.
              - `code` (string) **REQ** [enum=['CANNOT_CREATE']] — Represents the error code returned when a new AB test cannot be created because an existing test is not in the launched state.
Possible values:
**CANNOT_CREATE** - A new AB test cannot be created while an existing test has not been launched.
              - `details` (object) **REQ** — Represents the details of the error, including the name, ID, and current status of the existing AB test that is blocking creation.
                - `name` (string) [maxLen=255] — Represents the name of the existing AB test that is blocking creation.
                - `id` (string) [maxLen=19] — Represents the unique identifier of the existing AB test that is blocking creation.
                - `status` (string) [maxLen=255] — Represents the current status of the existing AB test that is blocking creation.
              - `message` (string) **REQ** [enum=['previously created A/B Testing should be in launched state']] — Represents the error message indicating that the previously created AB test must be in the launched state before creating a new one.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because an existing AB test has not been launched.
            - `ErrorResponseCore1620103746` — Error response returned when a required field is missing from the request body.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code returned when a required field is missing from the request body.
Possible values:
**MANDATORY_NOT_FOUND** - A required field is absent from the request.
              - `details` (object) **REQ** — Represents the details of the missing required field error, including the field name and JSON path.
                - `api_name` (string) [maxLen=255] — Represents the API name of the required field that is missing from the request.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the missing required field in the request body.
              - `message` (string) **REQ** [enum=['Required field is missing', 'required field not found']] — Represents the error message indicating that a required field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a missing required field.
            - `ErrorResponseCore654482121` — Error response returned when a field value does not match the expected data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the data type of a field value is invalid.
Possible values:
**INVALID_DATA** - The field value does not match the expected data type.
              - `details` (object) **REQ** — Represents the details of the data type validation error, including the field name, expected data type, and JSON path.
                - `expected_data_type` (string) [maxLen=255] — Represents the expected data type for the field.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the invalid data type.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the invalid data type.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message indicating that the field value has an invalid data type.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a data type validation failure.
            - `ErrorResponseCore121471384` — Error response returned when a field value exceeds the maximum allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the input data is invalid.
Possible values:
**INVALID_DATA** - The value provided for the field does not meet the required constraints.
              - `details` (object) **REQ** — Represents the details of the invalid data error, including the field name, JSON path, and maximum allowed length.
                - `maximum_length` (integer/int32) — Represents the maximum allowed length for the field value.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that contains the invalid value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the invalid value.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message indicating that the field data is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to invalid data.
            - `ErrorResponseCore1426090916` — Error response returned when a field value is shorter than the minimum allowed length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when the input data does not meet the minimum length requirement.
Possible values:
**INVALID_DATA** - The value provided for the field is shorter than the minimum allowed length.
              - `details` (object) **REQ** — Represents the details of the minimum length validation error, including the field name, JSON path, and minimum required length.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that failed the minimum length validation.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that failed the minimum length validation.
                - `minimum_length` (integer/int32) — Represents the minimum required length for the field value.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message indicating that the field data does not meet the minimum length requirement.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a minimum length validation failure.
            - `ErrorResponseCore686109240` — Error response returned when one or more expected fields are missing from the request body.
              - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Represents the error code returned when one or more expected fields are missing from the request body.
Possible values:
**EXPECTED_FIELD_MISSING** - A required set of alternative fields is absent from the request.
              - `details` (object) **REQ** — Represents the details of the expected field missing error, including the list of fields that must be present.
                - `expected_fields` (array of object) [maxItems=25] — Represents the list of fields, at least one of which must be present in the request.
                  - `api_name` (string) [maxLen=255] — Represents the API name of the expected field.
                  - `json_path` (string) [maxLen=1000] — Represents the JSON path of the expected field in the request body.
              - `message` (string) **REQ** [enum=['One of the required fields is missing']] — Represents the error message indicating that one or more required fields are missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a missing expected field.
            - `ErrorResponseCore241660575` — Error response returned when a field that is required by another field is missing from the request body.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code returned when a field that is required by another field is missing from the request body.
Possible values:
**DEPENDENT_FIELD_MISSING** - A dependent field is absent from the request.
              - `details` (object) **REQ** — Represents the details of the dependent field missing error, including the missing field name, its JSON path, and the field it depends on.
                - `dependee` (object) — Represents the field that requires the missing dependent field to be present.
                  - `api_name` (string) [maxLen=255] — Represents the API name of the field that triggers the dependency requirement.
                  - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field that triggers the dependency requirement.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field that is missing from the request.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the missing dependent field in the request body.
              - `message` (string) **REQ** [enum=['Dependent field is missing']] — Represents the error message indicating that a dependent field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a missing dependent field.
            - `ErrorResponseCoreInvalidDataBoolean` — Error response returned when a field value does not match the supported Boolean values.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when a field value does not match the supported Boolean values.
Possible values:
**INVALID_DATA** - The field value is not a valid Boolean.
              - `details` (object) **REQ** — Represents the details of the Boolean validation error, including the field name, JSON path, and supported Boolean values.
                - `api_name` (string) [maxLen=100] — Represents the API name of the field that contains the invalid Boolean value.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field in the request body that contains the invalid Boolean value.
                - `supported_values` (array of boolean) [maxItems=2] — Represents the list of supported Boolean values for the field.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that the field value is not a valid Boolean.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to a Boolean validation failure.
            - `ErrorResponseOperationNotAllowed` — Error response returned when the requested operation is not allowed in the current state.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code returned when the requested operation is not allowed.
Possible values:
**NOT_ALLOWED** - The operation cannot be performed in the current state.
              - `details` (object) **REQ** — Represents the details of the operation not allowed error, including the API name, ID, and JSON path of the affected resource.
                - `api_name` (string) [maxLen=255] — Represents the API name of the field or resource for which the operation is not allowed.
                - `id` (string) [maxLen=19] — Represents the unique identifier of the resource for which the operation is not allowed.
                - `json_path` (string) [maxLen=1000] — Represents the JSON path of the field or resource in the request body for which the operation is not allowed.
              - `message` (string) **REQ** [maxLen=1000] — Represents the error message indicating that the requested operation is not allowed.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed because the operation is not allowed.
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

- **403**: Permission denied to create the AB testing configuration.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `PermissionDeniedErrorResponse` [application/json]
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

**Scopes:** ZohoCRM.settings.abtest.CREATE
