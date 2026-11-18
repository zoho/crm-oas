Invalid data type error for the id field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
