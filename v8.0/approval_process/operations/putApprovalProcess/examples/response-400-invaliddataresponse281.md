INVALID_DATA error when the approval stage id is invalid

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[0].rules[0].actions_upon_final_approval.actions[0].id"
      },
      "message": "given action id not found",
      "status": "error"
    }
  ]
}
```
