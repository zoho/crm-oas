INVALID_DATA error: invalid data in the actions field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions",
        "maximum_length": 10,
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions"
      },
      "status": "error"
    }
  ]
}
```
