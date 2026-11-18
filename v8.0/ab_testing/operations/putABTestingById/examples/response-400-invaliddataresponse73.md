INVALID_DATA: Invalid data type (Field: name)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].variant_form[*].button_attributes[*].name"
      },
      "status": "error"
    }
  ]
}
```
