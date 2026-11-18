Missing required layout object in a final approval action

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "layout",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.layout"
      },
      "status": "error"
    }
  ]
}
```
