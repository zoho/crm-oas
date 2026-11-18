EXPECTED_FIELD_MISSING error when required module identifier fields are missing

```json
{
  "AB_testing": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "message": "One of the required fields is missing",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.AB_testing[*].module.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.AB_testing[*].module.AB_testing.module.api_name"
          }
        ]
      },
      "status": "error"
    }
  ]
}
```
