MANDATORY_NOT_FOUND error when the required name field is missing

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
