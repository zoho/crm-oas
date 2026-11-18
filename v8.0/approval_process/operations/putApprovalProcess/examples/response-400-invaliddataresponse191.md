INVALID_DATA error: update_allowed_for has unsupported value

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_allowed_for",
        "supported_values": [
          "all_fields",
          "no_fields",
          "approver_stages_record_modification_fields"
        ],
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.record_modification.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
