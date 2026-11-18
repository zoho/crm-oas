DEPENDENT_FIELD_MISSING error for the conversion_percentage_difference field

```json
{
  "AB_testing": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "message": "Dependent field is missing",
      "details": {
        "dependee": {
          "api_name": "announce_automatically",
          "json_path": "$.AB_testing[*].winner_configuration.announce_automatically"
        },
        "api_name": "conversion_percentage_difference",
        "json_path": "$.AB_testing[*].winner_configuration.AB_testing.winner_configuration.conversion_percentage_difference"
      },
      "status": "error"
    }
  ]
}
```
