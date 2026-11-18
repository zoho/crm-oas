INVALID_DATA error for an invalid id field value

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 19,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].id"
      },
      "status": "error"
    }
  ]
}
```
