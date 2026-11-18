INVALID_DATA error for update_allowed_for expected as text

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "update_allowed_for",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.record_modification.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
