INVALID_DATA error for invalid data in the comparator field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "comparator",
        "maximum_length": 5,
        "json_path": "$.approval_process[*].rules[*].criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
