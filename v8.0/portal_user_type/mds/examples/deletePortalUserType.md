# Examples: deletePortalUserType

**DELETE /settings/portals/{portal}/user_type/{userTypeId}**

## Response examples

### Status `200` — `application/json` — Success200

Portal user type deleted successfully (200)

```json
{
  "user_type": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "5020928000002330000"
      },
      "message": "Portal user type deleted successfully.",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse1

Api not supported for client portal user (API_NOT_SUPPORTED)

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_login_user_type": "Client Portal User"
  },
  "message": "api not supported for client portal user",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse2

Api not supported in sandbox (API_NOT_SUPPORTED)

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

### Status `400` — `application/json` — ApiNotSupportedResponse3

Api not supported (API_NOT_SUPPORTED)

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "supported_domains": [
      "eu",
      "com",
      "in",
      "au",
      "ca",
      "cn",
      "jp"
    ]
  },
  "message": "api not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Deletion of portal user type is not allowed, as user type contains users, which need to be transferred to other user type (INVALID_DATA)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "transfer_To"
  },
  "message": "Deletion of portal user type is not allowed, as user type contains users, which need to be transferred to other user type",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidPortalNameResponse1

No portal exists with the given portal name. (INVALID_DATA)

```json
{
  "code": "INVALID_DATA",
  "details": {},
  "message": "No portal exists with the given portal name.",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission (NO_PERMISSION)

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_ClientPortal"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse2

NO_PERMISSION (NO_PERMISSION)

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "NO_PERMISSION",
  "status": "error"
}
```
