Error response for invalid data type in module_parameters.

```json
{
  "webhooks": {
    "code": "INVALID_DATA",
    "message": "Invalid data type",
    "details": {
      "api_name": "module_parameters",
      "expected_data_type": "jsonarray",
      "json_path": "$.webhooks[*].headers.module_parameters"
    },
    "status": "error"
  }
}
```
