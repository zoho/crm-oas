INVALID_DATA: invalid sequence number in approver stage

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "sequence_number",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0]",
        "range": {
          "from": 1,
          "to": 5
        }
      },
      "message": "invalid sequence number",
      "status": "error"
    }
  ]
}
```
