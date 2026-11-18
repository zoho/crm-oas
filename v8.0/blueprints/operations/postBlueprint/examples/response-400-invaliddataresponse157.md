Error with code INVALID_DATA: Invalid data type (Field: validation_filter)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "validation_filter",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].validation_filter"
      },
      "status": "error"
    }
  ]
}
```
