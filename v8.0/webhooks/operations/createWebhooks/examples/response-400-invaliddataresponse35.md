Error response when authentication data type is invalid.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "authentication",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].authentication"
      },
      "status": "error"
    }
  ]
}
```
