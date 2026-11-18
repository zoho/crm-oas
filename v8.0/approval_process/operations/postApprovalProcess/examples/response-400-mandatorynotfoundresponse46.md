MANDATORY_NOT_FOUND error for the missing feed field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "feed",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.notify_original_approvers_via.feed"
      },
      "status": "error"
    }
  ]
}
```
