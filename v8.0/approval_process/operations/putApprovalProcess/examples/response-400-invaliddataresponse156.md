INVALID_DATA: type field of on-approval-trigger action has wrong data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger[*].type"
      },
      "status": "error"
    }
  ]
}
```
