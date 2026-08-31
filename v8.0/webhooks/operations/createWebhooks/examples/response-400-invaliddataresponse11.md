Error response when the headers have invalid data type in webhooks.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "headers",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].headers"
      },
      "status": "error"
    }
  ]
}
```
