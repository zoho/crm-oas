INVALID_DATA error when process_admin_configuration has an invalid data type

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "process_admin_configuration",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration"
      },
      "status": "error"
    }
  ]
}
```
