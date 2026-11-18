Invalid data error for the **after_record_rejection** field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "after_record_rejection",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection"
      },
      "status": "error"
    }
  ]
}
```
