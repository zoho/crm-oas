# Examples: shareEmails

**POST /{moduleApiName}/{id}/actions/share_emails**

## Parameter examples

### `moduleApiName` (path) — Example

```json
"Leads"
```

## Response examples

### Status `200` — `application/json` — Success

Successful email sharing

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

### Status `400` — `application/json` — InvalidData

INVALID_DATA - invalid record ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "the related id given seems to be invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — PermissionDenied

NO_PERMISSION - permission denied

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "ZohoCRM.modules.Leads.PUT"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
