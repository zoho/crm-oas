INVALID_DATA error for an invalid comparator field value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "comparator",
        "maximum_length": 12,
        "json_path": "$.blueprints[*].transitions[*].criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
