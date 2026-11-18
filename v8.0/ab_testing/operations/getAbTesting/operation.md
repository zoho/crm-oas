# GET /settings/AB_testing
**Operation:** `getAbTesting` — List Webform A/B Testing configurations

> To retrieve all Webform A/B Testing configurations created in your Zoho CRM organization. You can optionally filter the results by module or by the ID of a base webform.


**Parameters:**
- `module` (query, string, optional) [enum=['Leads']]: Specify the module API name to filter AB test configurations. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID and API name. 
Possible values:
**Leads** - Filter by the Leads module.
- `base_form` (query, number, optional) [enum=[111111000000115000]]: Specify the ID of the base webform to filter AB test configurations. Accepts a single base form ID. Use the [Get Webforms API](webforms.yaml#$.paths./settings/webforms.get) to retrieve the webform ID.

**Schemas:**
`ModuleNested`:
  > Represents the CRM module associated with an AB test, identified by its API name and ID.
  - `api_name` (string) [maxLen=50] — Represents the API name of the CRM module associated with the AB test.
  - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the CRM module associated with the AB test.

**Responses:**

- **200**: Returns a list of Webform A/B Testing configurations for the Zoho CRM organization, with up to 1000 records per response.
 — Schema: `GetAllabtestingResponse200` [application/json]
    > Successful response returned when retrieving all AB test configurations.
    schema: `GetAllabtestingResponse200`
    - `AB_testing` (array of object `AbTestingListNested`) [maxItems=1000] — Represents the list of AB test configurations returned by the request.
      schema: `AbTestingListNested`
      - `dynamic_allocation_by_zia` (boolean) — Indicates whether the traffic allocation between the base form and variant forms is managed dynamically by Zia, the AI assistant.
Possible values:
**true** - Zia dynamically adjusts traffic allocation based on performance.
**false** - Traffic is allocated according to the manually configured split.
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
      - `variant_form` (array of object `VariantFormNestedGetAll`) [maxItems=2] **REQ** — Represents the list of variant webforms included in the AB test, each with its own traffic allocation and performance data.
        schema: `VariantFormNestedGetAll`
        - `winner` (boolean) **REQ** — Indicates whether the variant webform has been declared the winner of the AB test.
Possible values:
**true** - The variant webform is the declared winner.
**false** - The variant webform has not been declared the winner.
        - `old_traffic` (null) — Represents the previous traffic allocation percentage for the variant webform before the most recent update. Returns null when no previous allocation exists.
        - `name` (string) **REQ** [maxLen=255] — Represents the name of the variant webform.
        - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the variant webform.
        - `traffic` (integer/int32) **REQ** — Represents the percentage of visitor traffic allocated to the variant webform.
      - `id` (string) **REQ** [maxLen=19] — Represents the unique identifier of the AB test configuration.
      - `traffic` (integer/int32) **REQ** — Represents the total percentage of visitor traffic allocated to this AB test.
      - `created_time` (string) [maxLen=255] — Represents the creation date and time of the AB test configuration.
      - `complete_restart_info` (null) — Represents information about a complete restart of the AB test, if applicable. Returns null when no restart has occurred.
      - `started_time` (string) [maxLen=255] — Represents the actual date and time when the AB test started running.
      - `module` (object `ModuleNested`) **REQ** — Represents the CRM module associated with an AB test, identified by its API name and ID.
      - `suggestion` (null) — Represents the AI-generated suggestion for the AB test, if available. Returns null when no suggestion is available.
      - `created_by` (object `CreatedByNested`) **REQ** — Represents the CRM user who created the AB test configuration.
        schema: `CreatedByNested`
        - `name` (string) [maxLen=255] — Represents the full name of the user who created the AB test.
        - `id` (string) [maxLen=19] — Represents the unique identifier of the user who created the AB test.
      - `start_time` (string) [maxLen=255] — Represents the scheduled start time of the AB test.
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
      - `winner_configuration` (object `WinnerConfigurationNested`) — Represents the winner declaration configuration for an AB test, including automatic announcement settings and the conversion percentage difference threshold.
        schema: `WinnerConfigurationNested`
        - `announce_automatically` (boolean) [enum=[True, False]] — Indicates whether the winning form is announced automatically when the conversion percentage difference threshold is met.
Possible values:
**true** - The winner is announced automatically.
**false** - The winner must be announced manually.
        - `conversion_percentage_difference` (integer/int32) — Represents the minimum conversion rate percentage difference required to automatically declare a winner. Required when **announce_automatically** is **true**.
      - `status` (string) **REQ** [maxLen=255, enum=['drafted', 'running', 'scheduled', 'paused', 'completed', 'launched']] — Represents the current lifecycle status of the AB test.
Possible values:
**drafted** - The test exists but has not started.
**running** - The test actively distributes traffic.
**scheduled** - The test starts at a future date.
**paused** - The test has stopped temporarily.
**completed** - The test has finished and results are available.
**launched** - The winning form has launched.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Returns no content when no Webform A/B Testing configurations match the specified filter criteria.

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The module name given seems to be invalid, or the base_form parameter value does not match the expected pattern.
**Resolution:** The caller must verify that the module parameter contains a valid CRM module API name and that the base_form parameter value is a valid webform ID.
 [application/json]
    > Represents the error response returned when an invalid module name is provided (INVALID_MODULE) or an input value does not match the expected pattern (PATTERN_NOT_MATCHED).

    anyOf:
      - `ErrorResponseCore1335454202` — Error response returned when the module name in the request is not a valid Zoho CRM module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned when the module name in the request is not valid.
Possible values:
**INVALID_MODULE** - The module name specified in the request is not a valid Zoho CRM module.
        - `details` (object) **REQ** — Represents the details of the invalid module error.
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Represents the error message indicating that the module name is not valid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response.
Possible values:
**error** - The request could not be processed due to an invalid module name.
      - `InvalidBaseFormId` — base_form param value should be base form id. Please give proper id value.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['The given param value is invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to retrieve Webform A/B Testing configurations.
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
