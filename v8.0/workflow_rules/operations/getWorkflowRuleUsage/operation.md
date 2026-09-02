# GET /settings/automation/workflow_rules/{workflowRuleId}/actions/usage
**Operation:** `getWorkflowRuleUsage` — Retrieve Action Usage for a Workflow Rule
> To retrieve the action usage report for a specific workflow rule in your Zoho CRM organization, including trigger count and per-action success, failure, and queue metrics, as well as email engagement statistics. Results are scoped to a configurable date range.

**Parameters:**
- `executed_from` (query, string/date, required): Specifies the start date of the usage data query window in ISO 8601 format (yyyy-MM-dd).
- `executed_till` (query, string/date, required): Specifies the end date of the usage data query window in ISO 8601 format (yyyy-MM-dd).
- `workflowRuleId` (path, string/string, required): Represents the unique 19-digit numeric ID of the workflow rule to target. Obtain valid IDs from the List Workflow Rules endpoint.

**Schemas:**
`EmailEngagementMetricsSchema`:
  > Represents email engagement metrics for an email notification action, including sent, delivered, opened, clicked, bounced, and unsent counts.
  - `bulk_mail` (boolean) **REQ** — Represents number of bulk email messages sent.
  - `unopened` (integer/int32) **REQ** — Represents number of emails not opened by recipients.
  - `sent_percentage` (integer/int32) **REQ** — Represents percentage of emails successfully sent out of total attempted.
  - `opened` (integer/int32) **REQ** — Represents number of emails opened by recipients.
  - `delivered` (integer/int32) **REQ** — Represents number of emails successfully delivered.
  - `unsent` (integer/int32) **REQ** — Represents number of emails that failed to send.
  - `bounced` (integer/int32) **REQ** — Represents number of emails that bounced back.
  - `clicked` (integer/int32) **REQ** — Represents number of emails where recipients clicked a link.
  - `sent` (integer/int32) **REQ** — Represents total number of emails sent.
`InvalidDataNoApiNameAndPathSchema`:
  > Represents the error response returned when a required parameter such as the module API name or field path is missing from the request.
  - `code` (string) **REQ** [enum=[9 values]] — Represents the error code that identifies the specific error condition.
  - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
  - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
  - `details` (object) **REQ** — Represents the error details containing additional context about the failed request.
    - `param_name` (string) [enum=[7 values]] — Represents the **param_name** value from the error detail object.
    - `maximum_length` (integer/int32) — Represents the **maximum_length** value from the error detail object.
    - `id` (string) [maxLen=20] — Represents the **ID** value from the error detail object.
    - `expected_data_type` (string) [maxLen=255] — Represents the **expected_data_type** value from the error detail object.
    - `api_name` (string) [maxLen=255] — Represents the API name of the field or parameter that caused the validation error.
`QueuedActionUsageMetricsSchema`:
  > Represents usage metrics for a single queued workflow action, including success, failure, and queue counts within a queried date range.
  - `queue_count` (integer/int32) **REQ** — Represents the number of executions currently queued and pending for this action.
  - `related_details` (object `EmailEngagementMetricsSchema`) **REQ** — Represents email engagement metrics for an email notification action, including sent, delivered, opened, clicked, bounced, and unsent counts.
  - `name` (string) **REQ** [maxLen=255] — Represents the display name of the workflow rule or its associated queued action as configured in Zoho CRM.
  - `success_count` (integer/int32) **REQ** — Represents the total number of successful executions recorded for this queued action within the queried date range.
  - `failure_count` (integer/int32) **REQ** — Represents the total number of failed executions recorded for this queued action within the queried date range.
  - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the QueuedActionUsageMetrics within the workflow rule.
  - `type` (string) **REQ** [maxLen=255] — Represents the category of queued workflow action. Possible values include **email_notifications**, **field_updates**, **tasks**, **webhooks**, **functions**, **assign_owner**, **add_tags**, **remove_tags**, **create_record**, **add_meeting**, **schedule_call**, and **convert**.
  - `associated_time` (string) **REQ** [maxLen=255] — Represents the ISO 8601 timestamp indicating when this queued action was last associated with or modified on a workflow rule.

**Responses:**

- **200**: Returns detailed execution usage metrics for the specified workflow rule, including trigger counts, conditions breakdowns, and instant and scheduled action usage statistics within the queried date range. — Schema: `WorkflowRuleUsageResponseSchema` [application/json]
    > Represents the response body containing detailed execution usage metrics for one or more workflow rules within a queried date range.
    schema: `WorkflowRuleUsageResponseSchema`
    - `workflow_rules` (array of object) [maxItems=10] **REQ** — Represents the array of workflow rule usage objects.
      - `trigger_count` (integer/int32) **REQ** — Represents the number of times this workflow rule was triggered within the queried date range.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the workflow rule.
      - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the workflow rule.
      - `conditions` (array of object) [maxItems=10] **REQ** — Represents the array of condition objects with usage metrics for the workflow rule.
        oneOf:
          - `WorkflowConditionUsageSummarySchema` — Represents the execution usage summary for a single workflow rule condition, including total execution count and breakdowns for instant and scheduled action groups.
            - `instant_actions` (object `InstantActionsUsageListSchema`) **REQ** — Represents a container for the list of instant action usage detail objects associated with a workflow rule condition.
              schema: `InstantActionsUsageListSchema`
              - `actions` (array of object) [maxItems=5] **REQ** — Represents the array of action usage detail objects for the instant actions configured in this condition.
                oneOf:
                  - `QueuedActionUsageMetricsSchema` — Represents usage metrics for a single queued workflow action, including success, failure, and queue counts within a queried date range.
                  - `ActionUsageMetricsSchema` — Represents usage metrics for a single workflow action, including its identifier, display name, action type, execution success and failure counts within a queried date range, and the timestamp of its last association.
                    - `name` (string) **REQ** [maxLen=255] — Represents the display name of the workflow rule or its associated action as configured in Zoho CRM.
                    - `success_count` (integer/int32) **REQ** — Represents the total number of successful executions recorded for this action within the queried date range.
                    - `failure_count` (integer/int32) **REQ** — Represents the total number of failed executions recorded for this action within the queried date range.
                    - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the workflow action.
                    - `type` (string) **REQ** [maxLen=255] — Represents the category of workflow action executed by the rule.
                    - `associated_time` (string) **REQ** [maxLen=255] — Represents the ISO 8601 timestamp indicating when this action was last associated with or modified on a workflow rule.
            - `scheduled_actions` (array of object `ScheduledActionsUsageGroupSchema`) [maxItems=5] **REQ** — Represents the array of scheduled action groups configured for this condition.
              schema: `ScheduledActionsUsageGroupSchema`
              - `id` (string) **REQ** [maxLen=255] — Represents the unique ID of the ScheduledActionsUsageGroup within the workflow rule.
              - `actions` (array of object `QueuedActionUsageMetricsSchema`) [maxItems=5] **REQ** — Represents the array of action usage detail objects within this scheduled action group.
            - `usage_count` (integer/int32) **REQ** — Represents the total number of times the actions in this condition were executed.
            - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the WorkflowConditionUsageSummary within the workflow rule.
          - `WorkflowConditionUsageWithTaggedInstantActionsSchema` — Represents the usage summary for a workflow rule condition where instant actions include tag-based metrics, along with scheduled action group data.
            - `instant_actions` (object `InstantActionsUsageWithTagsSchema`) **REQ** — Represents a container for instant action usage details that include tag-based metrics, grouped within a workflow rule condition.
              schema: `InstantActionsUsageWithTagsSchema`
              - `actions` (array of object `TaggedActionUsageMetricsSchema`) [maxItems=5] **REQ** — Represents the array of action usage detail objects, including those associated with tags, for the instant actions configured in this condition.
                schema: `TaggedActionUsageMetricsSchema`
                - `name` (string) **REQ** [maxLen=255] — Represents the display name of the workflow rule or its associated tagged action.
                - `success_count` (integer/int32) **REQ** — Represents the total number of successful executions recorded for this tagged action within the queried date range.
                - `tag_id` (string) **REQ** [maxLen=20] — Represents the unique ID of the tag associated with this action.
                - `failure_count` (integer/int32) **REQ** — Represents the total number of failed executions recorded for this tagged action within the queried date range.
                - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the TaggedActionUsageMetrics within the workflow rule.
                - `type` (string) **REQ** [maxLen=255] — Represents the category of tagged workflow action executed by the rule.
                - `associated_time` (string) **REQ** [maxLen=255] — Represents the ISO 8601 timestamp indicating when this tagged action was last associated with or modified on a workflow rule.
            - `scheduled_actions` (array of object) [maxItems=5] **REQ** — Represents the list of scheduled action groups for a workflow rule, each group containing the actions and their execution usage metrics.
              - `id` (string/string) **REQ** — Represents unique identifier for the scheduled action.
              - `actions` (array of object) [maxItems=5] **REQ** — Represents the list of action execution records within this scheduled action group.
                - `id` (string/string) **REQ** — Represents the unique ID of the executed action.
                - `name` (string/string) **REQ** — Represents the name of the executed action.
                - `type` (string/string) **REQ** — Represents the type of action executed, such as **email_notifications**.
                - `queue_count` (integer/int32) **REQ** — Represents the number of execution instances currently in queue for this action.
                - `success_count` (integer/int32) **REQ** — Represents the number of successful executions for this action within the date range.
                - `failure_count` (integer/int32) **REQ** — Represents the number of failed executions for this action within the date range.
                - `associated_time` (string/date-time) **REQ** — Represents the ISO 8601 timestamp when this action was last executed or associated.
                - `related_details` (object) — Represents additional information related to the action execution, such as email notification performance metrics.
            - `usage_count` (integer/int32) **REQ** — Represents the total number of times the actions in this condition were executed.
            - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the WorkflowConditionUsageWithTaggedInstantActions within the workflow rule.
      - `reset_time` (string) **REQ** [maxLen=255, nullable] — Represents the ISO 8601 timestamp when the usage counters were last reset.

- **400**: The request could not be processed due to invalid or missing parameters.
**Resolution:** The caller must ensure all required parameters are present, date ranges are within allowed limits, and values use the correct data types and formats. — Schema: `InvalidDataNoApiNameAndPathSchema` [application/json]
    > Represents the error response returned when a required parameter such as the module API name or field path is missing from the request.

- **401**: Authentication failed.
**Resolution:** Verify that a valid OAuth access token with the ZohoCRM.settings.workflow_rules.READ scope is included in the Authorization header and has not expired. — Schema: `InvalidDataNoApiNameAndPathSchema` [application/json]
    > Represents the error response returned when a required parameter such as the module API name or field path is missing from the request.

- **403**: Feature not available in this edition.
**Resolution:** The Zoho CRM subscription must include an edition that supports workflow rules. — Schema: `NoPermissionSchema` [application/json]
    > Represents the error response returned when the authenticated user does not have permission to access the requested feature or module.
    schema: `NoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION', 'FEATURE_NOT_SUPPORTED']] — Represents the error code that identifies the specific error condition.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
    - `details` (object) **REQ** — Represents error details. For NO_PERMISSION, contains the list of permissions needed. For FEATURE_NOT_SUPPORTED, empty object.
      - `permissions` (array of string) [maxItems=10] — Represents the list of CRM profile permissions required to perform the requested action.
        items: [maxLen=255]

**Scopes:** ZohoCRM.settings.workflow_rules.READ
