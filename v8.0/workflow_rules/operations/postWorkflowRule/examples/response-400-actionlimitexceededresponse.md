Error response with code LIMIT_EXCEEDED: per-type action limit exceeded in instant/scheduled actions

```json
{
  "workflow_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "actions",
        "limit": 5,
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions"
      },
      "message": "actions limit exceeded",
      "status": "error"
    }
  ]
}
```
