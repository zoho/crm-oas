INVALID_DATA error: rejection action type exceeds maximum length of 50

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
