INVALID_DATA error for an invalid data type in the description field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "description",
        "expected_data_type": "text",
        "json_path": "$.blueprints[*].transitions[*].description"
      },
      "status": "error"
    }
  ]
}
```
