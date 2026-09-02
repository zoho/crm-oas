Error response when type value exceeds the maximum allowed length in authentication.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "maximum_length": 7,
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```
