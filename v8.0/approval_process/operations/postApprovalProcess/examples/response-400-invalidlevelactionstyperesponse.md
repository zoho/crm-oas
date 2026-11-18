Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "field_updates"
        ],
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].actions.actions_per_approval[0].actions[0].type"
      },
      "status": "error"
    }
  ]
}
```
