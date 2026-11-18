Error response with code INVALID_DATA: Invalid data (Field: escalate_to)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "escalate_to",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details.escalate_to"
      },
      "status": "error"
    }
  ]
}
```
