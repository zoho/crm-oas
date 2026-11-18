INVALID_DATA error: Invalid data type (field: form_fields)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "form_fields",
        "expected_data_type": "jsonarray",
        "json_path": "$.AB_testing[*].variant_form[*].form_fields"
      },
      "status": "error"
    }
  ]
}
```
