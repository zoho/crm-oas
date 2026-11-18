Error response with code INVALID_DATA: Invalid data (Field: id)

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
