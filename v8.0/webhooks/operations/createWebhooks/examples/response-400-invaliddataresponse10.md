Error response for invalid connection_name.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "connection_name",
        "json_path": "$.webhooks[0].authentication.connetion_name"
      },
      "message": "Please provide valid connection name",
      "status": "error"
    }
  ]
}
```
