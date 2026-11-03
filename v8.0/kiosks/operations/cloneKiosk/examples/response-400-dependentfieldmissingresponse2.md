DEPENDENT_FIELD_MISSING error — required description field absent

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
        "api_name": "description",
        "json_path": "$.kiosks[*].kiosks.description"
      },
      "status": "error"
    }
  ]
}
```
