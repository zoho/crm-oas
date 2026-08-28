# Examples: deletePortalUsers

**DELETE /settings/portals/{portal}/user_type/{userType}/users**

## Response examples

### Status `200` — `application/json` — Success

Successful deletion of portal users

```json
{
  "users": [
    {
      "code": "SUCCESS",
      "details": {
        "personality_id": "12345"
      },
      "message": "User deleted successfully",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "personality_id": "67890"
      },
      "message": "User deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Error when the personality ID is invalid

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "personality_id": "5020928000001843001"
      },
      "message": "Delete of user failed as personality id does not belongs to any portal user or belongs to portal user, who does not belongs to provided user type.",
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
