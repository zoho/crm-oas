Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: details)

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
        "api_name": "details",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
