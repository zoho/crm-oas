INVALID_DATA error for the criteria field exceeding one character

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field",
        "maximum_length": 1,
        "json_path": "$.approval_process[*].rules[*].criteria.field"
      },
      "status": "error"
    }
  ]
}
```
