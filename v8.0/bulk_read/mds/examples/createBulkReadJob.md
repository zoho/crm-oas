# Examples: createBulkReadJob

**POST /read**

## Request examples

### `application/json` — Example1

Create bulk read job

```json
{
  "query": {
    "module": {
      "api_name": "string"
    }
  }
}
```

## Response examples

### Status `201` — `application/json` — Example1

Bulk read job created

```json
{
  "data": [
    {
      "status": "success",
      "code": "ADDED_SUCCESSFULLY",
      "message": "Added successfully.",
      "details": {
        "id": "string",
        "operation": "read",
        "state": "COMPLETED",
        "created_by": {
          "id": "string"
        },
        "created_time": "2023-01-01T00:00:00Z"
      }
    }
  ],
  "info": {}
}
```

### Status `400` — `application/json` — Example1

Invalid request error

```json
{
  "code": "REQUEST_BODY_NOT_SUPPORTED",
  "details": {},
  "message": "string",
  "status": "error"
}
```
