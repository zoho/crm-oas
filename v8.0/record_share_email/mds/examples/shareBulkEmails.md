# Examples: shareBulkEmails

**POST /{moduleApiName}/actions/share_emails**

## Parameter examples

### `moduleApiName` (path) — Example

```json
"Leads"
```

## Request examples

### `application/json` — BulkShare

Sample bulk email share request

```json
{
  "ids": [
    "1234567890",
    "0987654321"
  ]
}
```

## Response examples

### Status `200` — `application/json` — Success

Successful bulk email sharing

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1234567890"
      },
      "message": "Successfully shared",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — MultiStatus

Partial success - mixed sharing results

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1234567890"
      },
      "message": "Successfully shared",
      "status": "success"
    },
    {
      "code": "ALREADY_SHARED",
      "details": {
        "id": "0987654321"
      },
      "message": "Emails are already shared to the colleagues already",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

INVALID_DATA - invalid record ID

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "3249415000000548012"
      },
      "message": "the related id given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — PermissionDenied

NO_PERMISSION - permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "ZohoCRM.modules.Leads.DELETE"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
