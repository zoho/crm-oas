INVALID_DATA error: Invalid data type (field: color)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "color",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].variant_form[*].form_attributes.font_attributes.color"
      },
      "status": "error"
    }
  ]
}
```
