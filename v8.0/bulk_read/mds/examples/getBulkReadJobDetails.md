# Examples: getBulkReadJobDetails

**GET /read/{jobId}**

## Response examples

### Status `200` — `application/json` — Example1

Bulk read job details

```json
{
  "data": [
    {
      "id": "string",
      "operation": "string",
      "state": "COMPLETED",
      "query": {
        "module": {
          "api_name": "string",
          "id": "string"
        },
        "page": 0
      },
      "created_by": {
        "name": "string",
        "id": "string"
      },
      "created_time": "2023-01-01T00:00:00Z",
      "file_type": "csv"
    }
  ]
}
```

### Status `404` — `application/json` — Example1

Job not found error

```json
{
  "code": "RESOURCE_NOT_FOUND",
  "details": {
    "resource": "string"
  },
  "message": "string",
  "status": "error"
}
```
