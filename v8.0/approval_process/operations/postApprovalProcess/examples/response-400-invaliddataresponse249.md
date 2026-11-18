Invalid data error on the ID field in the create request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.layout.id"
      },
      "status": "error"
    }
  ]
}
```
