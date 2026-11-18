DEPENDENT_FIELD_MISSING error for a missing based_on_field property in an approver

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.approval_process[0].rules[0].approver_stages[2].approver.type"
        },
        "api_name": "based_on_field",
        "json_path": "$.approval_process[0].rules[0].approver_stages[2].approver.based_on_field"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
