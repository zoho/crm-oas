Error response when type value exceeds the maximum allowed length.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "maximum_length": 10,
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```
