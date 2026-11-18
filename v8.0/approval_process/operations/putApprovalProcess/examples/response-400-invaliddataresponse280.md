INVALID_DATA error for an invalid approval stage id

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.approval_process[0].rules[0].overall_stages_record_modification.during_approval_waiting[0].id"
      },
      "message": "the fieldId given seems to be invalid",
      "status": "error"
    }
  ]
}
```
