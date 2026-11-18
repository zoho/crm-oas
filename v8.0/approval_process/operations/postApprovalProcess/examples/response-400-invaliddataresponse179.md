Invalid data error for the name field in the create request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].resources[*].name"
      },
      "status": "error"
    }
  ]
}
```
