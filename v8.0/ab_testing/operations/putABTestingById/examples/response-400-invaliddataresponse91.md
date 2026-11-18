INVALID_DATA: Invalid data type (Field: text)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "text",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].help.text"
      },
      "status": "error"
    }
  ]
}
```
