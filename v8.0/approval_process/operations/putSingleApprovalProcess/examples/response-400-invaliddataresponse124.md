INVALID_DATA error when the based_on_field api_name exceeds 200 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field.api_name"
      },
      "status": "error"
    }
  ]
}
```
