Error response with code INVALID_DATA: invalid data in the name field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].name"
      },
      "status": "error"
    }
  ]
}
```
