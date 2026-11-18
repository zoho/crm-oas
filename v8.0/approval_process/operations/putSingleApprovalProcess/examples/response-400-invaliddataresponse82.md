Invalid data type error for the id field in record modification

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
