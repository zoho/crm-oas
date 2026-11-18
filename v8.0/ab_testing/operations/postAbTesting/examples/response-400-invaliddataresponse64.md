INVALID_DATA error: Invalid data (field: family)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "family",
        "maximum_length": 11,
        "json_path": "$.AB_testing[*].variant_form[*].form_attributes.font_attributes.family"
      },
      "status": "error"
    }
  ]
}
```
