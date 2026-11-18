INVALID_DATA error for a non-text api_name value in a transition criterion

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
