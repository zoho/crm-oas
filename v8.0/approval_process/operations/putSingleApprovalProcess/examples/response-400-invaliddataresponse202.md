Error when an action type exceeds the maximum of 50 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].type"
      },
      "status": "error"
    }
  ]
}
```
