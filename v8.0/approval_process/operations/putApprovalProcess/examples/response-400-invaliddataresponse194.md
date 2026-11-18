INVALID_DATA error for invalid data type in email

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "email",
        "expected_data_type": "boolean",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.notify_original_approvers_via.email"
      },
      "status": "error"
    }
  ]
}
```
