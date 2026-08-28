# Examples: transferPortalUsers

**POST /settings/portals/{portal}/user_type/{userType}/users/action/transfer**

## Response examples

### Status `200` — `application/json` — Success

Successful transfer of portal users

```json
{
  "users": [
    {
      "code": "SUCCESS",
      "details": {
        "personality_id": "5020928000000606073"
      },
      "message": "User has been transferred successfully",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "personality_id": "5020928000002110005"
      },
      "message": "User has been transferred successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Error when the transfer data is invalid

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "personality_id": "1234567890"
      },
      "message": "Transfer of user failed as personality id does not belongs to any portal user or belongs to portal user, who does not belongs to provided user type.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RequiredParamMissing

Error when a required parameter is missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param": "transfer_To"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
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
  "message": "User has been transferred successfully",
  "status": "error"
}
```
