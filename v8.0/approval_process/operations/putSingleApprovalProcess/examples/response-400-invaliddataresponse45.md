INVALID_DATA error when a rule criteria exceeds the maximum length of one

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "criteria",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].criteria"
      },
      "status": "error"
    }
  ]
}
```
