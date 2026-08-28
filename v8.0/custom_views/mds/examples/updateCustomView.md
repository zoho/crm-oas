# Examples: updateCustomView

**PUT /settings/custom_views/{id}**

## Request examples

### `application/json` — PutRequestBody

Update Custom View request body

```json
{
  "custom_views": [
    {
      "name": "updatedName"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — PutSuccessResponse

Custom view updated successfully

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

### Status `400` — `application/json` — PutErrorResponse

Update Custom View validation error

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "fields"
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
  "code": "NO_PERMISSION",
  "details": {
    "resource_path_index": 2
  },
  "message": "Permission denied. Locked custom views cannot be customized.",
  "status": "error"
}
```
