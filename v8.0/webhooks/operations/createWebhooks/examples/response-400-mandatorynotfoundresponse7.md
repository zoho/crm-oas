Error response when the feature_type is missing.

```json
{
  "webhooks": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "feature_type",
        "json_path": "$.webhooks[*].feature_type"
      },
      "status": "error"
    }
  ]
}
```
