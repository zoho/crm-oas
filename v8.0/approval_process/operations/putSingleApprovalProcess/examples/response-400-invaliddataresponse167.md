Unsupported value for the on_approve action type

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
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve[*].type"
      },
      "status": "error"
    }
  ]
}
```
