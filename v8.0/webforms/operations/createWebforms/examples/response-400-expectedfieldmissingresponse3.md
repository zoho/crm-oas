EXPECTED_FIELD_MISSING error for missing required form configuration fields

```json
{
  "webforms": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "theme",
            "json_path": "$.webforms[0].form_fields[2].theme"
          }
        ]
      },
      "message": "One of the expected field missing",
      "status": "error"
    }
  ]
}
```
