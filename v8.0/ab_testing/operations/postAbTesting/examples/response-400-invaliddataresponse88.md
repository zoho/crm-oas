INVALID_DATA error: Invalid data type (field: help)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "help",
        "expected_data_type": "jsonobject",
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].help"
      },
      "status": "error"
    }
  ]
}
```
