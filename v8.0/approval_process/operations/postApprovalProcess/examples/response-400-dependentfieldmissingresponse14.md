DEPENDENT_FIELD_MISSING error for the based_on_field dependent field

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.type"
        },
        "api_name": "based_on_field",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.approval_process.rules.approver_stages.approver.based_on_field"
      },
      "status": "error"
    }
  ]
}
```
