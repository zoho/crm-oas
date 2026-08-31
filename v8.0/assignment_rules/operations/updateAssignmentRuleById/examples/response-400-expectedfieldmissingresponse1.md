Error response with code EXPECTED_FIELD_MISSING: One of the required fields is missing

```json
{
  "assignment_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.assignment_rules[*].rule_entries[*].id"
          },
          {
            "api_name": "assign_to",
            "json_path": "$.assignment_rules[*].rule_entries[*].assignment_rules.rule_entries.assign_to"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
