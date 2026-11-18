INVALID_DATA error for a non-text criteria type value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "type",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.type"
      },
      "status": "error"
    }
  ]
}
```
