Error response with code DEPENDENT_FIELD_MISSING: Missing Associated Action Id

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].type"
        },
        "api_name": "id",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].id"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
