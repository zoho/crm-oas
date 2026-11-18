NOT_ALLOWED error for a profile outside the team profile type

```json
{
  "approval_process": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.resource.id"
      },
      "message": "the given profile details does not belong to team profile type",
      "status": "error"
    }
  ]
}
```
