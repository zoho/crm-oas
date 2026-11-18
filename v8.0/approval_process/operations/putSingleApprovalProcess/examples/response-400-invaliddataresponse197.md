INVALID_DATA error: actions_upon_final_approval exceeds maximum length

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions_upon_final_approval",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval"
      },
      "status": "error"
    }
  ]
}
```
