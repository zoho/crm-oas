Error response when the value of name exceeds maximum length in custom_parameters.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 6,
        "json_path": "$.webhooks[*].headers.custom_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```
