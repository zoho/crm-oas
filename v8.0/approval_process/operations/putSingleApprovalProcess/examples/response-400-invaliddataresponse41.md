INVALID_DATA error when the rule name exceeds 200 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].name"
      },
      "status": "error"
    }
  ]
}
```
