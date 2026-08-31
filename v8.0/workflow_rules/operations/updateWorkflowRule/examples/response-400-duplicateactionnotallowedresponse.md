Error response with code INVALID_DATA: Duplicate action not allowed

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
