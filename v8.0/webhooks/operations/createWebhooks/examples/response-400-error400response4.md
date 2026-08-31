Error response for invalid data type in custom_parameters.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "custom_parameters",
      "expected_data_type": "jsonarray",
      "json_path": "$.webhooks[*].headers.custom_parameters"
    },
    "status": "error"
  }
}
```
