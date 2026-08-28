# PUT /settings/automation/workflow_rules/actions/reorder
**Operation:** `reorderWorkflowRules` — Update Workflow Rule Execution Order for Module
> To update the execution order of workflow rules for a specific module in your Zoho CRM organization. By default, rules execute in the order in which they were created. If any of the specified rule IDs are invalid, the entire request fails and no partial updates are applied.

**Parameters:**
- `module` (query, string/string, optional): Specifies the CRM module API name to filter workflow rules by, such as Leads, Contacts, or Deals.

**Request Body** — application/json `ReorderWorkflowRulesRequestSchema`
> Workflow rule configuration payload.
  > Represents the request body for reordering workflow rules, containing the new position assignments for each rule.
  - `reorder` (object) **REQ** — Represents the reorder payload containing the list of workflow rules and their updated execution order.
    - `workflow_rules` (array of object) [maxItems=10] — Represents the array of workflow rule objects for which you want to update the execution order.
      - `module_specific_sequence` (integer/int32) **REQ** — Specify the new execution order for this workflow rule within the module. The index must start from one.
      - `id` (string) **REQ** [maxLen=20] — Specify the ID of the workflow rule for which you want to update the execution order.

**Responses:**

- **200**: OK - Successful response — Schema: `ReOrderSuccessResponseSchema` [application/json]
    > Represents the success response returned after reordering workflow rules.
    schema: `ReOrderSuccessResponseSchema`
    - `reorder` (array of object `SuccessResponseNestedSchema`) [maxItems=125] — Represents the array of workflow rule objects with their updated execution order.
      schema: `SuccessResponseNestedSchema`
      - `code` (string) [maxLen=255] — Represents the API response code indicating the operation result, such as **SUCCESS** or **INVALID_DATA**.
      - `details` (object `SuccessResponseDetailsSchema`) — Represents the details object within a success response, containing the unique ID of the created or updated resource.
        schema: `SuccessResponseDetailsSchema`
        - `id` (string) [maxLen=255] — Represents the unique ID of the SuccessResponseDetails within the workflow rule.
      - `message` (string) [enum=[6 values]] — Represents the message describing the operation result or error.
      - `status` (string) [maxLen=7] — Represents the response status indicator, such as **success** or **error**.

- **400**: The response returned when the deletion request is invalid, such as a malformed or missing rule ID.
 [application/json]
    oneOf:
      - `InvalidDataNoApiNameAndPathSchema` — Represents the error response returned when a required parameter such as the module API name or field path is missing from the request.
        - `code` (string) **REQ** [enum=[9 values]] — Represents the error code that identifies the specific error condition.
        - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
        - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
        - `details` (object) **REQ** — Represents the error details containing additional context about the failed request.
          - `param_name` (string) [enum=[7 values]] — Represents the **param_name** value from the error detail object.
          - `maximum_length` (integer/int32) — Represents the **maximum_length** value from the error detail object.
          - `id` (string) [maxLen=20] — Represents the **ID** value from the error detail object.
          - `expected_data_type` (string) [maxLen=255] — Represents the **expected_data_type** value from the error detail object.
          - `api_name` (string) [maxLen=255] — Represents the API name of the field or parameter that caused the validation error.
        - `reorder` (array of object) [maxItems=10] — Array of error objects

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

**Scopes:** ZohoCRM.settings.workflow_rules.UPDATE
