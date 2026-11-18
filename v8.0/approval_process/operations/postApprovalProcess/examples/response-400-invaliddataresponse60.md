Invalid data type error identified by the field **fields**

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
