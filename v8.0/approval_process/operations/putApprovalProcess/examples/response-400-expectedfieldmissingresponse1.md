Error response: no record modification field specified

```json
{
  "approval_process": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "during_approval_waiting",
            "json_path": "$.approval_process[0].rules[0].overall_stages_record_modification.during_approval_waiting"
          },
          {
            "api_name": "after_record_rejection",
            "json_path": "$.approval_process[0].rules[0].overall_stages_record_modification.after_record_rejection"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
