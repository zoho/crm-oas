Error response with code INVALID_DATA: Invalid data (Field: period)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "period",
        "supported_values": [
          "days",
          "hours",
          "minutes"
        ],
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].period"
      },
      "status": "error"
    }
  ]
}
```
