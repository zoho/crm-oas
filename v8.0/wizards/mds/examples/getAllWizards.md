# Examples: getAllWizards

**GET /settings/wizards**

## Response examples

### Status `200` — `application/json` — Success

Successful retrieval of all configured wizards in the organization

```json
{
  "wizards": [
    {
      "created_time": "2025-11-26T08:59:44+05:30",
      "modified_time": "2025-11-26T15:58:16+05:30",
      "display_label": "Example Wizard",
      "portal_user_types": [
        {
          "display_label": "ClientPortal",
          "name": "ClientPortal",
          "id": "3733145000000570124"
        }
      ],
      "module": {
        "api_name": "Contacts",
        "id": "3733145000000570138"
      },
      "name": "example_wizard",
      "modified_by": {
        "name": "Alice",
        "id": "3733145000000556001"
      },
      "profiles": [
        {
          "name": "Administrator",
          "id": "3733145000000570117",
          "display_label": "Administrator"
        }
      ],
      "active": true,
      "source": "crm",
      "containers": [
        {
          "layout": {
            "name": "Standard",
            "display_label": "Standard",
            "id": "3733145000000570510"
          },
          "screens": [
            {
              "api_name": "screen1",
              "id": "3733145000001209037",
              "display_label": "Screen 1"
            }
          ],
          "id": "3733145000000570510"
        }
      ],
      "id": "3733145000001209011",
      "created_by": {
        "name": "Bob",
        "id": "3733145000000556001"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

400 error returned when an unrecognized module API name is provided

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "The module name seems to be invalid",
  "status": "error"
}
```

### Status `401` — `application/json` — OauthScopeMismatch

Access token lacks the required OAuth scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `401` — `application/json` — InvalidToken

Access token is invalid or expired

```json
{
  "code": "INVALID_TOKEN",
  "details": {},
  "message": "invalid oauth token",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

User profile lacks permission to read wizards

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Zoho CRM: Settings Permission"
    ]
  },
  "message": "Permission denied to read wizards",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Request URL does not match a valid endpoint pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```
