INVALID_DATA error when the approval process name exceeds 100 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 100,
        "api_name": "name",
        "json_path": "$.approval_process[0].name"
      },
      "message": "The lenght of name has exceeded the limit",
      "status": "error"
    }
  ]
}
```
