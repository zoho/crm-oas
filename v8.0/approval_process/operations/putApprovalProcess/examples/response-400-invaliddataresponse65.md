INVALID_DATA error: invalid data in update_allowed_for

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_allowed_for",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
