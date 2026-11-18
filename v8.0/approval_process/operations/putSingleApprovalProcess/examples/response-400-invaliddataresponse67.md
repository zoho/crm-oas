Error response when the fields key has an invalid data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "fields",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.fields"
      },
      "status": "error"
    }
  ]
}
```
