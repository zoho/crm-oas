INVALID_DATA: type field of on-approval-trigger action not in supported values

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "tasks"
        ],
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger[*].type"
      },
      "status": "error"
    }
  ]
}
```
