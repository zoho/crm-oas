# Examples: deleteNotesModule

**DELETE /Notes**

## Response examples

### Status `200` — `application/json` — SuccessfulDeletion

Note successfully deleted

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4876876000006021002"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `200` — `application/json` — BulkDeletion

Multiple notes successfully deleted

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4876876000006021002"
      },
      "message": "record deleted",
      "status": "success"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "4876876000006021003"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — PartialSuccess

Partial success - some notes deleted, some failed

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000116001"
      },
      "message": "record deleted",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "111111000000116002"
      },
      "message": "record not deleted",
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failed

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

### Status `404` — `application/json` — InvalidUrlPattern

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalError

Internal server error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
