INVALID_DATA error for an invalid ID value data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.module.id"
      },
      "status": "error"
    }
  ]
}
```
