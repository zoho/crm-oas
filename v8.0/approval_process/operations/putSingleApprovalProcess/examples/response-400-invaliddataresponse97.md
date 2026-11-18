INVALID_DATA error when approver_stages exceeds one entry

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "approver_stages",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages"
      },
      "status": "error"
    }
  ]
}
```
