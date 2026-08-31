Error response: INVALID_DATA  - tags array is empty

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "tags",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.tags"
      },
      "message": "Tags array cannot be empty",
      "status": "error"
    }
  ]
}
```
