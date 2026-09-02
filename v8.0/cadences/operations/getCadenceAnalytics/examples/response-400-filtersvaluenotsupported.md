Unsupported filter value error

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.field.api_name"
    },
    "api_name": "value",
    "json_path": "$.value",
    "supported_values": [
      "tasks",
      "schedule_call",
      "email_notifications",
      "whatsapp_message_notification"
    ],
    "param_name": "filters"
  },
  "message": "The value given seems to be invalid",
  "status": "error"
}
```
