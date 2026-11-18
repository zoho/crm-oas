Criteria value exceeding the 9-character limit

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 9,
        "json_path": "$.approval_process[*].rules[*].criteria.value"
      },
      "status": "error"
    }
  ]
}
```
