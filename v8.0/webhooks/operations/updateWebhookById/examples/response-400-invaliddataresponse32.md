Field value has an incorrect data type for webhook update

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "http_method",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].http_method"
      },
      "status": "error"
    }
  ]
}
```
