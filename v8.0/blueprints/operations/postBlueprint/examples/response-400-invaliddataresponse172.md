INVALID_DATA error for a non-bigint validation filter criteria value

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.value"
      },
      "status": "error"
    }
  ]
}
```
