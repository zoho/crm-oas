INVALID_DATA error: invalid data in the name field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.layout.name"
      },
      "status": "error"
    }
  ]
}
```
