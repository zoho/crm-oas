Invalid data type error for the on_approve field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "on_approve",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve"
      },
      "status": "error"
    }
  ]
}
```
