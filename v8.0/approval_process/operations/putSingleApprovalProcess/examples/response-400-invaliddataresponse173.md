INVALID_DATA error when process_admin_configuration exceeds its maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "process_admin_configuration",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration"
      },
      "status": "error"
    }
  ]
}
```
