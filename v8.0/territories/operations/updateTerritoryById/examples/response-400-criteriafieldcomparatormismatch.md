Field and comparator mismatch in criteria

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
        "api_name": "comparator",
        "json_path": "$.territories[0].account_rule_criteria.comparator",
        "supported_values": [
          "equal",
          "not_equal",
          "greater_than",
          "less_than"
        ]
      },
      "message": "The comparator is not compatible with the given field",
      "status": "error"
    }
  ]
}
```
