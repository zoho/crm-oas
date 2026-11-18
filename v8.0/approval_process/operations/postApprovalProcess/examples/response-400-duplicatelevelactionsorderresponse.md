Error response with code DUPLICATE_DATA: The data is already given in the approval_order (Field: approval_order)

```json
{
  "approval_process": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "approval_order",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].actions.actions_per_approval[0].approval_order"
      },
      "message": "The data is already given in the approval_order",
      "status": "error"
    }
  ]
}
```
