INVALID_DATA error for a non-integer sequence number in the Approval Process

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "sequence_number",
        "expected_data_type": "integer",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].sequence_number"
      },
      "status": "error"
    }
  ]
}
```
