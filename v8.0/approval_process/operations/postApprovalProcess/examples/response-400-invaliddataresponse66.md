Invalid data type error for the **after_record_rejection** field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "after_record_rejection",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection"
      },
      "status": "error"
    }
  ]
}
```
