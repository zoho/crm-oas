Invalid data error for name over 200 characters in rejection actions

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].name"
      },
      "status": "error"
    }
  ]
}
```
