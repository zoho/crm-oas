# Examples: deleteWebhooks

**DELETE /settings/automation/webhooks**

## Response examples

### Status `200` — `application/json` — Success200

Successful bulk deletion of webhooks

```json
{
  "webhooks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "5249735000000100001"
      },
      "message": "Webhook is deleted",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "5249735000000100002"
      },
      "message": "Webhook is deleted",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — Success207

Partial success with mixed deletion results.

```json
{
  "webhooks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000066004"
      },
      "message": "webhook deleted successfully",
      "status": "success"
    },
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "111111000000057597"
      },
      "message": "webhook is associated with at least one of Approval Process/Workflow Rules/Blueprint",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse1

REQUIRED_PARAM_MISSING error for absent ids parameter.

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

### Status `400` — `application/json` — InvalidDataResponse1

INVALID_DATA error for an invalid webhook ID.

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "ids",
    "limit": 10
  },
  "message": "Bulk deletion of records limit reached",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedReadOnlyResponse1

NOT_ALLOWED error for a read-only webhook.

```json
{
  "webhooks": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "5249735000000100001"
      },
      "message": "Insufficient privileges to delete Read only webhook",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedAssociatedResponse1

NOT_ALLOWED error for a webhook associated with automation rules.

```json
{
  "webhooks": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "id": "5249735000000100001"
      },
      "message": "This webhook is associated with at least one of Approval Process/Workflow Rules/Blueprint",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

NO_PERMISSION error for insufficient profile privileges.

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
