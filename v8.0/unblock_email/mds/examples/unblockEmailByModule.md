# Examples: unblockEmailByModule

**POST /{module}/actions/unblock_email**

## Request examples

### `application/json` — UnblockMultipleEmails

An example response to unblock emails for multiple records in a module.

```json
{
  "ids": [
    "5545974000000224001",
    "5545974000000224002"
  ],
  "unblock_fields": [
    "Email"
  ]
}
```

## Response examples

### Status `200` — `application/json` — SuccessfulUnblock

An example response of successful bulk email unblock request.

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "5545974000000224001"
      },
      "message": "Email unblocked successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidToken

An example response for invalid OAuth token error.

```json
{
  "status": "error",
  "code": "INVALID_TOKEN",
  "message": "invalid oauth token",
  "details": {}
}
```
