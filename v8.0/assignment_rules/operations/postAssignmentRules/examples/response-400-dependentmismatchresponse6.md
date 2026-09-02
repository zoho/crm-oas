Error response with code DEPENDENT_MISMATCH: A Requester profile users are not allowed to be the owner of a record. (Field: ID)

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
        "json_path": "$.assignment_rules[0].rule_entries[i].assign_to.resources[i].id"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```
