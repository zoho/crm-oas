INVALID_DATA error for an approver level outside the range of 2 to 50

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "level_up_to",
        "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.level_up_to",
        "range": {
          "from": 2,
          "to": 50
        }
      },
      "message": "invalid approver level given",
      "status": "error"
    }
  ]
}
```
