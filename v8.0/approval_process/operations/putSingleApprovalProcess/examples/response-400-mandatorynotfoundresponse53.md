Missing module object in a rejection action's details

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "module",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.module"
      },
      "status": "error"
    }
  ]
}
```
