INVALID_DATA error when the criteria comparator is not a text value

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "comparator",
        "expected_data_type": "text",
        "json_path": "$.approval_process[*].rules[*].criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
