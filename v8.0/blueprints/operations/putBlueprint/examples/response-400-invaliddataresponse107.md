Error — invalid data type for api_name (INVALID_DATA)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].connections[*].from_state.api_name"
      },
      "status": "error"
    }
  ]
}
```
