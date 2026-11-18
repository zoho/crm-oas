Invalid data error for **actions** over 500 entries after rejection

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "actions",
        "maximum_length": 500,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions"
      },
      "status": "error"
    }
  ]
}
```
