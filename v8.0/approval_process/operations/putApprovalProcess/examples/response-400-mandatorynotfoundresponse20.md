MANDATORY_NOT_FOUND error when the required approver_stages field is missing

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
