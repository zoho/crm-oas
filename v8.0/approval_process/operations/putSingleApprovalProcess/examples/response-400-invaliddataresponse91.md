INVALID_DATA error when an approval action ID has an invalid data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions[*].id"
      },
      "status": "error"
    }
  ]
}
```
