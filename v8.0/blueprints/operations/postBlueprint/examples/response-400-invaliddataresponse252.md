INVALID_DATA error for an escalate_to value with an invalid data type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "escalate_to",
        "expected_data_type": "jsonarray",
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].details.escalate_to"
      },
      "status": "error"
    }
  ]
}
```
