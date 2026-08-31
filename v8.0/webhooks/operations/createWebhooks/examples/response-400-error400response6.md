Error response for invalid data type in api_name.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "api_name",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].module.api_name"
    },
    "status": "error"
  }
}
```
