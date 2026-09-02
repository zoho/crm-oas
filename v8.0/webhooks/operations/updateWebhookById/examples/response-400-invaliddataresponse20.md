Field value has an incorrect data type in webhook schema

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
