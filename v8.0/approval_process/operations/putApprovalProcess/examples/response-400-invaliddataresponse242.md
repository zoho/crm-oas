INVALID_DATA type error on notify_original_approvers_via.email (expected boolean)

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
