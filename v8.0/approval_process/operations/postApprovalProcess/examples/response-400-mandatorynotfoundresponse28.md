MANDATORY_NOT_FOUND error for a missing approver field in an approver stage

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "approver",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver"
      },
      "status": "error"
    }
  ]
}
```
