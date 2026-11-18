Invalid data error when the name field length exceeds its limit

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 100,
        "api_name": "name",
        "json_path": "$.approval_process[0].rules[0].name"
      },
      "message": "The length of name has exceeded the limit",
      "status": "error"
    }
  ]
}
```
