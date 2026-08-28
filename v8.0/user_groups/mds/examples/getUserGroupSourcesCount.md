# Examples: getUserGroupSourcesCount

**GET /settings/user_groups/{group}/actions/sources_count**

## Response examples

### Status `200` — `application/json` — Success

Successful response with source counts

```json
{
  "sources_count": [
    {
      "territories": 1,
      "roles": 2,
      "users": {
        "inactive": 0,
        "deleted": 0,
        "active": 2
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid group ID in request URL

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidData

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```
