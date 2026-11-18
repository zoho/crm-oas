INVALID_DATA Error for an Unsupported Action Type Value

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.states[0].state_escalation.trigger_details[0].actions[0].type",
        "supported_values": [
          "sla",
          "email_notifications",
          "tasks",
          "field_updates",
          "webhooks",
          "functions",
          "circuits",
          "whatsapp",
          "sms"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
