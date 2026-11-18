Invalid data type error for the id field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger[*].id"
      },
      "status": "error"
    }
  ]
}
```
