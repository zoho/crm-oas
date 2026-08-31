Error response when feature_type has invalid data type.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "feature_type",
        "expected_data_type": "text",
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```
