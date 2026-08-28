# DELETE /settings/automation/tasks
**Operation:** `deleteTasks` — Delete automation task definitions by IDs (bulk)
> PURPOSE: Deletes one or more automation task definitions by their IDs. MANDATORY: ids query parameter (comma-separated task IDs, max 10). KEY CONSTRAINTS: Tasks associated with active workflow rules, approval processes, or blueprints cannot be deleted (returns NOT_ALLOWED error). Returns per-task success/error status. Use GET /settings/automation/tasks to discover task IDs before deleting.

**Parameters:**
- `ids` (query, string, required) [maxLen=255, pattern=^[0-9]{1,20}(,[0-9]{1,20}){0,9}$]: Comma-separated automation task definition IDs to delete in bulk. Maximum 10 IDs per request. Each ID must be a numeric string (e.g., "111111000000200035,111111000000190030"). Tasks associated with active automation cannot be deleted  - returns NOT_ALLOWED per task.

**Schemas:**
`BulkDeleteTasksFailureItem`:
  > Result item for a task ID that failed during bulk delete. Code is INVALID_DATA when the ID does not exist, or NOT_ALLOWED when the task is associated with a rule/blueprint or is read-only.
  - `code` (string) **REQ** [enum=['INVALID_DATA', 'NOT_ALLOWED']] — Failure code.
  - `details` (object) **REQ** — Contains the failed task ID.
    - `id` (string) **REQ** [maxLen=20] — ID of the task that could not be deleted.
  - `message` (string) **REQ** [maxLen=255] — Failure message.
  - `status` (string) **REQ** [enum=['error']] — Operation status.
`BulkDeleteTasksSuccessItem`:
  > Result item for a task ID that was deleted successfully in a bulk delete operation.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Result code.
  - `details` (object) **REQ** — Contains the deleted task ID.
    - `id` (string) **REQ** [maxLen=20] — Unique ID of the deleted task.
  - `message` (string) **REQ** [maxLen=255] — Success message.
  - `status` (string) **REQ** [enum=['success']] — Operation status.
`TaskInvalidDataSchema`:
  > Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.
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

**Responses:**

- **200**: Bulk delete completed successfully for all requested task IDs. — Schema: `BulkDeleteTasksSuccessResponse` [application/json]
    > Bulk delete success response. All requested task IDs were deleted successfully.
    schema: `BulkDeleteTasksSuccessResponse`
    - `tasks` (array of object `BulkDeleteTasksSuccessItem`) [maxItems=10] **REQ** — Deletion result entries for each requested task ID.

- **207**: Bulk delete completed with mixed results. Some task IDs were deleted successfully while others failed with INVALID_DATA or NOT_ALLOWED. — Schema: `BulkDeleteTasksMixedResponse` [application/json]
    > Bulk delete partial-success response. Contains mixed success and failure items for the requested task IDs.
    schema: `BulkDeleteTasksMixedResponse`
    - `tasks` (array of object) [maxItems=10] **REQ** — Per-ID deletion results for the bulk request.
      oneOf:
        - `BulkDeleteTasksSuccessItem` — Result item for a task ID that was deleted successfully in a bulk delete operation.
        - `BulkDeleteTasksFailureItem` — Result item for a task ID that failed during bulk delete. Code is INVALID_DATA when the ID does not exist, or NOT_ALLOWED when the task is associated with a rule/blueprint or is read-only.

- **400**: Request validation failed or all provided task IDs failed deletion. Flat error for request-level issues (missing ids, limit exceeded, single-ID errors). Array response when multiple IDs all fail individually. [application/json]
    > Error response returned when a bulk delete of automation tasks fails validation, covering missing or oversized ids parameter and per-task delete failures.
    oneOf:
      - `RequiredParamMissingError` — Missing required parameter: ids
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [maxLen=255] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `TaskInvalidDataSchema` — Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.
      - `TaskNotAllowedSchema` — Returned when the requested operation is not allowed  - such as deleting a task associated with an Approval Process, Workflow Rule, or Blueprint, or modifying a read-only system-managed task.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Error code indicating operation not allowed.
        - `details` (object) **REQ** — Error details identifying the resource.
          - `resource_path_index` (integer/int32) — Index of the resource in the request array that caused the error.
        - `message` (string) **REQ** [maxLen=255] — Error message describing why the operation is not allowed.
        - `status` (string) **REQ** [enum=['error']] — Error status.
      - `BulkDeleteTasksAllFailedResponse` — Bulk delete response when all provided task IDs failed. Each item contains INVALID_DATA or NOT_ALLOWED details for that ID.
        - `tasks` (array of object `BulkDeleteTasksFailureItem`) [maxItems=10] **REQ** — Per-ID failure results for the bulk request.

- **401**: Authentication or scope error while deleting automation tasks. — Schema: `PostTasksAuthenticationErrorResponse` [application/json]
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

- **403**: Insufficient permission or feature not available in this CRM edition. — Schema: `TaskNoPermissionSchema` [application/json]
    > Returned when the caller does not have the required permissions to perform this operation or access this feature.
    schema: `TaskNoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating insufficient permissions.
    - `details` (object) **REQ** — Permission details required for this operation.
      - `permissions` (array of string) [maxItems=25] — Contains a list of required permissions for this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Error message describing the permission issue.
    - `status` (string) **REQ** [enum=['error']] — Error status.

- **404**: The provided task ID does not exist. — Schema: `TaskInvalidDataSchema` [application/json]
    > Returned when the request contains invalid data  - such as an unrecognized field, wrong data type, value exceeding maximum length, unsupported parameter value, or invalid resource ID.

- **500**: Internal server error. — Schema: `InternalServerErrorResponse` [application/json]
    > Error response when an unexpected server-side exception occurs.
    schema: `InternalServerErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Error code
    - `details` (object) **REQ** — Error details
    - `message` (string) **REQ** [maxLen=255] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.automation_actions.DELETE
