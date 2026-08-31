Error response when the feature_type exceeds maximum length.

```json
{
  "webhooks": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "feature_type",
        "maximum_length": 20,
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```
