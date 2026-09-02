INVALID_DATA error for unsupported merge field in headers

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "value",
        "json_path": "$.webhooks[0].headers.module_parameters[0].value"
      },
      "message": "Unsupported fields are present",
      "status": "error"
    }
  ]
}
```
