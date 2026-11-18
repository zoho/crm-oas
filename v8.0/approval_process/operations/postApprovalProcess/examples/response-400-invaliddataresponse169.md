INVALID_DATA error for a process_admin value below one character

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "process_admin",
        "minimum_length": 1,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin"
      },
      "status": "error"
    }
  ]
}
```
