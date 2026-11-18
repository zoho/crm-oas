INVALID_DATA error for field 'name' when updating an approval process

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].name"
      },
      "status": "error"
    }
  ]
}
```
