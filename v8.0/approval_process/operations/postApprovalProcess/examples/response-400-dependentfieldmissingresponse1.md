Missing dependent level field in the request

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.type"
        },
        "api_name": "level",
        "json_path": "$.approval_process[0].rules[0].approver_stages[1].approver.level"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
