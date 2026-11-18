INVALID_DATA Error for Unsupported Type Field Value

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
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
        ],
        "json_path": "$.states[*].state_escalation.trigger_details[*].actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
