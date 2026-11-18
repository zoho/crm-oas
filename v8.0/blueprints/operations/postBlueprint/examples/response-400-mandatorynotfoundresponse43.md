MANDATORY_NOT_FOUND error for a missing comparator field

```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "comparator",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter.criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
