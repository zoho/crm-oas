Error response for invalid data type in module ID.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "id",
      "expected_data_type": "bigint",
      "json_path": "$.webhooks[*].module.id"
    },
    "status": "error"
  }
}
```
