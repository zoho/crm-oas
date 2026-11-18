INVALID_DATA error: Invalid data type (field: api_name)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].api_name"
      },
      "status": "error"
    }
  ]
}
```
