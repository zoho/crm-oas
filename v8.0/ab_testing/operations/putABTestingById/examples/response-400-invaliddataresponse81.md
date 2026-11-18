INVALID_DATA: Invalid data type (Field: field_label)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field_label",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].field_label"
      },
      "status": "error"
    }
  ]
}
```
