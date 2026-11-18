Invalid data type for the api_name of the approver field in an approver stage

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
