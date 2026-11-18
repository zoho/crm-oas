Error response with code INVALID_DATA: Invalid data type (Field: id)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].map_states[*].existing_state.id"
      },
      "status": "error"
    }
  ]
}
```
