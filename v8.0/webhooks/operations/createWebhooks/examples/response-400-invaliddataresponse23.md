Error response when description has wrong data type in webhooks.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].description"
      },
      "status": "error"
    }
  ]
}
```
