Error response with code DEPENDENT_MISMATCH: Dependent Field is not matching (Field: module)

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "module_selection",
          "json_path": "$.workflow_rules[0].conditions[0].criteria_details.relational_criteria.module_selection"
        },
        "api_name": "module",
        "json_path": "$.workflow_rules[0].conditions[0].criteria_details.relational_criteria.module"
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```
