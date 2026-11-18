Error response with code INVALID_DATA: Invalid data (Field: id)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].resources[*].id"
      },
      "status": "error"
    }
  ]
}
```
