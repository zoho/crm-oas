Field value is not valid for its schema type

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
