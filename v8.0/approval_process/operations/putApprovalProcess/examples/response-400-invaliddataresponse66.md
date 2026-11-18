INVALID_DATA error: invalid data in the update_allowed_for field

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
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
