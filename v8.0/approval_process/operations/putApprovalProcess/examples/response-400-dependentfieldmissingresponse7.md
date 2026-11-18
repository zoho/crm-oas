DEPENDENT_FIELD_MISSING for missing actions_per_approval

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "overall_approval_type",
          "json_path": "$.approval_process[*].rules[*].overall_approval_type"
        },
        "api_name": "actions_per_approval",
        "json_path": "$.approval_process[*].rules[*].approval_process.rules.actions_per_approval"
      },
      "status": "error"
    }
  ]
}
```
