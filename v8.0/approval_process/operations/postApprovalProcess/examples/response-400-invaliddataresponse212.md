Invalid data error for the api_name field in the create request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.module.api_name"
      },
      "status": "error"
    }
  ]
}
```
