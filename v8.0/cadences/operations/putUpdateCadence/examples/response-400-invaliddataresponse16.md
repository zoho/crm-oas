Invalid field data value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "period",
        "json_path": "$.cadences[0].follow_ups[1].execute_after.period",
        "supported_values": [
          "minutes",
          "hours",
          "business_hours",
          "days",
          "business_days",
          "months"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
