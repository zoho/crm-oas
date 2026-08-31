Error response: MANDATORY_NOT_FOUND  - chat notification message missing

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "message",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.message"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```
