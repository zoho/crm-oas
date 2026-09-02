# DELETE /settings/automation/workflow_rules
**Operation:** `deleteWorkflowRules` — Delete One or More Workflow Rules
> To delete one or more workflow rules from your Zoho CRM organization. You can delete up to ten workflow rules in a single API call; when some deletions succeed and others fail, the API responds with a 207 Multi-Status.


**Parameters:**
- `ids` (query, string/string, required): Specifies one or more workflow rule IDs to filter the results. Provide multiple IDs as comma-separated values.

**Schemas:**
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
`SuccessResponseDetailsSchema`:
  > Represents the details object within a success response, containing the unique ID of the created or updated resource.
  - `id` (string) [maxLen=255] — Represents the unique ID of the SuccessResponseDetails within the workflow rule.
`SuccessResponseNestedSchema`:
  > Represents a single item in a multi-status response array, including a response code, status indicator, message, and optionally the resource details.
  - `code` (string) [maxLen=255] — Represents the API response code indicating the operation result, such as **SUCCESS** or **INVALID_DATA**.
  - `details` (object `SuccessResponseDetailsSchema`) — Represents the details object within a success response, containing the unique ID of the created or updated resource.
  - `message` (string) [enum=[6 values]] — Represents the message describing the operation result or error.
  - `status` (string) [maxLen=7] — Represents the response status indicator, such as **success** or **error**.

**Responses:**

- **200**: Workflow Rule deleted successfully — Schema: `WorkflowSuccessSchema` [application/json]
    > Represents the success response returned after creating a workflow rule, containing the result details of the created rule.
    schema: `WorkflowSuccessSchema`
    - `workflow_rules` (array of object `SuccessResponseNestedSchema`) [maxItems=200] — Represents the array of workflow rule objects returned in the success response.

- **207**: Multi-status response returned when a bulk deletion request contains a mix of successful and failed deletions. Each entry indicates whether the corresponding workflow rule was deleted successfully or returned an error
 [application/json]
    > Wrapped error response with workflow_rules
    - `workflow_rules` (array of object) [maxItems=10] **REQ** — Array of error objects
      oneOf:
        - `InvalidDataNoApiNameAndPathSchema` — Represents the error response returned when a required parameter such as the module API name or field path is missing from the request.
        - `SuccessResponseNestedSchema` — Represents a single item in a multi-status response array, including a response code, status indicator, message, and optionally the resource details.

- **400**: The response returned when the deletion request is invalid, such as a malformed or missing rule ID. Resolution: verify the rule IDs in the request and resubmit. [application/json]
    oneOf:
      - `InvalidDataNoApiNameAndPathSchema` — Represents the error response returned when a required parameter such as the module API name or field path is missing from the request.
        - `workflow_rules` (array of object `InvalidDataNoApiNameAndPathSchema`) [maxItems=10] **REQ** — Array of error objects

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

**Scopes:** ZohoCRM.settings.workflow_rules.DELETE
