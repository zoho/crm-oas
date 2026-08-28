# Examples: deleteTasks

**DELETE /settings/automation/tasks**

## Response examples

### Status `200` — `application/json` — BulkDeleteSuccessResponse

All tasks deleted successfully

```json
{
  "tasks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000098788"
      },
      "message": "task deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — BulkDeleteMixedResponse

Mixed success and failure results

```json
{
  "tasks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000200035"
      },
      "message": "task deleted successfully",
      "status": "success"
    },
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000190030"
      },
      "message": "the specified task is associated with at least one of Approval Process/Workflow Rules/Blueprint",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000165002"
      },
      "message": "task deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse

REQUIRED_PARAM_MISSING: ids query parameter not provided

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "ids"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — IdsLimitExceededResponse

INVALID_DATA: More than 10 IDs provided in the ids parameter

```json
{
  "code": "INVALID_DATA",
  "details": {
    "maximum_length": 10,
    "param_name": "ids"
  },
  "message": "Ids maximum length exceeded",
  "status": "error"
}
```

### Status `400` — `application/json` — TaskAssociatedNotAllowedResponse

NOT_ALLOWED: Task is linked to a workflow rule, Approval Process, or Blueprint

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "the specified task is associated with at least one of Approval Process/Workflow Rules/Blueprint",
  "status": "error"
}
```

### Status `400` — `application/json` — ReadOnlyActionNotAllowedResponse

NOT_ALLOWED: Cannot delete a read-only or system-managed task

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "Insufficient privileges to delete action",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidIdResponse

INVALID_DATA: One of the provided task IDs does not exist

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — AllFailedArrayResponse

All IDs failed  - per-ID error details in array

```json
{
  "tasks": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000190030"
      },
      "message": "the specified task is associated with at least one of Approval Process/Workflow Rules/Blueprint",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000195072"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000195032"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — OauthScopeMismatchResponse

OAUTH_SCOPE_MISMATCH: Unauthorized

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "Unauthorized",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailureResponse

AUTHENTICATION_FAILURE: Authentication failed

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse

NO_PERMISSION: feature not available in this edition

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow",
      "WorkFlow_Tasks"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidTaskIdResponse

INVALID_DATA: the id given seems to be invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalServerErrorResponse

INTERNAL_ERROR: Internal Server Error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
