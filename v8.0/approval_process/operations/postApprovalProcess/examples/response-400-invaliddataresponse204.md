Invalid data error for the layout ID field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.layout.id"
      },
      "status": "error"
    }
  ]
}
```
