DEPENDENT_FIELD_MISSING error — required name field absent

```json
{
  "kiosks": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.kiosks[*].type"
        },
        "api_name": "name",
        "json_path": "$.kiosks[*].kiosks.name"
      },
      "status": "error"
    }
  ]
}
```
