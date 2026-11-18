DEPENDENT_MISMATCH error when enabling URL-based analytics without prerequisite condition met

```json
{
  "webforms": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "location_url",
          "json_path": "$.webforms[0].location_url"
        },
        "api_name": "url_analytics_enabled",
        "json_path": "$.webforms[0].analytics_data.url_analytics_enabled"
      },
      "message": "url based analytics can be enabled only when more than one location_url is configured",
      "status": "error"
    }
  ]
}
```
