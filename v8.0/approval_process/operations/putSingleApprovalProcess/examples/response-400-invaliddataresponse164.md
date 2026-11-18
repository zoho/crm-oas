INVALID_DATA error for an on_approve list exceeding five entries

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
