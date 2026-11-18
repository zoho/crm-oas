INVALID_DATA error when the module id has an invalid data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.module.id"
      },
      "status": "error"
    }
  ]
}
```
