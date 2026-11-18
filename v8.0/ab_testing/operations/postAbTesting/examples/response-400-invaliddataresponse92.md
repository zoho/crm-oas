INVALID_DATA error: Invalid data (field: text)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "text",
        "maximum_length": 100,
        "json_path": "$.AB_testing[*].variant_form[*].fields[*].help.text"
      },
      "status": "error"
    }
  ]
}
```
