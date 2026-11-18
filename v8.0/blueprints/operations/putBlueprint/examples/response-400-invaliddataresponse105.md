Error — invalid data type for name in state or transition (INVALID_DATA)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].connections[*].from_state.name"
      },
      "status": "error"
    }
  ]
}
```
