Error response when value exceeds maximum length for module_parameters.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 15,
        "json_path": "$.webhooks[*].headers.module_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```
