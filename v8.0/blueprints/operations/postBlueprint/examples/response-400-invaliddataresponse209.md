Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "field_updates",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "sms",
          "whatsapp",
          "tasks",
          "create_record",
          "add_meeting",
          "schedule_call",
          "convert",
          "webhooks",
          "functions"
        ],
        "json_path": "$.blueprints[*].transitions[*].actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
