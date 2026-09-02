# GET /settings/automation/webhook_failures
**Operation:** `getWebhookFailures` — Get webhook execution failure records

> To retrieve detailed information about webhook execution failures in your Zoho CRM organization.

Optionally filter results by module, webhook ID, and date range. If the **from** and **to** parameters are not specified, the API returns webhook failures from the last 30 days by default. The maximum allowed span between **from** and **to** is 90 days.


**Parameters:**
- `webhook_id` (query, string, optional) [maxLen=20]: Specify the unique identifier of the webhook whose failure records to retrieve. Refer to the [Get Webhooks](webhooks.yaml#$.paths./settings/automation/webhooks.get) resource for valid values. When omitted, failure records for all webhooks are returned.
- `module` (query, string, optional) [maxLen=100]: Specify the API name of the parent CRM module to filter webhooks. When omitted, webhooks across all modules are returned. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `from` (query, string/date, optional) [maxLen=10]: Specify the start date (inclusive) for the query window in YYYY-MM-DD format, evaluated in the organization's time zone. For webhook_failures, defaults to 30 days before **to**; earlier dates are clamped to that 30-day window. For usage_reports, defaults to 30 days before **to**. Future dates return 400 INVALID_DATA.
- `to` (query, string/date, optional) [maxLen=10]: Specify the end date (inclusive) for the query window in YYYY-MM-DD format, evaluated in the organization's time zone. Defaults to the current date at 23:59:59 when omitted. Must be on or after the **from** date. Future dates are rejected.
- `page` (query, integer/int32, optional) [min=1]: Specify the page number for paginated results. Defaults to 1 when omitted. Use together with per_page to navigate large result sets.
- `per_page` (query, integer/int32, optional) [min=1, max=200]: Specify the number of records to return per page. Default and maximum is **200**.

**Responses:**

- **200**: Returns a paginated list of webhook execution failure records matching the specified filters. Each item contains the failure time, failure reason, the webhook reference, the triggering workflow rule, and the CRM record that triggered the failure.
 — Schema: `WebhookFailuresResponse` [application/json]
    > Represents the paginated response containing webhook execution failure records. Filter by webhook_id, module API name, and date range using query parameters.
    schema: `WebhookFailuresResponse`
    - `webhook_failures` (array of object `WebhookFailureDetail`) [maxItems=200] — Represents the list of webhook execution failure detail objects.
      schema: `WebhookFailureDetail`
      - `webhook` (object `WebhookReference`) — Reference to the webhook that failed (id and name).
        schema: `WebhookReference`
        - `name` (string) [maxLen=255] — Represents the display name of the webhook.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the webhook.
      - `entity_details` (object `FailureEntityDetails`) — Details of the CRM record that triggered the failed webhook execution.
        schema: `FailureEntityDetails`
        - `module` (object `AutomationModuleDetailsResponse`) — API name of the CRM module the triggering record belongs to.
          schema: `AutomationModuleDetailsResponse`
          - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module (for example, Leads, Contacts, Deals).
          - `id` (string) **REQ** [maxLen=255] — Represents the unique identifier of the CRM module. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
        - `name` (string) [maxLen=255] — Represents the display name of the CRM record that triggered the webhook execution failure.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the CRM record that triggered the webhook execution failure.
      - `failure_time` (string) [maxLen=255] — Represents the ISO 8601 timestamp of when the webhook execution failed.
      - `failure_reason` (string) [maxLen=255] — Represents the reason for the webhook execution failure, such as page_notfound.
      - `id` (string) [maxLen=255] — Represents the unique identifier of the failure record.
      - `workflow_rule` (object `WorkflowRuleReference`) — Reference to the workflow rule that triggered the webhook.
        schema: `WorkflowRuleReference`
        - `name` (string) [maxLen=255] — Represents the display name of the workflow rule.
        - `id` (string) [maxLen=255] — Represents the unique identifier of the workflow rule.
    - `info` (object `PaginationInfoResponse`) — Pagination metadata for navigating failure records.
      schema: `PaginationInfoResponse`
      - `max_limit` (integer/int32) — Represents the maximum number of records allowed per page for this resource.
      - `per_page` (integer/int32) — Represents the number of records returned per page in the paginated response.
      - `count` (integer/int32) — Represents the total number of webhooks returned in the current page.
      - `page` (integer/int32) — Represents the current page number in the paginated response.
      - `more_records` (boolean) — Indicates whether additional pages of results are available.
Possible values:
**true** - More records exist beyond the current page.
**false** - The current page contains the last records.

- **204**: No webhook failure records match the specified filter criteria. Returned when no failures exist for the given module, webhook ID, or date range combination.


- **400**: One or more query parameters are invalid.

**Resolution:** The module API name must be valid. The **webhook_id** must be numeric. The **from** and **to** dates must be in YYYY-MM-DD format and must not be in the future.
 [application/json]
    > Represents the error response returned when one or more query parameters in the request are invalid. The response body conforms to one of three error variants: an invalid module, an invalid webhook action ID, or an invalid date range.

    oneOf:
      - `InvalidModuleErrorResponse` — Represents the error returned when the module api_name provided in a query parameter does not match an existing CRM module.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for this failure.
Possible values:
**INVALID_MODULE** - The module API name provided in the request is not recognized.
        - `details` (object) **REQ** — Represents the error details containing the name of the parameter with the invalid module.
          - `param_name` (string) [maxLen=255] — Represents the name of the parameter that contains the invalid module API name.
        - `message` (string) **REQ** [enum=['The value provided to the param is Invalid']] — Represents the error message describing the failure.
Possible values:
**The value provided to the param is Invalid** - The module API name does not match any valid CRM module.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
      - `InvalidActionIDErrorResponse` — Represents the error returned when the action ID provided in the request is invalid or does not match an existing webhook.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The webhook action ID provided in the request is not valid.
        - `details` (object) **REQ** — Represents the error details containing the parameter name associated with the invalid action ID.
          - `param_name` (string) [maxLen=255] — Represents the name of the parameter that contains the invalid action ID.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message describing the failure.
Possible values:
**the id given seems to be invalid** - The action ID provided in the request does not match a valid webhook record.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.
      - `InvalidDateRangeErrorResponse` — Represents the error returned when the date range provided in from and to is invalid. For example, when from is after to.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for this failure.
Possible values:
**INVALID_DATA** - The date range provided in the request parameters is not valid.
        - `details` (object) **REQ** — Represents the error details containing information about the invalid date range parameter.
          - `expected_data_type` (string) [maxLen=255] — Represents the expected data type for the date range field.
          - `param_name` (string) [maxLen=255] — Represents the name of the parameter that contains the invalid date range value.
        - `message` (string) **REQ** [enum=['The value provided to the param is Invalid']] — Represents the error message describing the failure.
Possible values:
**The value provided to the param is Invalid** - The date range parameter value does not match the expected format.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

- **403**: Permission denied to retrieve webhook failure logs in this organization.

**Resolution:** The CRM administrator must grant the Manage Workflow permission to the user's profile.
 — Schema: `NoPermissionErrorResponse` [application/json]
    > Represents the error returned when the requesting user does not have the required CRM profile permission to perform the operation.
    schema: `NoPermissionErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The requesting user does not have the required CRM profile permission.
    - `details` (object) **REQ** — Represents the error details containing the list of permissions required for this operation.
      - `permissions` (array of string) [maxItems=25] — Represents the list of CRM profile permissions required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the failure.

Possible values:
**permission denied** - The requesting user lacks the required CRM profile permission for this operation.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

**Scopes:** ZohoCRM.settings.automation_actions.READ
