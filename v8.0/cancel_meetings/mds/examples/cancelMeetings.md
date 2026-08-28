# Examples: cancelMeetings

**POST /Events/{event}/actions/cancel**

## Request examples

### `application/json` — RequestBodyExample

```json
{
  "data": [
    {
      "send_cancelling_mail": false
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — CancelMeetingSuccessResponse

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4876876000001563018"
      },
      "message": "The event is successfully cancelled",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — ErrorResponse

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The request method is incorrect.",
  "status": "error"
}
```

### Status `401` — `application/json` — ForbiddenErrorResponse

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionErrorResponse

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Edit_Events"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```
