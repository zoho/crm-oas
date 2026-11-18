INVALID_DATA error for an invalid data type in the name field of the request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions[*].name"
      },
      "status": "error"
    }
  ]
}
```
