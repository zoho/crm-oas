# DELETE /settings/automation/tasks/{id}
**Operation:** `deleteTaskById` — Automation Task
> PURPOSE: Deletes a single automation task definition by its ID. MANDATORY: id path parameter (string - automation task definition ID, not a Task record ID). KEY CONSTRAINTS: Tasks associated with active workflow rules, approval processes, or blueprints cannot be deleted (returns NOT_ALLOWED). Returns success/error status.

**Parameters:**
- `id` (path, string, required) [maxLen=20]: Represents the unique ID of the task that you want to delete. Skip this parameter if you have specified the ID in the request URL. You can pass upto 10 comma-separated IDs in this parameter. Tasks associated with active workflow rules, approval processes, or blueprints cannot be deleted. Use the [Workflow Tasks API](workflow_tasks.yaml#$.paths./settings/automation/tasks.get) to retrieve the ID.


**Responses:**

- **200**: Task deleted successfully. — Schema: `DeleteTaskByIdSuccessResponse` [application/json]
    > Single-task delete success response.
    schema: `DeleteTaskByIdSuccessResponse`
    - `tasks` (array of object `TaskActionResult`) [minItems=1, maxItems=1] **REQ** — Contains one success result object for the deleted task.
      schema: `TaskActionResult`
      - `code` (string) **REQ** [maxLen=255] — Operation result code (e.g., SUCCESS).
      - `details` (object `TaskActionResultDetails`) **REQ** — Details returned with a task action result, including the created or affected resource ID.
        schema: `TaskActionResultDetails`
        - `resource_path_index` (string) [maxLen=255] — Index of the resource in the request payload array.
        - `id` (string) **REQ** [maxLen=20] — Unique ID of the created or affected automation task.
      - `message` (string) **REQ** [maxLen=255] — Result message describing the outcome of the task action.
      - `status` (string) **REQ** [maxLen=255] — Operation result status (e.g., success).

- **400**: Invalid task ID or task cannot be deleted due to active association with workflow/approval/Blueprint. [application/json]
    > Error response returned when a single automation task delete fails validation, such as an invalid ID or the task being associated with active automation.
    oneOf:
      - `TaskNotAllowedSchema` — Returned when the requested operation is not allowed  - such as deleting a task associated with an Approval Process, Workflow Rule, or Blueprint, or modifying a read-only system-managed task.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating operation not allowed.
        - `details` (object) **REQ** — Error details identifying the resource.
          - `resource_path_index` (integer/int32) — Index of the resource in the request array that caused the error.
        - `message` (string) **REQ** [maxLen=255] — Error message describing why the operation is not allowed.
        - `status` (string) **REQ** [enum=['error']] — Error status.
      - `TaskInvalidDataSchema` — Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code indicating invalid data.
        - `details` (object) **REQ** — Error details with contextual validation information.
          - `api_name` (string) [maxLen=255] — API name of the field that caused the error.
          - `json_path` (string) [maxLen=1000] — JSON path pointing to the invalid value in the request payload.
          - `expected_data_type` (string) [maxLen=255] — Expected data type for the field value.
          - `supported_values` (array of string) [maxItems=25] — List of accepted values for this field.
            items: [maxLen=255]
          - `maximum_length` (integer/int32) — Maximum allowed length or count for the field value.
          - `param_name` (string) [maxLen=255] — Name of the query parameter that caused the error.
          - `resource_path_index` (integer/int32) — Index of the resource in the request array that caused the error.
        - `message` (string) **REQ** [maxLen=255] — Error message describing the invalid data condition.
        - `status` (string) **REQ** [enum=['error']] — Error status.

- **401**: Authentication or scope error while deleting the automation task. — Schema: `PostTasksAuthenticationErrorResponse` [application/json]
    > Authentication or OAuth scope error response for POST automation tasks.
    oneOf:
      - `OAuthScopeMismatchErrorResponse` — Error response when access token does not include the required OAuth scope.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code
        - `details` (object) **REQ** — Error details
        - `message` (string) **REQ** [maxLen=255] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `AuthenticationFailureErrorResponse` — Error response when authentication token is invalid or missing.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Error code
        - `details` (object) **REQ** — Error details
        - `message` (string) **REQ** [maxLen=255] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Insufficient permission to delete automation tasks. — Schema: `TaskNoPermissionSchema` [application/json]
    > Returned when the caller does not have the required permissions to perform this operation or access this feature.
    schema: `TaskNoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating insufficient permissions.
    - `details` (object) **REQ** — Permission details required for this operation.
      - `permissions` (array of string) [maxItems=25] — Contains a list of required permissions for this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Error message describing the permission issue.
    - `status` (string) **REQ** [enum=['error']] — Error status.

- **500**: Internal server error. — Schema: `InternalServerErrorResponse` [application/json]
    > Error response when an unexpected server-side exception occurs.
    schema: `InternalServerErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Error code
    - `details` (object) **REQ** — Error details
    - `message` (string) **REQ** [maxLen=255] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.automation_actions.DELETE
