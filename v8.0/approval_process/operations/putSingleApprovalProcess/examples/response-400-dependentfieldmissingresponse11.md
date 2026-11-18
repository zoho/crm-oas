DEPENDENT_FIELD_MISSING error when approver level is missing

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
        "api_name": "level",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.approval_process.rules.approver_stages.approver.level"
      },
      "status": "error"
    }
  ]
}
```
