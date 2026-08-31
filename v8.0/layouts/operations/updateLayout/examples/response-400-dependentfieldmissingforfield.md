Field ID or field_label absent during a field operation

```json
{
  "layouts": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.layouts[0].sections[0].fields[0].id"
          },
          {
            "api_name": "field_label",
            "json_path": "$.layouts[0].sections[0].fields[0].field_label"
          }
        ]
      },
      "message": "should contain either id or field_label",
      "status": "error"
    }
  ]
}
```
