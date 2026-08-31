Error response: AMBIGUITY_DUE_TO  - tag name and id resolve to different tags

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "name",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.tags[0].name"
          },
          {
            "api_name": "id",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.tags[0].id"
          }
        ]
      },
      "message": "Ambiguity during processing",
      "status": "error"
    }
  ]
}
```
