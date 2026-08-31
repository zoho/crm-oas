Error response when body has invalid data type in webhooks.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "body",
        "expected_data_type": "jsonobject",
        "json_path": "$.webhooks[*].body"
      },
      "status": "error"
    }
  ]
}
```
