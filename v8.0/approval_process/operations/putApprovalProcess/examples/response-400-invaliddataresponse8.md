INVALID_DATA response for an invalid approver level in the level_up_to field

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
