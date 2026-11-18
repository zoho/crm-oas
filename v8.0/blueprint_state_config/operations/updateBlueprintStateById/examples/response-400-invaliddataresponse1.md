INVALID_DATA Error for an Unsupported Period Value

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "period",
        "json_path": "$.states[0].state_escalation.trigger_details[0].period",
        "supported_values": [
          "days",
          "hours",
          "minutes"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
