Missing record_modification field in the process admin configuration

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "record_modification",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.record_modification"
      },
      "status": "error"
    }
  ]
}
```
