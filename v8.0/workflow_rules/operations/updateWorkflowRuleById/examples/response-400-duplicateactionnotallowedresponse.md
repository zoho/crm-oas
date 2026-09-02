INVALID_DATA error when a duplicate action type is detected

```json
{
  "workflow_rules": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "actions",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0]"
      },
      "message": "Duplicate action not allowed",
      "status": "error"
    }
  ]
}
```
