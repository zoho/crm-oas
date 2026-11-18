Missing email option in the original-approver notification settings

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "email",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.notify_original_approvers_via.email"
      },
      "status": "error"
    }
  ]
}
```
