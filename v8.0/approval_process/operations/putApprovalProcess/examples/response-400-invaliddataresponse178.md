Invalid data for the process_admin type field exceeding the maximum length of 50

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].process_admin_configuration.process_admin[*].type"
      },
      "status": "error"
    }
  ]
}
```
