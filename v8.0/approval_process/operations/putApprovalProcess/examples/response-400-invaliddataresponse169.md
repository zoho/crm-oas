INVALID_DATA: on-approve action name field exceeds maximum length 25

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve[*].name"
      },
      "status": "error"
    }
  ]
}
```
