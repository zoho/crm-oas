Missing id field for an on_approve action of an approver stage

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].actions.on_approve[*].id"
      },
      "status": "error"
    }
  ]
}
```
