INVALID_DATA error: action id is not of expected data type bigint

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].id"
      },
      "status": "error"
    }
  ]
}
```
