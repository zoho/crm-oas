Duplicate parameter name in module or custom parameters.

```json
{
  "webhooks": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[0].headers.module_parameters[1].name"
      },
      "message": "duplicate parameter name found",
      "status": "error"
    }
  ]
}
```
