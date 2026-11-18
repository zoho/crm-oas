INVALID_DATA error when the action name has an invalid data type

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
