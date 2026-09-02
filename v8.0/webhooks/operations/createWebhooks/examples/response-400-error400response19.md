Error response when type value is not among the accepted values.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "type",
      "supported_values": [
        "form_data",
        "raw"
      ],
      "json_path": "$.webhooks[*].body.type"
    },
    "status": "error"
  }
}
```
