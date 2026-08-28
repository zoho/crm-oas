# GET /settings/automation/workflow_rules/actions/actions_count
**Operation:** `getWorkflowRulesActionsCount` — Get Workflow Rule Action Counts
> To retrieve the total number of actions configured in the specified workflow rules in your Zoho CRM organization, including counts categorized by action type across both instant and scheduled actions.

**Parameters:**
- `ids` (query, string/string, required): Specifies one or more workflow rule IDs to filter the results. Provide multiple IDs as comma-separated values.

**Schemas:**
`ActionsCountSummarySchema`:
  > Represents a summary of execution count entries for instant actions in a workflow rule condition, categorized by action type.
  - `actions_count` (array of object) [maxItems=10] **REQ** — Represents the list of action count entries, each categorized by action type, for the workflow rule.
    - `type` (string) **REQ** [enum=[29 values]] — Represents the category of workflow action to which the execution count applies, such as email notifications, field updates, or webhooks.
    - `value` (integer/int32) **REQ** — Represents the total execution count for the specified action type within the queried date range.

**Responses:**

- **200**: OK - Successful response — Schema: `WorkflowActionCountsResponseSchema` [application/json]
    > Represents the response body containing the action count breakdown for one or more workflow rules, grouped by condition.
    schema: `WorkflowActionCountsResponseSchema`
    - `workflow_rules` (array of object `WorkflowRuleActionCountGroupSchema`) [maxItems=10] **REQ** — Represents the array of workflow rule objects with their action count details.
      schema: `WorkflowRuleActionCountGroupSchema`
      - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the WorkflowRuleActionCountGroup within the workflow rule.
      - `conditions` (array of object `WorkflowConditionActionCountSummarySchema`) [maxItems=10] **REQ** — Represents array of condition objects containing criteria and actions for this rule.
        schema: `WorkflowConditionActionCountSummarySchema`
        - `sequence_number` (integer/int32) **REQ** — Represents the execution order of this condition within the workflow rule, starting from one.
        - `instant_actions` (object) **REQ**
          oneOf:
            - `ActionsCountSummarySchema` — Represents a summary of execution count entries for instant actions in a workflow rule condition, categorized by action type.
              type: null — Represents a null value indicating no instant actions are configured for this condition.
        - `scheduled_actions` (array of object `ActionsCountSummarySchema`) [maxItems=5, nullable] **REQ** — Represents the array of scheduled action groups configured for this condition.
        - `id` (string) **REQ** [maxLen=20] — Represents the unique ID of the WorkflowConditionActionCountSummary within the workflow rule.

- **204**: No Content - Successful response with no body

- **400**: The response returned when the deletion request is invalid, such as a malformed or missing rule ID. Resolution: verify the rule IDs in the request and resubmit.
 — Schema: `InvalidDataNoApiNameAndPathSchema` [application/json]
    > Represents the error response returned when a required parameter such as the module API name or field path is missing from the request.
    schema: `InvalidDataNoApiNameAndPathSchema`
    - `code` (string) **REQ** [enum=[9 values]] — Represents the error code that identifies the specific error condition.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
    - `details` (object) **REQ** — Represents the error details containing additional context about the failed request.
      - `param_name` (string) [enum=[7 values]] — Represents the **param_name** value from the error detail object.
      - `maximum_length` (integer/int32) — Represents the **maximum_length** value from the error detail object.
      - `id` (string) [maxLen=20] — Represents the **ID** value from the error detail object.
      - `expected_data_type` (string) [maxLen=255] — Represents the **expected_data_type** value from the error detail object.
      - `api_name` (string) [maxLen=255] — Represents the API name of the field or parameter that caused the validation error.

- **403**: Forbidden. The authenticated user does not have permission to perform this operation, or the workflow rules feature is not available in the current CRM edition. Resolution: verify the user's permissions and the organization's edition capabilities.
 — Schema: `NoPermissionSchema` [application/json]
    > Represents the error response returned when the authenticated user does not have permission to access the requested feature or module.
    schema: `NoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION', 'FEATURE_NOT_SUPPORTED']] — Represents the error code that identifies the specific error condition.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
    - `details` (object) **REQ** — Represents error details. For NO_PERMISSION, contains the list of permissions needed. For FEATURE_NOT_SUPPORTED, empty object.
      - `permissions` (array of string) [maxItems=10] — Represents the list of CRM profile permissions required to perform the requested action.
        items: [maxLen=255]

**Scopes:** ZohoCRM.settings.workflow_rules.READ
