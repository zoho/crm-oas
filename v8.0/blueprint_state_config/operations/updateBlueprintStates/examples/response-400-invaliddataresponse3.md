INVALID_DATA Error for an Invalid Period Field Value

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "period",
        "json_path": "$.states[0].state_escalation.period",
        "supported_values": [
          "days",
          "hours",
          "minutes",
          "business_days",
          "business_hours"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
