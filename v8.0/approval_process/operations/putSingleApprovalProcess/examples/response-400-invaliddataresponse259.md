Invalid data type error for a rejection action module

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "module",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.module"
      },
      "status": "error"
    }
  ]
}
```
