MANDATORY_NOT_FOUND error: required after_record_rejection field is missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "after_record_rejection",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.after_record_rejection"
      },
      "status": "error"
    }
  ]
}
```
