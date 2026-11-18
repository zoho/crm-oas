Missing after_record_rejection error in record modification settings

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "after_record_rejection",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.after_record_rejection"
      },
      "status": "error"
    }
  ]
}
```
