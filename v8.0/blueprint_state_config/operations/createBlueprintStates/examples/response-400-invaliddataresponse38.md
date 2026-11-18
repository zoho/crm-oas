INVALID_DATA Error for Invalid Action Type Field

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 20,
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
