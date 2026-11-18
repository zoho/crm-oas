MANDATORY_NOT_FOUND error for the missing actions field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "actions",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions"
      },
      "status": "error"
    }
  ]
}
```
