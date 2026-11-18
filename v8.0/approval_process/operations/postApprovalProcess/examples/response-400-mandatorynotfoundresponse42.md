MANDATORY_NOT_FOUND error for a missing process admin resource ID field

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
