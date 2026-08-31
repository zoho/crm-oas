Mixed result with one field created successfully and one rejected with INVALID_DATA

```json
{
  "fields": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1947368000002460003"
      },
      "message": "field created",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "data_type",
        "json_path": "$.fields[1].data_type"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
