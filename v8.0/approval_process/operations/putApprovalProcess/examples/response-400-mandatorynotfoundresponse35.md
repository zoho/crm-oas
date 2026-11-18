Missing type field for an entry in a rule's process_admin array

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].type"
      },
      "status": "error"
    }
  ]
}
```
