INVALID_DATA error for an invalid data type in the during_approval_waiting field

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
