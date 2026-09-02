Error response when the name has invalid value in custom_parameters.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.custom_parameters[*].name"
      },
      "status": "error"
    }
  ]
}
```
