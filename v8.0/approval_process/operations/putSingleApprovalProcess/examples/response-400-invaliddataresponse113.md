Invalid data error for the approver resource name

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.resource.name"
      },
      "status": "error"
    }
  ]
}
```
