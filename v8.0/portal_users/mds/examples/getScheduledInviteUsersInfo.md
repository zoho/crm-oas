# Examples: getScheduledInviteUsersInfo

**GET /{module}/actions/portal_invite**

## Response examples

### Status `200` — `application/json` — Example1

Scheduled invitation job with completion status

```json
{
  "portal_invite": [
    {
      "data": [
        {
          "details": {
            "id": "1234567890"
          },
          "code": "SUCCESS",
          "message": "An Invite has been sent to the personality.",
          "status": "success"
        }
      ],
      "job_id": "1234567",
      "status": "completed"
    }
  ]
}
```

### Status `400` — `application/json` — ApiNotSupported

Error when the API runs in a sandbox environment

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "unsupported_environment": "sandbox"
  },
  "message": "api not supported in sandbox",
  "status": "error"
}
```
