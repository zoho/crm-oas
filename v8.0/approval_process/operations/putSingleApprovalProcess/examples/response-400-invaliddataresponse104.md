INVALID_DATA error for an invalid approver value in the Approval Process

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "approver",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver"
      },
      "status": "error"
    }
  ]
}
```
