Error response with code INVALID_DATA: Invalid data (Field: comparator)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "comparator",
        "maximum_length": 12,
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
