INVALID_DATA error for invalid data type on the form field ID

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].id"
      },
      "status": "error"
    }
  ]
}
```
