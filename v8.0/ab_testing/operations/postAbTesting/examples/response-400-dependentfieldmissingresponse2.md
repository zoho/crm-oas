DEPENDENT_FIELD_MISSING error for the unit field

```json
{
  "AB_testing": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.AB_testing[*].condition.type"
        },
        "api_name": "unit",
        "json_path": "$.AB_testing[*].condition.AB_testing.condition.unit"
      },
      "status": "error"
    }
  ]
}
```
