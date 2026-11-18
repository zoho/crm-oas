INVALID_DATA error when approver_stages is not a JSON array

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "approver_stages",
        "expected_data_type": "jsonarray",
        "json_path": "$.approval_process[*].rules[*].approver_stages"
      },
      "status": "error"
    }
  ]
}
```
