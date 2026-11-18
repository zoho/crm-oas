Error response with code INVALID_DATA: invalid data in the details field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "details",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
