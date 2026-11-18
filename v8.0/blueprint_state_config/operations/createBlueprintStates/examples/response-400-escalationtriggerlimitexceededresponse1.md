LIMIT_EXCEEDED Error When Escalation Trigger Actions Exceed the Configured Limit

```json
{
  "states": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "action_type": "tasks",
        "api_name": "actions",
        "limit": 5,
        "json_path": "$.states[0].state_escalation.trigger_details[0]",
        "configured_count": 6
      },
      "message": "Action Limit Exceeds",
      "status": "error"
    }
  ]
}
```
