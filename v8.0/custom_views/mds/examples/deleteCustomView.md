# Examples: deleteCustomView

**DELETE /settings/custom_views**

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

Delete Custom View success response

```json
{
  "custom_views": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2411194000004030016"
      },
      "message": "deleted successfully",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccessResponse

Partial delete success and failure

```json
{
  "custom_views": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2411194000004030016"
      },
      "message": "deleted successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "12"
      },
      "message": "The provided CustomView is either invalid or already Deleted",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FailureResponse

Invalid Custom View ID error

```json
{
  "custom_views": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "12"
      },
      "message": "The provided CustomView is either invalid or already Deleted",
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
