INVALID_DATA error: Invalid data type (field: width)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "width",
        "expected_data_type": "integer",
        "json_path": "$.AB_testing[*].variant_form[*].form_attributes.width"
      },
      "status": "error"
    }
  ]
}
```
