INVALID_DATA error for an oversized validation filter criteria value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 3,
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.value"
      },
      "status": "error"
    }
  ]
}
```
