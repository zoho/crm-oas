# Examples: getRecycleBinRecords

**GET /settings/recycle_bin**

## Response examples

### Status `200` — `application/json` — RecycleBinListSample

Sample paginated Recycle Bin list

```json
{
  "recycle_bin": [
    {
      "display_name": "John Doe",
      "deleted_time": "2025-10-22T14:12:00Z",
      "owner": {
        "name": "Jane Smith",
        "id": "789"
      },
      "module": {
        "api_name": "Leads"
      },
      "deleted_by": {
        "name": "Admin",
        "id": "456"
      },
      "id": "12345"
    }
  ],
  "info": {
    "per_page": 20,
    "count": 1,
    "page": 1,
    "more_records": false
  }
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
