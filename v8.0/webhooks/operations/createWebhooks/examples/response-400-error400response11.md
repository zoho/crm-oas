Error response when raw_data_content exceeds the maximum allowed length.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "raw_data_content",
      "maximum_length": 500,
      "json_path": "$.webhooks[*].body.raw_data_content"
    },
    "status": "error"
  }
}
```
