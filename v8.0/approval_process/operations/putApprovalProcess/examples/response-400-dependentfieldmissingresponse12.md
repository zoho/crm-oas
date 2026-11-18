DEPENDENT_FIELD_MISSING error: dependent field 'field' is missing

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
        "api_name": "field",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.approval_process.rules.approver_stages.approver.field"
      },
      "status": "error"
    }
  ]
}
```
