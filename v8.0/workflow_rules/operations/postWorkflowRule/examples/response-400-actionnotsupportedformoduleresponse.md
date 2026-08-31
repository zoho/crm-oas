Error response with code AMBIGUITY_DURING_PROCESSING: action type not supported for module, or action's bound module does not match relational_criteria.module

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "module",
            "json_path": "$.workflow_rules[*].module"
          },
          {
            "api_name": "type",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].type"
          }
        ]
      },
      "message": "action not supported for this module",
      "status": "error"
    }
  ]
}
```
