DEPENDENT_FIELD_MISSING error for a missing approver field

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.approval_process[0].rules[0].approver_stages[3].approver.type"
        },
        "api_name": "field",
        "json_path": "$.approval_process[0].rules[0].approver_stages[3].approver.field"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
