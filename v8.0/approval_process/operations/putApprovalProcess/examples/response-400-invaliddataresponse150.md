INVALID_DATA: id must be of bigint data type (Field: id)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
