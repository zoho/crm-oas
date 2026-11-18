INVALID_DATA error for an invalid module object in a rejection action

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "module",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.module"
      },
      "status": "error"
    }
  ]
}
```
