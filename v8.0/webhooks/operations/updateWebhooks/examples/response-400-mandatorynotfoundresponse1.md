MANDATORY_NOT_FOUND error for missing required field

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "value",
        "json_path": "$.webhooks[0].headers.custom_parameters[0].value"
      },
      "message": "the given parameter is invalid, specify both name and value",
      "status": "error"
    }
  ]
}
```
