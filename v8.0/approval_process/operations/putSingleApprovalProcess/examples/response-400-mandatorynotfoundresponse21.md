MANDATORY_NOT_FOUND error for a missing stage name

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].name"
      },
      "status": "error"
    }
  ]
}
```
