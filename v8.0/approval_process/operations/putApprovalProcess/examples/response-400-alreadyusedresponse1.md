ALREADY_USED error for a duplicate level value across approver stages

```json
{
  "approval_process": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "level",
        "exists_in": {
          "api_name": "level",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.level"
        },
        "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.level"
      },
      "message": "The data is already given in the same request under different key",
      "status": "error"
    }
  ]
}
```
