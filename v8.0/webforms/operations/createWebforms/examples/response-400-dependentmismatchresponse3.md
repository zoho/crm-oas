DEPENDENT_MISMATCH error for unsupported URL-based analytics in current edition

```json
{
  "webforms": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.webforms[0].type"
        },
        "api_name": "url_analytics_enabled",
        "json_path": "$.webforms[0].analytics_data.url_analytics_enabled"
      },
      "message": "URL based Analytics is not supported for portal forms",
      "status": "error"
    }
  ]
}
```
