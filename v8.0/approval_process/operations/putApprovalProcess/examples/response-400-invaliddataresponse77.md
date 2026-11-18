INVALID_DATA error response caused by invalid update_allowed_for data

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
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
