INVALID_DATA unsupported value error for body.format field

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data",
    "details": {
      "api_name": "format",
      "supported_values": [
        "JSON",
        "XML",
        "Text",
        "HTML"
      ],
      "json_path": "$.webhooks[*].body.format"
    },
    "status": "error"
  }
}
```
