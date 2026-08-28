# Examples: deleteWebhooksById

**DELETE /settings/automation/webhooks/{webhookId}**

## Response examples

### Status `200` — `application/json` — Success200

Successful deletion of a single webhook by ID.

```json
{
  "webhooks": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "5725767000007098001"
      },
      "message": "Webhook is deleted",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedResponse1

Webhook created by a Marketplace extension cannot be deleted

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "Webhook  is associated with MarketPlace",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse2

Webhook associated with active automation rules cannot be deleted

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 3
  },
  "message": "This webhook is associated with at least one of Approval Process/Workflow Rules/Blueprint",
  "status": "error"
}
```

### Status `400` — `application/json` — NotAllowedResponse3

Read-only webhook cannot be deleted

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "id": "5249735000000100001"
  },
  "message": "Insufficient privileges to delete Read only webhook",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid webhook ID in request body

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.webhooks[0].id"
      },
      "message": "The ID given is invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidWebhookIdPathResponse1

Invalid webhook ID in URL path

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

### Status `403` — `application/json` — NoPermissionResponse1

Insufficient Manage Workflow permission to delete webhook

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
