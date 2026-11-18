INVALID_DATA error: send_default_emails_enabled has an invalid data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "send_default_emails_enabled",
        "expected_data_type": "boolean",
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.send_default_emails_enabled"
      },
      "status": "error"
    }
  ]
}
```
