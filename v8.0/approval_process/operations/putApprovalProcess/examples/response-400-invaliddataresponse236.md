INVALID_DATA error: actions_upon_rejection exceeds maximum length of 1

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions_upon_rejection",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection"
      },
      "status": "error"
    }
  ]
}
```
