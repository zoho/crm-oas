# Examples: getPortals

**GET /settings/portals**

## Response examples

### Status `200` — `application/json` — Default

Successful portal list retrieval

```json
{
  "portals": [
    {
      "created_time": "2022-12-20T10:23:57Z",
      "modified_time": "2022-12-20T10:23:57Z",
      "modified_by": {
        "name": "John Doe",
        "id": "1234567890"
      },
      "name": "portalname",
      "created_by": {
        "name": "Jane Doe",
        "id": "0987654321"
      },
      "zaid": "1234567890",
      "active": true,
      "login_url": "www.example.com"
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupportedResponse1

API_NOT_SUPPORTED - sandbox environment

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

### Status `403` — `application/json` — Example1

NO_PERMISSION - insufficient portal permission

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "Permission is invalid.",
  "status": "error"
}
```
