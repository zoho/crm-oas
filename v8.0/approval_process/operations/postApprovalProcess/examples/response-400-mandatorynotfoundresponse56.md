MANDATORY_NOT_FOUND error when the required layout field is missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
