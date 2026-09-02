Error response when the module has invalid data type in webhooks.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].module"
      },
      "status": "error"
    }
  ]
}
```
