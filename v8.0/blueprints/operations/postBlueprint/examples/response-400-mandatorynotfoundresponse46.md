MANDATORY_NOT_FOUND error for missing criteria type in validation filter

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "type",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.type"
      },
      "status": "error"
    }
  ]
}
```
