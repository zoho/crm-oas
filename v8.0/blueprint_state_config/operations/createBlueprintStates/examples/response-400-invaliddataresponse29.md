INVALID_DATA Error for Actions Field Exceeding Maximum Length

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions",
        "maximum_length": 5,
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions"
      },
      "status": "error"
    }
  ]
}
```
