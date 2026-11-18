INVALID_DATA Error for State Escalation Action Name Field

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 4,
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].details.name"
      },
      "status": "error"
    }
  ]
}
```
