INVALID_DATA error for an unsupported data type in the type field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "text",
        "api_name": "type",
        "json_path": "$.approval_process[0].rules[0].approver_stages[0].approver.type"
      },
      "message": "data type not supported",
      "status": "error"
    }
  ]
}
```
