Invalid data error for the criteria field ID over 25 characters

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
