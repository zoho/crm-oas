INVALID_DATA error: Invalid data type (field: url)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "url",
        "expected_data_type": "website",
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].help.url"
      },
      "status": "error"
    }
  ]
}
```
