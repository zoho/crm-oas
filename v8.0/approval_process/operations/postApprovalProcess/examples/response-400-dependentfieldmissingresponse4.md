Dependent field missing error naming the field **rejection_type**

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
        "api_name": "rejection_type",
        "json_path": "$.approval_process[0].rules[0].actions_upon_rejection.rejection_type"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```
