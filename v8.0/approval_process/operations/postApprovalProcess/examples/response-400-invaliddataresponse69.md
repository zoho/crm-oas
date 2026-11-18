Invalid data error for the **update_allowed_for** field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_allowed_for",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
