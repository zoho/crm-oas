Error response

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.type"
        },
        "api_name": "resources",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.assignment_rules.rule_entries.assign_to.resources"
      },
      "status": "error"
    }
  ]
}
```
