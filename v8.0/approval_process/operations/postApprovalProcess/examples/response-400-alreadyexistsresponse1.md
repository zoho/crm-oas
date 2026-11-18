ALREADY_EXISTS error for duplicate approval order

```json
{
  "approval_process": [
    {
      "code": "ALREADY_EXISTS",
      "details": {
        "api_name": "approval_order",
        "exists_in": {
          "api_name": "approval_order",
          "json_path": "$.approval_process[0].rules[0].actions_per_approval[0].approval_order"
        },
        "json_path": "$.approval_process[0].rules[0].actions_per_approval[1].approval_order"
      },
      "message": "duplicate sequence number",
      "status": "error"
    }
  ]
}
```
