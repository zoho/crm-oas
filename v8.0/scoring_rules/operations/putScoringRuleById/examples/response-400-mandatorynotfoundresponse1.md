Error response with code MANDATORY_NOT_FOUND: required field not found (Field: reference_field | field_label)

```json
{
  "scoring_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "status": "error",
      "details": {
        "api_name": "reference_field | field_label",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field | $.scoring_rules[0].custom_fields[0].field_label"
      },
      "message": "required field not found"
    }
  ]
}
```
