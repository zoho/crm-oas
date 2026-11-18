MANDATORY_NOT_FOUND error: required feed field missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "feed",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.notify_original_approvers_via.feed"
      },
      "status": "error"
    }
  ]
}
```
