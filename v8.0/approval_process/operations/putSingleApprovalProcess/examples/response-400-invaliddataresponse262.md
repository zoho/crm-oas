INVALID_DATA error for a module id exceeding the maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.module.id"
      },
      "status": "error"
    }
  ]
}
```
