Invalid data type error for the process_admin field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "process_admin",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin"
      },
      "status": "error"
    }
  ]
}
```
