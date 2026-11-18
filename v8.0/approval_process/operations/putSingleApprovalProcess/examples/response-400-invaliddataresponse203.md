Error when an action type is not a supported value

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
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
