Error response with code DEPENDENT_MISMATCH: Invalid data (Field: ID)

```json
{
  "assignment_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "param_name": "module"
        },
        "api_name": "id",
        "json_path": "$.assignment_rules[0].rule_entries[*].assign_to.resources[*].id"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```
