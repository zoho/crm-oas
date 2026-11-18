Invalid data type error for layout in rejection action details

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "layout",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.layout"
      },
      "status": "error"
    }
  ]
}
```
