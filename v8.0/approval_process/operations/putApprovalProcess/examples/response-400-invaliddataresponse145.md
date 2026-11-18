INVALID_DATA error: update_allowed_for is not a supported value

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_allowed_for",
        "supported_values": [
          "no_fields",
          "all_fields",
          "specific_fields"
        ],
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
