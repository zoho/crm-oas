Invalid data type error identified by the field **api_name**

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
