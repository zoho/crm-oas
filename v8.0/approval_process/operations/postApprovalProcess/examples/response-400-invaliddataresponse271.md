Invalid data type error for the rejection action ID expected as bigint

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].id"
      },
      "status": "error"
    }
  ]
}
```
