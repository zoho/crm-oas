INVALID_DATA error for an action type value outside the supported list

```json
{
  "blueprints": [
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
        "json_path": "$.blueprints[*].states[*].state_escalation.trigger_details[*].actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
