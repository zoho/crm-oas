# Examples: getPortalUsers

**GET /settings/portals/{portal}/user_type/{userType}/users**

## Response examples

### Status `200` — `application/json` — Example1

List of portal users with response metadata

```json
{
  "users": [
    {
      "personality_id": "12345",
      "confirm": true,
      "status_reason__s": "Active",
      "created_time": "2023-01-15T10:30:00Z",
      "module": "Contacts",
      "name": "John Doe",
      "active": true,
      "email": "john.doe@example.com",
      "Source__s": "Portal"
    }
  ],
  "info": {
    "total_count": 1
  }
}
```

### Status `400` — `application/json` — InvalidType

Error when a parameter value does not match the expected pattern

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "details": {
    "api_name": "type"
  },
  "message": "Please check whether the input values are correct",
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
