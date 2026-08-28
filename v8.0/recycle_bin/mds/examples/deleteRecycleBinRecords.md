# Examples: deleteRecycleBinRecords

**DELETE /settings/recycle_bin**

## Parameter examples

### `filters` (query) — ByModule

```json
"module:Leads"
```

## Response examples

### Status `200` — `application/json` — Success

```json
{
  "recycle_bin": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4794080000003267613"
      },
      "message": "record deleted",
      "status": "success"
    }
  ]
}
```

### Status `202` — `application/json` — Scheduled

```json
{
  "recycle_bin": [
    {
      "code": "SCHEDULED",
      "details": {
        "id": "4794080000003267613"
      },
      "message": "record has been scheduled for deletion",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — MultiStatusResponse

```json
{
  "recycle_bin": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "4794080000003274845"
      },
      "message": "record restored",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "id": "1000000000000"
      },
      "message": "the id given seems to be invalid",
      "status": "error"
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
