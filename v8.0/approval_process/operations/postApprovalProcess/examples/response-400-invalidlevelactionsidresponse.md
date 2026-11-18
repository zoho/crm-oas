Error response with code INVALID_DATA: invalid approval stage id (Field: id)

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].actions.actions_per_approval[0].actions[0].id"
      },
      "message": "given action id not found",
      "status": "error"
    }
  ]
}
```
