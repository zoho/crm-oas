Minimum length violation for the process admin resources field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "resources",
        "minimum_length": 1,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].resources"
      },
      "status": "error"
    }
  ]
}
```
