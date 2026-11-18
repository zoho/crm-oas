INVALID_DATA error for an invalid ID value in the create request

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.module.id"
      },
      "status": "error"
    }
  ]
}
```
