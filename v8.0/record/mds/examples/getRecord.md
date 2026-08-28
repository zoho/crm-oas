# Examples: getRecord

**GET /{module}/{recordId}**

## Parameter examples

### `module` (path) — Example

```json
"Leads"
```

## Response examples

### Status `200` — `application/json` — Leads

Records retrieved from the Leads module

```json
{
  "data": [
    {
      "id": "4150868000000002175",
      "Owner": {
        "name": "Patricia Boyle",
        "id": "4150868000000225013",
        "email": "patricia.boyle@example.com"
      },
      "Company": "Zylker Corp",
      "First_Name": "John",
      "Last_Name": "Doe",
      "Email": "john.doe@zylker.com",
      "Phone": "+1-555-123-4567",
      "Lead_Status": "Not Contacted",
      "Created_Time": "2023-10-15T10:30:00+00:00",
      "Modified_Time": "2023-10-15T14:20:00+00:00"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid field value in the request

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 0
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — TokenBoundDataMismatch

TokenBoundDataMismatch response example

```json
{
  "code": "TOKEN_BOUND_DATA_MISMATCH",
  "message": "The page_token given seems to be invalid or input param is added or altered or deleted",
  "status": "error",
  "details": {
    "param_name": "page_token"
  }
}
```

### Status `400` — `application/json` — ExpiredValue

ExpiredValue response example

```json
{
  "status": "error",
  "code": "EXPIRED_VALUE",
  "message": "Page token expired",
  "details": {
    "api_name": "page_token",
    "json_path": "$.query.page_token"
  }
}
```

### Status `401` — `application/json` — ScopeMismatch

OAuth access token missing the required scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "Unauthorized",
  "status": "error",
  "details": {}
}
```

### Status `403` — `application/json` — NoPermission

User profile lacks the required module permission

```json
{
  "code": "NO_PERMISSION",
  "message": "Permission denied",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_View_Leads"
    ]
  }
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Invalid or unrecognized API endpoint URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error",
  "details": {}
}
```

### Status `500` — `application/json` — InternalError

Unexpected internal server error during processing

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "status": "error",
  "details": {}
}
```
