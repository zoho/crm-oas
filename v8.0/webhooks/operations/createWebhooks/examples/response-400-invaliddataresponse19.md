Error response when the value has wrong data type in custom_parameters.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].headers.custom_parameters[*].value"
      },
      "status": "error"
    }
  ]
}
```
