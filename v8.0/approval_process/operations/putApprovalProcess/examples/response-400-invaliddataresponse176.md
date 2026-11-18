Invalid data for the process_admin field below the minimum length of 1

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
