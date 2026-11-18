INVALID_DATA error when update_allowed_for has an unsupported value

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
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
