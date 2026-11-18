INVALID_DATA: Invalid data type (Field: size)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "size",
        "expected_data_type": "bigint",
        "json_path": "$.AB_testing[*].variant_form[*].form_attributes.font_attributes.size"
      },
      "status": "error"
    }
  ]
}
```
