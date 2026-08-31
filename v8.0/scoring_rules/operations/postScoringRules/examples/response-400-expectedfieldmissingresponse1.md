Error response with code EXPECTED_FIELD_MISSING: field_rules or signal_rules is expected(For leads and contacts)

```json
{
  "scoring_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "field_rules",
            "json_path": "$.scoring_rules[0].field_rules"
          },
          {
            "api_name": "signal_rules",
            "json_path": "$.scoring_rules[0].signal_rules"
          }
        ]
      },
      "message": "field_rules or signal_rules is expected",
      "status": "error"
    }
  ]
}
```
