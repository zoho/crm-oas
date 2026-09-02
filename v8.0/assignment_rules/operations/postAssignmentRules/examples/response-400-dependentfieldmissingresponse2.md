Error response with code DEPENDENT_FIELD_MISSING: Dependent field is missing (Field: resource)

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
        "api_name": "resource",
        "json_path": "$.assignment_rules[*].rule_entries[*].assign_to.assignment_rules.rule_entries.assign_to.resource"
      },
      "status": "error"
    }
  ]
}
```
