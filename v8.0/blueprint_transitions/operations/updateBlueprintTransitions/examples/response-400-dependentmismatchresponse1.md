Error response with code DEPENDENT_MISMATCH: You can provide upto 10 checklist items (Field: items)

```json
{
  "transitions": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "json_path": "$.transitions[0].during_inputs[0].items",
        "api_name": "items",
        "maximum_length": 10,
        "dependee": {
          "dependee_value": "checklist",
          "json_path": "$.transitions[0].during_inputs[0].type",
          "api_name": "type"
        }
      },
      "message": "You can provide upto 10 checklist items",
      "status": "error"
    }
  ]
}
```
