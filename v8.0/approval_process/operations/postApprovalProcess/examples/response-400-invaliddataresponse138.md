Invalid data type error for the fields array after record rejection

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "fields",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.fields"
      },
      "status": "error"
    }
  ]
}
```
