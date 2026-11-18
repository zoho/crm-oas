Dependent mismatch error on the actions_per_approval field

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "approver_stages",
          "json_path": "$.approval_process[0].rules[0].approver_stages"
        },
        "maximum_length": 7,
        "api_name": "actions_per_approval",
        "json_path": "$.approval_process[0].rules[0].actions_per_approval[10].approval_order"
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```
