INVALID_DATA error: on-approval trigger action type exceeds 50 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 50,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approval_trigger[*].type"
      },
      "status": "error"
    }
  ]
}
```
