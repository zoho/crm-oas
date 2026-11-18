MANDATORY_NOT_FOUND error for a missing approver field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "approver",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver"
      },
      "message": "The required data missing",
      "status": "error"
    }
  ]
}
```
