Error response for missing related_module when feature_type is kiosk

```json
{
  "webhooks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "feature_type",
          "json_path": "$.webhooks[0].feature_type"
        },
        "api_name": "related_module",
        "json_path": "$.webhooks[0].related_module"
      },
      "message": "Webhook action related module missing for kiosk feature",
      "status": "error"
    }
  ]
}
```
