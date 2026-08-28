# Examples: changePortalUsersStatus

**PUT /settings/portals/{portal}/user_type/{userType}/users/{recordId}/actions/change_status**

## Response examples

### Status `200` — `application/json` — Success

Successful status change for a portal user

```json
{
  "change_status": [
    {
      "code": "SUCCESS",
      "details": {
        "personality_id": "5020928000000606073"
      },
      "message": "Status of the user changed successfully.",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowed

Error when the status change is not allowed

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": "6"
  },
  "message": "Deactivating unconfirmed user is not allowed",
  "status": "error"
}
```

### Status `400` — `application/json` — LimitExceeded

Error when the portal user limit is exceeded

```json
{
  "code": "LIMIT_EXCEEDED",
  "details": {
    "limit": 0
  },
  "message": "License Limit has been exceeded.",
  "status": "error"
}
```

### Status `400` — `application/json` — AlreadyActivated

Error when user is already activated

```json
{
  "code": "ALREADY_ACTIVATED",
  "details": {
    "resource_path_index": "6"
  },
  "message": "Already in active state only.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidData

Error when the personality ID is invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": "6"
  },
  "message": "Activation/Deactivation of portal user whose personality record in recyclebin is not allowed.",
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
  "message": "NO_PERMISSION",
  "status": "error"
}
```
