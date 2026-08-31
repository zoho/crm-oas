Error response when name value exceeds maximum length in module_parameters.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 10,
        "json_path": "$.webhooks[*].headers.module_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```
