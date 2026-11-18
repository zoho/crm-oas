MANDATORY_NOT_FOUND error for a missing id in an on-approval action

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger[*].id"
      },
      "status": "error"
    }
  ]
}
```
