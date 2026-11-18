DEPENDENT_MISMATCH: stage record_modification requires everyone_sequential

```json
{
  "approval_process": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "overall_approval_type",
          "json_path": "$.approval_process[0].rules[0].overall_approval_type"
        },
        "api_name": "record_modification",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].record_modification"
      },
      "message": "stage record_modification is applicable for everyone_sequential",
      "status": "error"
    }
  ]
}
```
