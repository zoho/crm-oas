Error response for invalid data type in authentication type.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "type",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```
