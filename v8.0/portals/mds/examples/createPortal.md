# Examples: createPortal

**POST /settings/portals**

## Request examples

### `application/json` — Default

Sample portal creation request

```json
{
  "portals": [
    {
      "name": "examplePortal"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Default

Successful portal creation

```json
{
  "portals": [
    {
      "code": "SUCCESS",
      "message": "Portal created successfully",
      "details": {
        "name": "examplePortal"
      },
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Example1

INVALID_DATA - portal name validation error

```json
{
  "portals": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.portals[0].name",
        "minimum_length": 6
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example2

ALREADY_USED - portal name already in use

```json
{
  "portals": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "name"
      },
      "message": "The entered portal name is already in use",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — Example3

MANDATORY_NOT_FOUND - required field missing

```json
{
  "portals": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.portals[0].name"
      },
      "message": "required field not found",
      "status": "error"
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

NO_PERMISSION - required permission missing

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_ClientPortal"
    ]
  },
  "message": "Permission is invalid.",
  "status": "error"
}
```

### Status `403` — `application/json` — Example2

NO_PERMISSION - insufficient portal permission

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "Permission is invalid.",
  "status": "error"
}
```
