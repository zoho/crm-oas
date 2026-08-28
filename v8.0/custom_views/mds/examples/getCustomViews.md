# Examples: getCustomViews

**GET /settings/custom_views**

## Parameter examples

### `ids` (query) — Example

```json
[
  "123456789012345",
  "234567890123456"
]
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

Get all Custom Views success response

```json
{
  "custom_views": [
    {
      "display_value": "Character limit tooltip",
      "created_time": "2025-11-17T09:55:04-02:00",
      "access_type": "only_to_me",
      "system_name": null,
      "created_by": {
        "name": "Jess Moana",
        "id": "2411194000000478001"
      },
      "default": false,
      "modified_time": "2025-11-26T02:50:12-02:00",
      "name": "Character limit tooltip",
      "system_defined": false,
      "modified_by": {
        "name": "Jess Moana",
        "id": "2411194000000478001"
      },
      "id": "2411194000003855598",
      "category": "created_by_me",
      "last_accessed_time": "2025-11-26T09:00:24-02:00",
      "locked": false
    }
  ],
  "info": {
    "per_page": 200,
    "default": "2411194000004030016",
    "count": 10,
    "translation": {
      "public_views": "Public Views",
      "other_users_views": "Other User's Views",
      "shared_with_me": "Shared With Me",
      "created_by_me": "Created By Me"
    },
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — FailureResponse

Invalid request error

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
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
