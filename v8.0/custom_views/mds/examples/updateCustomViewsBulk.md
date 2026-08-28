# Examples: updateCustomViewsBulk

**PUT /settings/custom_views**

## Request examples

### `application/json` — PutRequestBody

Bulk update Custom Views request body

```json
{
  "custom_views": [
    {
      "id": "2411194000004076067",
      "name": "test1"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — PutRequestBody

Bulk update success response

```json
{
  "custom_views": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2411194000004076067"
      },
      "message": "custom view updated",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PutRequestBody

Bulk update partial success response

```json
{
  "custom_views": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2411194000004076067"
      },
      "message": "custom view updated",
      "status": "success"
    },
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.custom_views[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FailureResponse

Bulk update validation error

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "name"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth scope mismatch

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `403` — `application/json` — FailureResponse

Permission denied

```json
{
  "custom_views": [
    {
      "code": "NO_PERMISSION",
      "details": {
        "api_name": "id",
        "json_path": "$.custom_views[0].id"
      },
      "message": "Permission denied. Locked custom views cannot be customized.",
      "status": "error"
    }
  ]
}
```
