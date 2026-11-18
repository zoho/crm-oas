INVALID_DATA error when the based_on_field id is not a bigint

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field.id"
      },
      "status": "error"
    }
  ]
}
```
