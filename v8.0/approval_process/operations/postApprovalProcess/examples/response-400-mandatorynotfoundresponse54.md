MANDATORY_NOT_FOUND error when the required email field is missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "email",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.notify_original_approvers_via.email"
      },
      "status": "error"
    }
  ]
}
```
