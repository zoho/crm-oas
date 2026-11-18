INVALID_DATA error for an escalation action type exceeding its length limit

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 20,
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
