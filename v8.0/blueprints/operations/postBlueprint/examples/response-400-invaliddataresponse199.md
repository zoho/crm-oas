Error response with code INVALID_DATA: Invalid data type (Field: details)

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "details",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].transitions[*].actions[*].details"
      },
      "status": "error"
    }
  ]
}
```
