Field value type mismatch in criteria

```json
{
  "territories": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "field",
          "json_path": "$.territories[0].account_rule_criteria.field"
        },
        "api_name": "value",
        "json_path": "$.territories[0].account_rule_criteria.value",
        "expected_data_type": "integer"
      },
      "message": "The value is not compatible with the given field",
      "status": "error"
    }
  ]
}
```
