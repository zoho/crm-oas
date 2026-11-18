Error response with code INVALID_DATA: Invalid data type (Field: ID)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.blueprints[*].states[*].pick_list_value.id"
      },
      "status": "error"
    }
  ]
}
```
