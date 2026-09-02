INVALID_DATA unsupported value error for body.type field

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
