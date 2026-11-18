Error response with code INVALID_DATA: Invalid data (Field: api_name)

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
