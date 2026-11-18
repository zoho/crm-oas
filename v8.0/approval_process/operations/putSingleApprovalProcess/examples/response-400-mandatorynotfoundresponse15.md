**MANDATORY_NOT_FOUND** error when **update_allowed_for** is missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "update_allowed_for",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
