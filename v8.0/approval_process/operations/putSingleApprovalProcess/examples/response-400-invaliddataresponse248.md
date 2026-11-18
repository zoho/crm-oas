INVALID_DATA error: unsupported value for a rejection action type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "tasks",
          "email_notifications",
          "functions",
          "field_updates",
          "create_record"
        ],
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
