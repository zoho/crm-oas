INVALID_DATA error for a criteria type value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "maximum_length": 5,
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.type"
      },
      "status": "error"
    }
  ]
}
```
