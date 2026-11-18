Error response with code INVALID_DATA: Invalid data (Field: id)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 50,
        "json_path": "$.blueprints[*].map_states[*].existing_state.id"
      },
      "status": "error"
    }
  ]
}
```
