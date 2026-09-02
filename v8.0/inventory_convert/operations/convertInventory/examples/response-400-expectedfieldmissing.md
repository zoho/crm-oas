Required field missing from convert_to array

```json
{
  "data": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.data[0].convert_to[0].module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.data[0].convert_to[0].module.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
