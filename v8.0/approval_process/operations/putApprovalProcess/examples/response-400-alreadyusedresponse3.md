ALREADY_USED error for a duplicate approver resource ID across stages

```json
{
  "approval_process": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "id",
        "exists_in": {
          "api_name": "id",
          "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.resource.id"
        },
        "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.resource.id"
      },
      "message": "The data is already given in the same request under different key",
      "status": "error"
    }
  ]
}
```
