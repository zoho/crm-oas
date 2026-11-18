NOT_ALLOWED error when deleting all approval stages of a rule

```json
{
  "approval_process": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "_delete",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0]._delete"
      },
      "message": "all approval stages cannot be deleted",
      "status": "error"
    }
  ]
}
```
