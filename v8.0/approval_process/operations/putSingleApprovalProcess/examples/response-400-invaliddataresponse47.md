INVALID_DATA error when the criteria comparator exceeds the maximum length

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
