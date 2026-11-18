Missing required type key in a final approval action

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
