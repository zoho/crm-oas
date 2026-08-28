# Examples: deleteWorkflowRuleById

**DELETE /settings/automation/workflow_rules/{id}**

## Response examples

### Status `200` — `application/json` — SuccessResponse

Successful deletion of a workflow rule by ID

```json
{
  "workflow_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006294001"
      },
      "message": "workflow deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — UrlPathIdMissing

400 error — invalid workflow rule ID in the request URL path

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

### Status `400` — `application/json` — NotAllowedErrorResponse

400 error — delete operation not allowed for the workflow rule ID

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse

403 error — insufficient permission to delete workflow rules

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```
