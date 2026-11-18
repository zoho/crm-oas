Invalid data error for the criteria field api_name over 200 characters

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 200,
        "json_path": "$.approval_process[*].rules[*].criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
