# Examples: unblockEmailById

**POST /{module}/{id}/actions/unblock_email**

## Request examples

### `application/json` — UnblockSingleEmail

An example to unblock the primary email field for a single record.

```json
{
  "unblock_fields": [
    "Email"
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulSingleUnblock

An example response of successful email unblock for a single record.

```json
{
  "code": "SUCCESS",
  "details": {
    "id": "5545974000000224001"
  },
  "message": "Email unblocked successfully",
  "status": "success"
}
```

### Status `400` — `application/json` — InvalidTokenError

An example response of invalid OAuth token.

```json
{
  "status": "error",
  "code": "INVALID_TOKEN",
  "message": "invalid oauth token",
  "details": {}
}
```
