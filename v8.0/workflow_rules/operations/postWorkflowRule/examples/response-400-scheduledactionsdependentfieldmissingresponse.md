Error response with code DEPENDENT_FIELD_MISSING: unit/period is missing

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "execute_after",
          "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].execute_after"
        },
        "api_name": "unit",
        "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].execute_after.unit"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
