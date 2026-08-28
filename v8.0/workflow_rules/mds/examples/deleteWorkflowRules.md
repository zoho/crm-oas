# Examples: deleteWorkflowRules

**DELETE /settings/automation/workflow_rules**

## Response examples

### Status `200` — `application/json` — SuccessResponse

DELETE- Success response for status 200

```json
{
  "workflow_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006461011"
      },
      "message": "WorkFlow Rule deleted successfully",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006492426"
      },
      "message": "WorkFlow Rule deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — MultiStatusErrorRespose

MultiStatus response for status 207

```json
{
  "workflow_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006492443"
      },
      "message": "WorkFlow Rule deleted successfully",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "3361265000006492444"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "3361265000006492445"
      },
      "message": "Sorry, you cannot perform this operation as the record is locked.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingErrorResponse

Error response with code REQUIRED_PARAM_MISSING

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

### Status `400` — `application/json` — ActionLimitExceededResponse

Error response with code INVALID_DATA

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

### Status `400` — `application/json` — MultipleErrorResponse

Error response with code multiple INVALID_DATA

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "3361265000006492443"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "3361265000006492444"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "3361265000006492445"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse

Error response for status 403

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
