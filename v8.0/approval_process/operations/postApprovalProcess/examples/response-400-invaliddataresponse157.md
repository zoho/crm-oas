Invalid data error for the on_approve field violating its length constraint

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "on_approve",
        "minimum_length": -2,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve"
      },
      "status": "error"
    }
  ]
}
```
