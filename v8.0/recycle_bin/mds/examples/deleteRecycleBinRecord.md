# Examples: deleteRecycleBinRecord

**DELETE /settings/recycle_bin/{recordId}**

## Response examples

### Status `200` — `application/json` — Success

```json
{
  "recycle_bin": [
    {
      "status": "success",
      "code": "SUCCESS",
      "message": "Deleted permanently",
      "details": {
        "id": "12345"
      }
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
