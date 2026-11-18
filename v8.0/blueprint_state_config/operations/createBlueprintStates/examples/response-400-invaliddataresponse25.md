INVALID_DATA Error for Invalid execute_type Field Value

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "execute_type",
        "supported_values": [
          "before",
          "on",
          "after"
        ],
        "json_path": "$.states[*].state_escalation.trigger_details[*].execute_type"
      },
      "status": "error"
    }
  ]
}
```
