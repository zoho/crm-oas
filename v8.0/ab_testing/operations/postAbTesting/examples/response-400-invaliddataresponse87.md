INVALID_DATA error: Invalid data type (field: advanced)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "advanced",
        "expected_data_type": "boolean",
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].advanced"
      },
      "status": "error"
    }
  ]
}
```
