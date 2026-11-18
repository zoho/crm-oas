INVALID_DATA error: action id exceeds maximum length of 25

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].id"
      },
      "status": "error"
    }
  ]
}
```
