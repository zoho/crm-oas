INVALID_DATA error for field 'details' when updating an approval process

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "details",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
