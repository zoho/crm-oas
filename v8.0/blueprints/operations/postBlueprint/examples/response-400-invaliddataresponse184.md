Error response with code INVALID_DATA: Invalid data type (Field: optional)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "optional",
        "expected_data_type": "boolean",
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].optional"
      },
      "status": "error"
    }
  ]
}
```
