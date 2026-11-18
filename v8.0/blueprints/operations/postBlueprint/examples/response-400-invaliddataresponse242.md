Error response with code INVALID_DATA: Invalid data (Field: period)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "period",
        "maximum_length": 10,
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].period"
      },
      "status": "error"
    }
  ]
}
```
