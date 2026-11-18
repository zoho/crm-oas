INVALID_DATA error when an action type exceeds 20 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 20,
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
