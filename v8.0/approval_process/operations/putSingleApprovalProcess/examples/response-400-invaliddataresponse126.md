INVALID_DATA error when the based_on_field id exceeds 25 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].approver_stages[*].approver.based_on_field.id"
      },
      "status": "error"
    }
  ]
}
```
