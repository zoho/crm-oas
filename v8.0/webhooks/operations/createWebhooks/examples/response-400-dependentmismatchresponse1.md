Error response when authentication type is incompatible with connection_name.

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "connection_name",
          "json_path": "$.webhooks[0].authentication.connetion_name"
        },
        "api_name": "type",
        "json_path": "$.webhooks[0].authentication.type"
      },
      "message": "provide appropriate authentication type",
      "status": "error"
    }
  ]
}
```
