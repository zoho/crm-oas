Invalid data type in the fields element returns an INVALID_DATA error

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "fields",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.fields"
      },
      "status": "error"
    }
  ]
}
```
