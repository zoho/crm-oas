Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "scoring_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "status": "error",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.id"
          }
        ]
      },
      "message": "Specify atleast one field"
    }
  ]
}
```
