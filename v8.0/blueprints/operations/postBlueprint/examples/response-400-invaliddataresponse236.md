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
          "minutes",
          "business_days",
          "business_hours"
        ],
        "json_path": "$.blueprints[*].states[*].state_escalation.period"
      },
      "status": "error"
    }
  ]
}
```
