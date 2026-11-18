INVALID_DATA error for unsupported period field value

```json
{
  "states": [
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
        "json_path": "$.states[*].state_escalation.period"
      },
      "status": "error"
    }
  ]
}
```
