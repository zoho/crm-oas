Invalid data type error for the **update_allowed_for** field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "update_allowed_for",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
