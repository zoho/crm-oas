MANDATORY_NOT_FOUND error for missing criteria value in validation filter

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "value",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.value"
      },
      "status": "error"
    }
  ]
}
```
