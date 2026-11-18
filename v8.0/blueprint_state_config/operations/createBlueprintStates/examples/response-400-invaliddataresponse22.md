INVALID_DATA Error for Unsupported Period Field Value

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
        "json_path": "$.states[*].state_escalation.trigger_details[*].period"
      },
      "status": "error"
    }
  ]
}
```
