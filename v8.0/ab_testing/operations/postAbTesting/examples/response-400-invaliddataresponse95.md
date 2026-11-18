INVALID_DATA error: Invalid data type (field: hidden)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "hidden",
        "expected_data_type": "boolean",
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].hidden"
      },
      "status": "error"
    }
  ]
}
```
