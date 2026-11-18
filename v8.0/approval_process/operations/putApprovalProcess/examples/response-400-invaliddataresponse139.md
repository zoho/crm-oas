INVALID_DATA error for invalid data type in the id field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting.fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
