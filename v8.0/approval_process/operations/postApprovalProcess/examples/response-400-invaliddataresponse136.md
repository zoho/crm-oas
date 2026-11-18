Invalid data error for update_allowed_for over 50 characters after rejection

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_allowed_for",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
