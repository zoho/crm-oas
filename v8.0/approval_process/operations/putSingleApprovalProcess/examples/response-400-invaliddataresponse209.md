INVALID_DATA error when an action layout value exceeds one character

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "layout",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.layout"
      },
      "status": "error"
    }
  ]
}
```
