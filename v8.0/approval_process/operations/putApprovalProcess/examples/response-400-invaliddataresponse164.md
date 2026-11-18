Invalid data error for the on_approve field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "on_approve",
        "maximum_length": 5,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve"
      },
      "status": "error"
    }
  ]
}
```
