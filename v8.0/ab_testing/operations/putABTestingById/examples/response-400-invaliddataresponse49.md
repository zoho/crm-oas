INVALID_DATA: Invalid data type (Field: traffic)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "traffic",
        "expected_data_type": "integer",
        "json_path": "$.AB_testing[*].variant_form[*].traffic"
      },
      "status": "error"
    }
  ]
}
```
