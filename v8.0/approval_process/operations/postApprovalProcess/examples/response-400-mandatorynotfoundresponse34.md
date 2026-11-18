MANDATORY_NOT_FOUND error: create request missing the update_allowed_for field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "update_allowed_for",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
