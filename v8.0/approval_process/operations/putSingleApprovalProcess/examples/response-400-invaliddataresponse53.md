Invalid criteria field ID exceeding the 25-character limit

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.approval_process[*].rules[*].criteria.field.id"
      },
      "status": "error"
    }
  ]
}
```
