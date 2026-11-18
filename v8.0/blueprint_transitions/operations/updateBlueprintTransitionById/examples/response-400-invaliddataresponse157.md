Error response when the **comparator** field contains invalid data

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "comparator",
        "maximum_length": 5,
        "json_path": "$.transitions[*].criteria.group[*].group[*].comparator"
      },
      "status": "error"
    }
  ]
}
```
