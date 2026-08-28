# Examples: emptyRecycleBin

**POST /settings/recycle_bin/actions/empty**

## Response examples

### Status `200` — `application/json` — ImmediateSuccess

Recycle Bin emptied immediately

```json
{
  "code": "SUCCESS",
  "details": {},
  "message": "recyclebin is cleared",
  "status": "success"
}
```

### Status `202` — `application/json` — ScheduledDeletion

Empty Recycle Bin scheduled as background job

```json
{
  "code": "SCHEDULED",
  "details": {},
  "message": "Empty bin action has been scheduled",
  "status": "success"
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
  "message": "Please check if the URL trying to access is a correct one",
  "details": {}
}
```
