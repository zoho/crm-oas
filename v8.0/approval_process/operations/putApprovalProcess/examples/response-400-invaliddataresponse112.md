INVALID_DATA error: approver resource name must be of type text

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.resource.name"
      },
      "status": "error"
    }
  ]
}
```
