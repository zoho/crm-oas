Invalid data type error for the name field in the create request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].resources[*].name"
      },
      "status": "error"
    }
  ]
}
```
