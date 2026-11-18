INVALID_DATA error for an unsupported update_allowed_for value

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
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
