INVALID_DATA error for an invalid comparator field type

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "comparator",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
