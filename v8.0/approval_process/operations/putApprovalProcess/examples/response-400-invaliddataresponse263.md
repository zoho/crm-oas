Invalid data type error for the api_name field in the update payload

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.module.api_name"
      },
      "status": "error"
    }
  ]
}
```
