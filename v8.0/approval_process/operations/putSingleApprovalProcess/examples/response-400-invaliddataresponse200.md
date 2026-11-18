Error when the actions list exceeds the maximum of 500 entries

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
