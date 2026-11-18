INVALID_DATA error for an invalid data type on during_approval_waiting

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "during_approval_waiting",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting"
      },
      "status": "error"
    }
  ]
}
```
