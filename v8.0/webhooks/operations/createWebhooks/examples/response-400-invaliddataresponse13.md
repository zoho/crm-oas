Error response when the name key has invalid data type in module_parameters.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.module_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```
