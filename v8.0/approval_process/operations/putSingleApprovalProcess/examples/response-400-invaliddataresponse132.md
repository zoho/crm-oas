INVALID_DATA error: update_allowed_for has an invalid data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "update_allowed_for",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
