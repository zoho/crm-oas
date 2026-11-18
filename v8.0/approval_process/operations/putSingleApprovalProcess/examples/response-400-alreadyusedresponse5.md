ALREADY_USED error for a duplicate approver type across approver stages

```json
{
  "approval_process": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "type",
        "exists_in": {
          "api_name": "type",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.type"
        },
        "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.type"
      },
      "message": "The data is already given in the same request under different key",
      "status": "error"
    }
  ]
}
```
