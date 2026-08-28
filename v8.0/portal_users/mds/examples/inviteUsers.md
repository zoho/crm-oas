# Examples: inviteUsers

**POST /{module}/actions/portal_invite**

## Request examples

### `application/json` — Example1

Example1 example

```json
{
  "portal_invite": [
    {
      "data": [
        {
          "id": "5843104000000624013",
          "user_type_id": "5843104000000411001",
          "type": "invite",
          "language": "en_US"
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Example1

Successful scheduled bulk portal invitation

```json
{
  "portal_invite": [
    {
      "code": "SCHEDULED",
      "details": {
        "job_id": "5020928000002338037"
      },
      "message": "Portal bulk invite scheduled successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

Error when a required field is missing from the request

```json
{
  "portal_invite": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "user_type_id",
        "json_path": "$.portal_invite[0].data[0].user_type_id"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupported

Error when the API runs in a sandbox environment

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_environment": "sandbox"
  },
  "message": "api not supported in sandbox",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissions

Error when the user lacks required permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_ClientPortal_Users"
    ]
  },
  "message": "NO_PERMISSION",
  "status": "error"
}
```
