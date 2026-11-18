INVALID_DATA error for on_approval_trigger exceeding the maximum length of 5

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "on_approval_trigger",
        "maximum_length": 5,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger"
      },
      "status": "error"
    }
  ]
}
```
