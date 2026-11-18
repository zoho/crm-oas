Invalid data type for the process_admin type field, which expects text

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].type"
      },
      "status": "error"
    }
  ]
}
```
