INVALID_DATA error for a non-object approver in the Approval Process

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "approver",
        "expected_data_type": "jsonobject",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver"
      },
      "status": "error"
    }
  ]
}
```
