# GET /settings/automation/email_notifications/actions/usage_reports
**Operation:** `getEmailNotificationUsageReports` — Get Email Notification Action Usage Reports
> Retrieves usage statistics for email notification actions executed in your Zoho CRM organization over a specified date range, grouped by date, resource, or type according to the group_by parameter.

**Parameters:**
- `group_by` (query, string, required) [maxLen=100, enum=['date', 'date,resource', 'date,resource,type']]: Specify the grouping criteria for usage report data. The value must include `date`. Two combinations are accepted:
`date` - Returns daily totals; the response omits the resource object, and the count represents the total number of alerts sent that day.
`date,resource` - Returns per-action rows with the resource identifier and name populated; type is an optional addition.
- `type` (query, string, optional) [maxLen=50, enum=[11 values]]: Specify the automation feature type to filter usage data. When omitted, returns usage across all supported feature types.
Possible values:
workflow_rules - Filters usage data for Workflow Rules.
approval_process - Filters usage data for Approval Processes.
blueprint - Filters usage data for Blueprint Processes.
orchestrations - Filters usage data for Orchestrations.
wizards - Filters usage data for Wizards.
modules - Filters usage data for module-level limits.
email_notifications - Filters usage data for email notification actions.
email_templates - Filters usage data for Email Templates.
kiosks - Filters usage data for Kiosks.
cadences - Filters usage data for Cadences.
connected_workflows - Filters usage data for connected workflows.
- `from` (query, string/date, optional) [maxLen=10]: Specify the start date (inclusive) for the date range filter, in YYYY-MM-DD format. The date is evaluated in the organization's time zone. When omitted, defaults to 30 days before the value set for the end date parameter. Future dates return an INVALID_DATA error.
- `to` (query, string/date, optional) [maxLen=10]: Specify the end date (inclusive) for the query range in YYYY-MM-DD format. Evaluated in the organization's time zone. Defaults to the current date at 23:59:59 when omitted. Future dates return a 400 error with the code INVALID_DATA and the message 'provided_time_is_ahead'.
- `page` (query, integer/int32, optional) [min=1, default=1]: Specify the page number to retrieve results from. The first page is page one.
- `per_page` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of records to return per page. The maximum value is 200.
- `sort_order` (query, string, optional) [enum=['desc', 'asc']]: Specify the sort order for the results.
Possible values:
desc - Sorts the results in descending order.
asc - Sorts the results in ascending order.
- `include_inner_details` (query, string, optional) [maxLen=50, enum=['resource.layout_id']]: Specify the additional nested fields to include in usage report resource objects. Currently, only `resource.layout_id` is supported, which adds the layout ID inside the resource object when available, primarily for wizard usage rows. Other values are silently ignored.

**Responses:**

- **200**: Returns the email notification action usage statistics grouped according to the group_by parameter. The data_usage array contains one entry per action per day when group_by includes resource, or one entry per day when group_by is date only. The info object includes pagination details. — Schema: `AutomationUsageReportResponse` [application/json]
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
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: One of the expected parameters is missing or invalid. Resolution: The group_by parameter must be included and must contain date. The type parameter must use a supported value. Date values must not be in the future. [application/json]
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

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to retrieve email notification usage reports. Resolution: The CRM administrator must grant the manage workflow permission to the user's profile. — Schema: `AutomationUsageNoPermissionError` [application/json]
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

  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.READ
