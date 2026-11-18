INVALID_DATA error for a criteria field ID value exceeding the maximum length

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.field.id"
      },
      "status": "error"
    }
  ]
}
```
