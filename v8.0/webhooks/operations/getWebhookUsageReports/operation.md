# GET /settings/automation/webhooks/actions/usage_reports
**Operation:** `getWebhookUsageReports` — Get webhook action usage reports

> To retrieve usage statistics for webhook actions executed in your Zoho CRM organization. Specify the **group_by** parameter to control the granularity of results; optionally filter by automation feature type and date range.


**Parameters:**
- `group_by` (query, string, required) [maxLen=100, enum=['date', 'date,resource', 'date,resource,type']]: Specify the grouping criteria for usage data. Must include date.
Possible values:
**date** - Returns daily totals; the resource object is omitted from each row.
**date,resource** - Returns per-action rows including resource.id and resource.name.
**date,resource,type** - Returns per-action rows grouped by resource and type.
- `type` (query, string, optional) [maxLen=50, enum=[8 values]]: Specify the automation feature type to filter usage data. When omitted, usage across all supported feature types is returned.
Possible values:
**workflow_rules** - Workflow Rules.
**approval_process** - Approval Process.
**blueprint** - Blueprint.
**orchestrations** - Orchestrations.
**wizards** - Wizards.
**modules** - Modules.
**webhooks** - Webhooks.
**kiosks** - Kiosks.
- `from` (query, string/date, optional) [maxLen=10]: Specify the start date (inclusive) for the query window in YYYY-MM-DD format, evaluated in the organization's time zone. For webhook_failures, defaults to 30 days before **to**; earlier dates are clamped to that 30-day window. For usage_reports, defaults to 30 days before **to**. Future dates return 400 INVALID_DATA.
- `to` (query, string/date, optional) [maxLen=10]: Specify the end date (inclusive) for the query window in YYYY-MM-DD format, evaluated in the organization's time zone. Defaults to the current date at 23:59:59 when omitted. Must be on or after the **from** date. Future dates are rejected.
- `page` (query, integer/int32, optional) [min=1]: Specify the page number for paginated results. Defaults to 1 when omitted. Use together with per_page to navigate large result sets.
- `per_page` (query, integer/int32, optional) [min=1, max=200]: Specify the number of records to return per page. Default and maximum is **200**.
- `sort_order` (query, string, optional) [enum=['asc', 'desc']]: Specify the sort direction for list results. Defaults to desc when omitted.
Possible values:
**asc** - Ascending order.
**desc** - Descending order.
- `include_inner_details` (query, string, optional) [maxLen=50, enum=['resource.layout_id']]: Specify to request additional nested fields within usage report resource objects. Currently, only resource.layout_id is recognized; it adds layout_id inside the resource object when available, primarily for wizard usage rows. Other values are silently ignored.

**Responses:**

- **200**: Returns the webhook action usage report for the requested date range. Each item in the **data_usage** array represents usage grouped by the criteria specified in the **group_by** parameter. When **group_by** includes **resource**, each item represents one webhook action per day; when **group_by** is **date** only, each item represents the daily total across all webhook actions.
 — Schema: `AutomationUsageReportResponse` [application/json]
    > Represents a successful response from an automation usage report endpoint. Contains an array of daily usage data points alongside pagination metadata that includes the edition-specific daily execution cap. When no usage exists for the queried period, the endpoint returns an empty data array rather than null, and the response resolves with HTTP 200.

    schema: `AutomationUsageReportResponse`
    - `data_usage` (array of object `AutomationUsageDataEntry`) [maxItems=200] — Contains the collection of usage data points for the queried period. Each entry represents the execution count for a specific automation action on a given date. Returns an empty array when no usage exists for the queried period.
      schema: `AutomationUsageDataEntry`
      - `date` (string/date) [maxLen=10] — Represents the date of this usage data point in YYYY-MM-DD format. All dates are evaluated in the organization's time zone.
      - `resource` (object `AutomationUsageResource`) — Reference to the specific automation action (email notification or webhook) that generated the usage count. Only present when group_by includes 'resource'.
        schema: `AutomationUsageResource`
        - `id` (string) [maxLen=20] — Represents the unique identifier of the automation action, such as an email notification ID or a webhook ID.
        - `name` (string) [maxLen=255] — Represents the display name of the automation action. Falls back to the name recorded in the automation audit log when the action has been deleted.

        - `layout_id` (string) [maxLen=20] — Represents the identifier of the wizard layout associated with the automation action. Present only when the include_inner_details query parameter is set to resource.layout_id and the action is linked to a wizard layout.
      - `count` (integer/int32) [min=0] — Represents the number of times the automation action was executed on this date. When the group_by parameter is set to 'date' only, this value reflects the total across all actions.
      - `type` (string) [maxLen=50] — Represents the automation feature type associated with the reported executions. Values correspond to the filter types supported by the type query parameter, such as workflow_rules, approval_process, Blueprint, email_notifications, webhooks, and kiosks.

    - `info` (object `AutomationUsagePaginationInfo`) — Pagination metadata including the edition-specific daily execution cap.
      schema: `AutomationUsagePaginationInfo`
      - `per_page` (integer/int32) [min=1, max=200] — Represents the number of records returned in each page of the result set.
      - `count` (integer/int32) [min=0] — Represents the number of records included in the current page of results.
      - `page` (integer/int32) [min=1] — Represents the one-based index of the current page within the paginated result set.
      - `more_records` (boolean) — Indicates whether additional pages of results are available beyond the current page.
Possible values:
true - More records exist beyond the current page.
false - The current page contains the last records.
      - `max_limit` (integer/int32) [min=0] — Represents the edition-specific daily execution cap for the automation action type. For email notifications, this reflects the WORKFLOWALERT day limit; for webhooks, it reflects the WFWEBHOOK day limit. Lower-tier editions carry smaller caps.

- **400**: One or more query parameters are invalid.

**Resolution:** The **group_by** parameter must be present and must include **date**. The **type** value must match a supported automation feature type. Date parameters must be in YYYY-MM-DD format and must not be in the future.
 [application/json]
    > Represents the error response returned when one or more query parameters fail validation. Applies when **group_by** is missing or does not include **date**, when **type** has an unsupported value, when a date parameter is in the future, or when pagination parameters are invalid.

    oneOf:
      - `AutomationUsageRequiredParamMissingError` — Represents the error structure returned when the group_by query parameter is omitted from the request. All automation usage report endpoints require group_by to be present and to include date as a mandatory grouping dimension.

        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Indicates the error classification for a missing required parameter.
Possible values:
REQUIRED_PARAM_MISSING - A mandatory query parameter was omitted from the request.
        - `details` (object) **REQ** — Contains details about the missing request parameter that caused the error.

          - `param_name` (string) [enum=['group_by']] — Indicates the name of the required parameter that was absent from the request.
Possible values:
group_by - The group_by parameter was not included in the request.
        - `message` (string) **REQ** [maxLen=255] — Represents a descriptive message explaining the error that caused the request to fail.

        - `status` (string) **REQ** [enum=['error']] — Represents the outcome classification of the response.
Possible values:
error - The request was not processed due to a missing required parameter.

      - `AutomationUsageInvalidDataError` — Represents the error envelope returned when an invalid value is supplied for a usage report query parameter. The details object identifies which parameter is invalid. Common causes include an unsupported type filter value, an invalid group_by combination, a malformed date, an invalid sort_order, or a non-numeric page or per_page value.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the invalid-data condition.
Possible values:
INVALID_DATA - The value supplied for the identified query parameter is not valid.
        - `details` (object) **REQ** — Contains details about the query parameter that failed validation.

          - `param_name` (string) [maxLen=50] — Represents the name of the query parameter that carried the invalid value, such as type, group_by, date, sort_order, page, or per_page.
        - `message` (string) **REQ** [maxLen=255] — Represents a descriptive message explaining the error that caused the request to fail.

        - `status` (string) **REQ** [enum=['error']] — Represents the outcome classification of the response.
Possible values:
error - The request was not processed due to invalid input.


- **403**: Permission denied to retrieve webhook action usage reports.

**Resolution:** The CRM administrator must grant the Manage Automation Actions permission to the user's profile.
 — Schema: `AutomationUsageNoPermissionError` [application/json]
    > Represents the error structure returned when the authenticated user lacks the required Manage Automation Actions privilege, or when the requested feature — email notifications or webhooks — is not available in the organization's current edition.

    schema: `AutomationUsageNoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the permission-denied condition.
Possible values:
NO_PERMISSION - The user lacks the required privilege or the feature is unavailable in the current edition.
    - `details` (object) **REQ** — Contains details about the missing permission or unavailable feature that caused the error.
      - `permissions` (array of string) [maxItems=5] — Contains the list of required permissions that the caller lacks and that prevented the request from succeeding.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Represents a descriptive message explaining the error that caused the request to fail.

    - `status` (string) **REQ** [enum=['error']] — Represents the outcome classification of the response.
Possible values:
error - The request was denied due to insufficient permission.


**Scopes:** ZohoCRM.settings.automation_actions.READ
