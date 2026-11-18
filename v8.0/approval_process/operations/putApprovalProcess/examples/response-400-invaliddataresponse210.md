INVALID_DATA error when the layout action id is not a bigint

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.layout.id"
      },
      "status": "error"
    }
  ]
}
```
