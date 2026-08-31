Error response when type value is not among the accepted values in authentication.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "supported_values": [
        "general"
      ],
      "json_path": "$.webhooks[*].authentication.type"
    },
    "status": "error"
  }
}
```
