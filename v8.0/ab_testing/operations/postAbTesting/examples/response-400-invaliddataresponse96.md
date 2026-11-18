INVALID_DATA error: Invalid data (field: hidden)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "hidden",
        "supported_values": [
          true,
          false
        ],
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].hidden"
      },
      "status": "error"
    }
  ]
}
```
