INVALID_DATA error for update_allowed_for exceeding 50 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "update_allowed_for",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.record_modification.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
