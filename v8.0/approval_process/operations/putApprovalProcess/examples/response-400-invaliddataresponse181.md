INVALID_DATA error for process admin resources maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "resources",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].resources"
      },
      "status": "error"
    }
  ]
}
```
