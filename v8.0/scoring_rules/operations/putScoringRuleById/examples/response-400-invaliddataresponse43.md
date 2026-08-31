Error response with code INVALID_DATA: Invalid data type (Field: reference_field)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "reference_field",
        "expected_data_type": "jsonobject",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field"
      },
      "status": "error"
    }
  ]
}
```
