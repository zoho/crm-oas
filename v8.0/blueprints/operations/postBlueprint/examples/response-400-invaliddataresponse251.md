INVALID_DATA error for a details value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "details",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
