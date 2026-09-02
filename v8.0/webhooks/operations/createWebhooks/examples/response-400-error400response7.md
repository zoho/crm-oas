Error response when api_name exceeds the maximum allowed length.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "api_name",
      "maximum_length": 5,
      "json_path": "$.webhooks[*].module.api_name"
    },
    "status": "error"
  }
}
```
