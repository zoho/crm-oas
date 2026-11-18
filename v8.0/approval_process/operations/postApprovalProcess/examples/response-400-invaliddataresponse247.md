Invalid data error for layout exceeding one entry in rejection action details

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
