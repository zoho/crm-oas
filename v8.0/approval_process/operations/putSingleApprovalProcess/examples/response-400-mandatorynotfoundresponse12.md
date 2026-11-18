Missing during_approval_waiting error in record modification settings

```json
{
  "approval_process": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "during_approval_waiting",
        "json_path": "$.approval_process[*].rules[*].overall_stages_record_modification.during_approval_waiting"
      },
      "status": "error"
    }
  ]
}
```
