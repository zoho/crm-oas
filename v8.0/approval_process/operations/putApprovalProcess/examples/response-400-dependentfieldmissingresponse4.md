DEPENDENT_FIELD_MISSING for missing notify_original_approvers_via

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "overall_approval_type",
          "json_path": "$.approval_process[0].rules[0].overall_approval_type"
        },
        "api_name": "notify_original_approvers_via",
        "json_path": "$.approval_process[0].rules[0].actions_upon_rejection.notify_original_approvers_via"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
