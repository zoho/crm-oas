MANDATORY_NOT_FOUND error: missing id in process admin resources

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
