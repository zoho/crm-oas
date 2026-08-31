MANDATORY_NOT_FOUND error for missing parameter name or value

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.webhooks[0].headers.module_parameters[0].name"
      },
      "message": "the given parameter is invalid, specify both name and value",
      "status": "error"
    }
  ]
}
```
