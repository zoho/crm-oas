ALREADY_USED error for repeated level_up_to value

```json
{
  "approval_process": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "level_up_to",
        "exists_in": {
          "api_name": "level_up_to",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.level_up_to"
        },
        "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.level_up_to"
      },
      "message": "The data is already given in the same request under different key",
      "status": "error"
    }
  ]
}
```
