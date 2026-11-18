MANDATORY_NOT_FOUND error for the missing approver_stages field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "approver_stages",
        "json_path": "$.approval_process[*].rules[*].approver_stages"
      },
      "status": "error"
    }
  ]
}
```
