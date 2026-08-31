Example of missing required field or group in criteria object.

```json
{
  "code": "EXPECTED_FIELD_MISSING",
  "details": {
    "expected_fields": [
      {
        "api_name": "group",
        "json_path": "$.criteria.group"
      },
      {
        "api_name": "field",
        "json_path": "$.criteria.field"
      }
    ]
  },
  "message": "Specify atleast one field",
  "status": "error"
}
```
