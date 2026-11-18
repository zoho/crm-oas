INVALID_DATA error: invalid data type in the process_admin_configuration field

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
