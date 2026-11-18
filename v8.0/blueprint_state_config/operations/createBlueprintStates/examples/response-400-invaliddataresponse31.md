INVALID_DATA Error for the Details Field

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "details",
        "maximum_length": 3,
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
