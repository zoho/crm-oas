INVALID_DATA error for actions exceeding the maximum length of 1

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions"
      },
      "status": "error"
    }
  ]
}
```
