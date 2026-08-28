# Examples: unshareBulkEmails

**POST /{moduleApiName}/actions/unshare_emails**

## Parameter examples

### `moduleApiName` (path) — Example

```json
"Leads"
```

## Request examples

### `application/json` — BulkUnshare

Sample bulk email unshare request

```json
{
  "ids": [
    "1234567890",
    "0987654321"
  ]
}
```

## Response examples

### Status `207` — `application/json` — InvalidData

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
