MANDATORY_NOT_FOUND error for the missing **module** field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "module",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.module"
      },
      "status": "error"
    }
  ]
}
```
