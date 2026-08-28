# Examples: getTaskById

**GET /settings/automation/tasks/{id}**

## Response examples

### Status `200` — `application/json` — GetTaskByIdSuccessResponse

Single task retrieved successfully

```json
{
  "tasks": [
    {
      "created_time": "2023-10-20T11:17:30+05:30",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "111111000000002393"
      },
      "related_module": null,
      "deletable": true,
      "source": "user",
      "created_by": {
        "name": "vignesh B",
        "id": "111111000000051635"
      },
      "notify": false,
      "feature_type": "workflow",
      "field_mappings": [
        {
          "display_value": "efefdeff",
          "field": {
            "api_name": "Subject",
            "id": "111111000000000221"
          },
          "type": "static",
          "value": "efefdeff"
        },
        {
          "display_value": "From Date plus 1 day(s)",
          "field": {
            "api_name": "Due_Date",
            "id": "111111000000000223"
          },
          "type": "execution_time",
          "value": {
            "period": "days",
            "unit": "1",
            "trigger_field": "${CURRENTTIME}",
            "sign": "plus"
          }
        },
        {
          "display_value": "Not Started",
          "field": {
            "api_name": "Status",
            "id": "111111000000000229"
          },
          "type": "static",
          "value": "Not Started"
        },
        {
          "display_value": "High",
          "field": {
            "api_name": "Priority",
            "id": "111111000000000231"
          },
          "type": "static",
          "value": "High"
        }
      ],
      "modified_time": "2023-10-20T11:17:30+05:30",
      "associated": true,
      "modified_by": {
        "name": "vignesh B",
        "id": "111111000000051635"
      },
      "name": "efefdeff",
      "id": "111111000000190030"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidTaskIdResponse

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

### Status `400` — `application/json` — InvalidFeatureTypeResponse

INVALID_DATA: the given feature name is invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "feature_type"
  },
  "message": "the given feature name is invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse

INVALID_MODULE: The value provided to the param is Invalid

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "The value provided to the param is Invalid",
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
