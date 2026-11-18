Invalid data type error for ID expected as bigint after final approval

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
