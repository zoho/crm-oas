# DELETE /settings/automation/workflow_rules/{id}
**Operation:** `deleteWorkflowRuleById` — Delete a workflow rule by ID
> To delete a workflow rule from your Zoho CRM organization by its unique ID. Locked workflow rules cannot be deleted.


**Parameters:**
- `id` (path, string/string, required): Represents the unique 19-digit numeric ID of the workflow rule. Obtain valid IDs from the List Workflow Rules endpoint.

**Responses:**

- **200**: Returns the result of the workflow rule deletion, including the workflow rule ID and a success status. — Schema: `WorkflowSuccessSchema` [application/json]
    > Represents the success response returned after creating a workflow rule, containing the result details of the created rule.
    schema: `WorkflowSuccessSchema`
    - `workflow_rules` (array of object `SuccessResponseNestedSchema`) [maxItems=200] — Represents the array of workflow rule objects returned in the success response.
      schema: `SuccessResponseNestedSchema`
      - `code` (string) [maxLen=255] — Represents the API response code indicating the operation result, such as **SUCCESS** or **INVALID_DATA**.
      - `details` (object `SuccessResponseDetailsSchema`) — Represents the details object within a success response, containing the unique ID of the created or updated resource.
        schema: `SuccessResponseDetailsSchema`
        - `id` (string) [maxLen=255] — Represents the unique ID of the SuccessResponseDetails within the workflow rule.
      - `message` (string) [enum=[6 values]] — Represents the message describing the operation result or error.
      - `status` (string) [maxLen=7] — Represents the response status indicator, such as **success** or **error**.

- **400**: The workflow rule ID provided in the request URL is invalid or the action is not permitted.
**Resolution:** Verify that the workflow rule ID in the request path is a valid numeric ID and that the operation is allowed for the target workflow rule. — Schema: `UrlIdMissingSchema` [application/json]
    > Represents the error response returned when the workflow rule ID provided in the URL path is invalid or does not match an existing record.
    schema: `UrlIdMissingSchema`
    - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Represents the error code that identifies the specific error condition.
    - `details` (object) **REQ** — Represents the error details containing additional context about the failed request.
      - `resource_path_index` (integer/int32) — Represents the **resource_path_index** value from the error detail object.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.

- **403**: The user does not have permission to delete workflow rules.
**Resolution:** The CRM administrator must grant the required permission to the user's CRM profile. — Schema: `NoPermissionSchema` [application/json]
    > Represents the error response returned when the authenticated user does not have permission to access the requested feature or module.
    schema: `NoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION', 'FEATURE_NOT_SUPPORTED']] — Represents the error code that identifies the specific error condition.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
    - `details` (object) **REQ** — Represents error details. For NO_PERMISSION, contains the list of permissions needed. For FEATURE_NOT_SUPPORTED, empty object.
      - `permissions` (array of string) [maxItems=10] — Represents the list of CRM profile permissions required to perform the requested action.
        items: [maxLen=255]

**Scopes:** ZohoCRM.settings.workflow_rules.DELETE
