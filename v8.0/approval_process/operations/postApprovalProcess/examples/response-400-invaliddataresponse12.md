INVALID_DATA error for invalid data on update_allowed_for

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "update_allowed_for",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].record_modification.after_record_rejection.record_modification.update_allowed_for",
        "supported_values": [
          "specific_fields",
          "all_fields",
          "no_fields"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
