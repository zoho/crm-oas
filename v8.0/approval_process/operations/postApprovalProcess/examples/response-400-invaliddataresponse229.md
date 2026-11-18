Invalid data error for actions_upon_rejection exceeding one entry

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
