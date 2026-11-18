INVALID_DATA error when an approval action ID exceeds 25 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].actions_per_approval[*].actions[*].id"
      },
      "status": "error"
    }
  ]
}
```
