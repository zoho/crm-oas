Dependent field missing in criteria

```json
{
  "territories": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.territories[0].account_rule_criteria.field"
        },
        "api_name": "comparator",
        "json_path": "$.territories[0].account_rule_criteria.comparator"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```
