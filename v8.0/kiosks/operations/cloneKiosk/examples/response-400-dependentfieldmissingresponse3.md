DEPENDENT_FIELD_MISSING error — required group_api_name field absent

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
        "api_name": "group_api_name",
        "json_path": "$.kiosks[*].kiosks.group_api_name"
      },
      "status": "error"
    }
  ]
}
```
