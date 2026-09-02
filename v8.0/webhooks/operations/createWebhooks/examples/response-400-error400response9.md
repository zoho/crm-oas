Error response when module ID exceeds the maximum allowed length.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "id",
      "maximum_length": 19,
      "json_path": "$.webhooks[*].module.id"
    },
    "status": "error"
  }
}
```
