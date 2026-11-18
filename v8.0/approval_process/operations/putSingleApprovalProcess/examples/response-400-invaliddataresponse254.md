Layout in rejection action details exceeding the maximum length of 1

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "layout",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.layout"
      },
      "status": "error"
    }
  ]
}
```
