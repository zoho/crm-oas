INVALID_DATA error for the based_on_field ID exceeding its length limit

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
