INVALID_DATA error for an invalid data type in the layout field

```json
{
  "blueprints": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "layout",
        "expected_data_type": "jsonobject",
        "json_path": "$.blueprints[*].transitions[*].layout"
      },
      "status": "error"
    }
  ]
}
```
