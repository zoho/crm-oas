Error response: AMBIGUITY_DUE_TO  - notify_to field id and api_name mismatch

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.notify_to.notify_fields.fields[0].id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.notify_to.notify_fields.fields[0].api_name"
          }
        ]
      },
      "message": "Ambiguity during processing",
      "status": "error"
    }
  ]
}
```
