# Examples: deleteTaskById

**DELETE /settings/automation/tasks/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Task deleted successfully

```json
{
  "tasks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000035041"
      },
      "message": "task deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Error response with code NOT_ALLOWED: Task is associated with at least one of Approval Process/Workflow Rules/Blueprint

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "Task is associated with at least one of Approval Process/Workflow Rules/Blueprint",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: the id given seems to be invalid

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

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_manage_workflow"
    ]
  },
  "message": "permission denied",
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
