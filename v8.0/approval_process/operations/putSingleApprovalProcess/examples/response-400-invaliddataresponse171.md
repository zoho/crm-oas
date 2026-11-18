INVALID_DATA error when an on_approve action id exceeds its maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve[*].id"
      },
      "status": "error"
    }
  ]
}
```
