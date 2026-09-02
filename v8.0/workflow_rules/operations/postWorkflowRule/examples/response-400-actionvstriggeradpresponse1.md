Error response with code AMBIGUITY_DURING_PROCESSING: action not supported for this trigger

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "type",
            "json_path": "$.workflow_rules[0].execute_when.type"
          },
          {
            "api_name": "type",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].type"
          }
        ]
      },
      "message": "action not supported for this trigger",
      "status": "error"
    }
  ]
}
```
