INVALID_DATA error for invalid data on the based_on_field field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "based_on_field",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field"
      },
      "status": "error"
    }
  ]
}
```
