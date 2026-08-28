# Examples: changeSortById

**PUT /settings/custom_views/{id}/actions/change_sort**

## Request examples

### `application/json` — ChangeSortRequest

Change sort order by ID request body

```json
{
  "custom_views": [
    {
      "sort_by": {
        "id": "2411194000000000597",
        "api_name": "Full_Name"
      },
      "sort_order": "asc"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

Change sort by ID success response

```json
{
  "custom_views": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2411194000000091501"
      },
      "message": "custom view updated",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — FailureResponse

Invalid sort order error

```json
{
  "custom_views": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "api_name",
        "json_path": "$.custom_views[0].sort_by.api_name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
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

### Status `403` — `application/json` — NoPermissionError

Permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": []
  },
  "message": "permission denied",
  "status": "error"
}
```
