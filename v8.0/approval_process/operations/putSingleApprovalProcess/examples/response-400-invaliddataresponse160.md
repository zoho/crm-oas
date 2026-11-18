INVALID_DATA error for an on-approval action name exceeding 200 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger[*].name"
      },
      "status": "error"
    }
  ]
}
```
