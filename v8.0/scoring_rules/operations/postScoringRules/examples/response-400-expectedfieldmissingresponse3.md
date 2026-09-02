Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "scoring_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
