Error response with code DEPENDENT_FIELD_MISSING: Dependent field is missing (Field: resources)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].type"
        },
        "api_name": "resources",
        "json_path": "$.assignment_rules[*].rule_entries[*].followup_actions[*].assignment_rules.rule_entries.followup_actions.resources"
      },
      "status": "error"
    }
  ]
}
```
