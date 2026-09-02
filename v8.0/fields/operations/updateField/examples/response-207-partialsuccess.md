Partial success - one field updated, one failed

```json
{
  "fields": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "1947368000002460003"
      },
      "message": "field updated",
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
