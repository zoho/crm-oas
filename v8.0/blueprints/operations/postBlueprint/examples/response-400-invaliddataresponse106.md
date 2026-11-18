INVALID_DATA error for an invalid data type in the field property

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].transitions[*].criteria.field"
      },
      "status": "error"
    }
  ]
}
```
