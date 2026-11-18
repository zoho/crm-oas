MANDATORY_NOT_FOUND error for the missing update_allowed_for field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "update_allowed_for",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.record_modification.update_allowed_for"
      },
      "status": "error"
    }
  ]
}
```
