INVALID_DATA error for an invalid data type on record_modification

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "record_modification",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].record_modification"
      },
      "status": "error"
    }
  ]
}
```
