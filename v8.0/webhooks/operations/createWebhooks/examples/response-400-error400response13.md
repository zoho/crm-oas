Error response for invalid data type in body format

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "format",
      "expected_data_type": "text",
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```
