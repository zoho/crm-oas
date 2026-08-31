Error response with code DEPENDENT_MISMATCH: Invalid data (Field: type)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "param_name": "module"
        },
        "api_name": "type",
        "json_path": "$.assignment_rules[0].rule_entries[*].assign_to.resources[*].type"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```
