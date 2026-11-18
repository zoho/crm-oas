Error response with code INVALID_DATA: Invalid data (Field: actions)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions",
        "maximum_length": 500,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions"
      },
      "status": "error"
    }
  ]
}
```
