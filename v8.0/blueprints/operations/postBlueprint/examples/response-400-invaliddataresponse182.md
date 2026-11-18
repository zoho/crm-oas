Error response with code INVALID_DATA: Invalid data (Field: ID)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.blueprints[*].transitions[*].during_inputs[*].field.id"
      },
      "status": "error"
    }
  ]
}
```
