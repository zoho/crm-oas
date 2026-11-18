INVALID_DATA error: invalid data in the actions_per_approval field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions_per_approval",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_per_approval"
      },
      "status": "error"
    }
  ]
}
```
