INVALID_DATA error for state escalation details exceeding the maximum count

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "state_escalation",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].states[*].state_escalation"
      },
      "status": "error"
    }
  ]
}
```
