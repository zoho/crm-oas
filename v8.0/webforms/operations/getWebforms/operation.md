# GET /settings/webforms
**Operation:** `getWebforms` — Get webforms
> To retrieve all webforms from your Zoho CRM organization.

**Parameters:**
- `module` (query, string, optional) [enum=['Leads']]: Specify the module API name to filter webforms by the target CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `include_inner_details` (query, string, optional) [enum=['user_type.active']]: Specify whether to include inner details such as portal information in the webforms response. Possible values: true - Include inner details. false - Exclude inner details.
- `feature_name` (query, string, optional) [enum=['Web_Forms | Orchestration']]: Specify the feature name to check whether the required permission is granted for the feature.
- `active` (query, string, optional) [enum=['true', 'false']]: Specify the active status of the webforms to filter. Possible values: true - Return only active webforms. false - Return only inactive webforms.
- `layout_id` (query, number, optional) [enum=[12345678909876]]: Specify the layout ID to filter the webforms list by layout. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.
- `filters` (query, string, optional) [enum=[43 values]]: Specify the filter criteria for the webforms list. The value must be a JSON object with group and group_operator fields.

**Schemas:**
`ErrorResponse`:
  > Represents a generic API error response containing an error code, status, message, and details.
  - `code` (string) **REQ** [enum=[18 values]] — Represents the error code that identifies the type of error returned by the API.
  - `details` (object) **REQ** — Represents additional details providing context about the error, such as the invalid field name or parameter.
  - `message` (string) **REQ** [maxLen=2000] — Represents the error message describing the reason for the failure.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: error - The request was not successful.

**Responses:**

- **200**: Returns a paginated list of webforms configured in the CRM organization. — Schema: `GetWebformsSuccessResponse` [application/json]
    > Represents the response for listing all webforms, including the webforms array and pagination information.
    schema: `GetWebformsSuccessResponse`
    - `webforms` (array of object `WebformsNested`) [maxItems=100] **REQ** — Contains the list of webform objects returned in the response.
      schema: `WebformsNested`
      - `layout` (object `LayoutNested`) **REQ** — Represents the layout associated with the webform, including its identifier, name, and display label.
        schema: `LayoutNested`
        - `display_label` (string) [maxLen=255] — Represents the display label of the layout associated with the webform.
        - `name` (string) [maxLen=255] — Represents the name of the layout associated with the webform.
        - `id` (string/int64) [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents the unique identifier of the layout associated with the webform.
      - `created_time` (string) **REQ** [maxLen=255] — Represents the timestamp of webform creation.
      - `analytics_data` (object `AnalyticsDataNested`) **REQ** — Represents the analytics configuration for a webform, including whether analytics tracking is enabled and the time it was enabled.
        schema: `AnalyticsDataNested`
        - `analytics_enabled` (boolean) **REQ** — Indicates whether analytics tracking is enabled for the webform. Possible values: true - Analytics tracking is active for the webform. false - Analytics tracking is inactive for the webform.
        - `analytics_enabled_time` (string) **REQ** [maxLen=255] — Represents the date and time at which analytics tracking was enabled for the webform.
      - `module` (object `ModuleNested`) **REQ** — Represents the CRM module associated with the webform, including its API name and identifier.
        schema: `ModuleNested`
        - `api_name` (string) **REQ** [maxLen=50] — Represents the display name of the user who created the webform.
        - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the user who created the webform.
      - `suggestion` (null) — Represents the AI-generated suggestion for improving the webform's performance.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the webform.
      - `type` (string) [maxLen=255] — Represents the type of the form. Possible values: webform - A standard webform. portalform - A portal form for registered portal users.
      - `active` (boolean) **REQ** — Indicates whether the webform is active. Possible values: true - The webform is active. false - The webform is inactive.
      - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the webform.
      - `created_by` (object `CreatedByNested`) **REQ** — Represents the user who created the webform, including their identifier and display name.
        schema: `CreatedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the user who created the webform.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the user who created the webform.
      - `last_submitted_time` (null) **REQ** — Represents the date and time at which the webform received its last submission.
      - `user_type` (object `UserTypeNested`) — portal form details
        schema: `UserTypeNested`
        - `name` (string) [maxLen=50, nullable] — Represents the name of the portal configured for the webform.
        - `active` (boolean) [nullable] — Indicates whether the portal form is active. Possible values: true - The portal form is active. false - The portal form is inactive.
        - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the portal configured for the webform.
    - `info` (object `InfoNested`) — Represents the pagination metadata for a list API response, including page number, count, and sort information.
      schema: `InfoNested`
      - `per_page` (integer/int32) **REQ** — Represents the maximum number of webforms returned per page in the response.
      - `count` (integer/int32) **REQ** — Represents the number of webforms returned in the current page of the response.
      - `page` (integer/int32) **REQ** — Represents the current page number of the paginated webforms response.
      - `sort_by` (string) **REQ** [maxLen=255] — Represents the field by which the webforms are sorted in the response.
      - `sort_order` (string) **REQ** [maxLen=255] — Represents the sort order applied to the webforms in the response.
      - `more_records` (boolean) **REQ** — Indicates whether additional webforms are available beyond the current page. Possible values: true - More records are available. false - No more records are available.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: One or more request parameters contain invalid or unsupported values.
**Resolution:** The top-level query parameters must be valid — including module, layout_id, and active. When using the filters parameter, the sub-fields group, group_operator, and comparator must be correctly structured and present. [application/json]
    > Contains the error response returned when the request parameters for listing webforms are invalid, such as when the filters parameter is not provided as a JSON object, the group field within filters is not a JSON array, or required filter fields are missing.
    oneOf:
      - `WebformsErrorResponse1` — Represents the top-level error response wrapper returned when one or more webform operations fail, containing per-webform error details.
        - `webforms` (array of object `ErrorResponse`) [maxItems=25] **REQ** — Contains the list of per-webform error result objects in the wrapped error response.
      - `ErrorResponse` — Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied for accessing webforms.
**Resolution:** The CRM administrator must grant the required permission to the user's profile. — Schema: `ErrorResponse` [application/json]
    > Represents a generic API error response containing an error code, status, message, and details.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.webforms.READ
