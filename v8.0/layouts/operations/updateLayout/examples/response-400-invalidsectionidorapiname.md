Section missing required ID or display label

```json
{
  "layouts": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].id"
          },
          {
            "api_name": "display_label",
            "json_path": "$.layouts[0].sections[0].display_label"
          }
        ]
      },
      "message": "should contain either id or display_label",
      "status": "error"
    }
  ]
}
```
