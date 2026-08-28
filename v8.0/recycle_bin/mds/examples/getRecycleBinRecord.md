# Examples: getRecycleBinRecord

**GET /settings/recycle_bin/{recordId}**

## Parameter examples

### `recordId` (path) — Example1

```json
"4876876000007018006"
```

## Response examples

### Status `200` — `application/json` — SingleRecordExample

Recycle Bin record metadata

```json
{
  "recycle_bin": [
    {
      "owner": {
        "name": "Patricia Boyle",
        "id": "4876876000000327001"
      },
      "module": {
        "api_name": "Leads",
        "id": "4876876000000002175"
      },
      "deleted_by": {
        "name": "Patricia Boyle",
        "id": "4876876000000327001"
      },
      "id": "4876876000007018006",
      "display_name": "John Doe",
      "deleted_time": "2024-07-23T15:37:52+05:30"
    }
  ]
}
```

### Status `400` — `application/json` — Error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "comparator",
    "json_path": "$.comparator",
    "param_name": "filters"
  },
  "message": "Please provide a valid comparator",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

```json
{
  "status": "error",
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "Unauthorized",
  "details": {}
}
```

### Status `404` — `application/json` — InvalidUrlPattern

```json
{
  "status": "error",
  "code": "INVALID_URL_PATTERN",
  "message": "The request URL is incorrect.",
  "details": {}
}
```
