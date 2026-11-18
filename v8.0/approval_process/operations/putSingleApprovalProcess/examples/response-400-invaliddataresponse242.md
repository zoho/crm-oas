INVALID_DATA error when the email flag is not a Boolean

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "email",
        "expected_data_type": "boolean",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.notify_original_approvers_via.email"
      },
      "status": "error"
    }
  ]
}
```
