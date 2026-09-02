Invalid execution period value error

```json
{
  "cadences": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "period",
        "json_path": "$.cadences[0].execution_details.execute_every.period",
        "supported_values": [
          "immediately",
          "hours",
          "days",
          "weeks"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
