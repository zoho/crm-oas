INVALID_DATA error caused by an invalid data type in during_approval_waiting

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "during_approval_waiting",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification.during_approval_waiting"
      },
      "status": "error"
    }
  ]
}
```
