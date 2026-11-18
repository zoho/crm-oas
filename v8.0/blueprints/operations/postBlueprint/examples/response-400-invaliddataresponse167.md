INVALID_DATA error for a non-numeric ID value in a transition criterion

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.field.id"
      },
      "status": "error"
    }
  ]
}
```
