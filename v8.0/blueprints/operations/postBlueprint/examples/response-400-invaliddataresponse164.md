INVALID_DATA error for a field value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field",
        "maximum_length": 1,
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.field"
      },
      "status": "error"
    }
  ]
}
```
