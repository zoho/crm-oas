# Examples: changePortalUsersStatusBulk

**PUT /settings/portals/{portal}/user_type/{userType}/users/actions/change_status**

## Request examples

### `application/json` — Example1

Request body for bulk status change

```json
{
  "change_status": [
    {
      "users": [
        {
          "active": false,
          "personality_id": "12346789899"
        },
        {
          "active": false,
          "personality_id": "12346789898"
        }
      ]
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful bulk status change

```json
{
  "change_status": [
    {
      "code": "SCHEDULED",
      "details": {
        "job_id": "5020928000000606073"
      },
      "message": "Portal bulk user status change scheduled successfully",
      "status": "success"
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
