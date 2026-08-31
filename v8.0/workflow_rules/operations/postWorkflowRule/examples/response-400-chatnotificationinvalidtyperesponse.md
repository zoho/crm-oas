Error response: INVALID_DATA  - invalid notify_to type for chat notification

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.notify_to.type"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
