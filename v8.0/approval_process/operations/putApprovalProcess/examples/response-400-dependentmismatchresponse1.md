DEPENDENT_MISMATCH: overall_stages_record_modification value mismatch

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
        "api_name": "overall_stages_record_modification",
        "json_path": "$.approval_process[0].rules[0].overall_stages_record_modification"
      },
      "message": "overall_stages_record_modification is applicable for anyone or everyone_parallel",
      "status": "error"
    }
  ]
}
```
