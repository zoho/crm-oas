400 MANDATORY_NOT_FOUND when the required approver field is missing

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "approver",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver"
      },
      "message": "The required data missing",
      "status": "error"
    }
  ]
}
```
