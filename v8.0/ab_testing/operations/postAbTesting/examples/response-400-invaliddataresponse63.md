INVALID_DATA error: Invalid data type (field: family)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "family",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].variant_form[*].form_attributes.font_attributes.family"
      },
      "status": "error"
    }
  ]
}
```
