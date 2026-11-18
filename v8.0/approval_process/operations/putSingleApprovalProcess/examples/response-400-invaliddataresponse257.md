Invalid data type error for a rejection action layout name

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.layout.name"
      },
      "status": "error"
    }
  ]
}
```
