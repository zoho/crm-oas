Error response: INVALID_DATA  - tag name/id does not exist for the module

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "tags",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.tags[0]"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
