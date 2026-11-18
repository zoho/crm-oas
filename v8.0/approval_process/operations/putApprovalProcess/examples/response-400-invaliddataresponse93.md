INVALID_DATA error: invalid data type for the type field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
