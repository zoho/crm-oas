INVALID_DATA error: visits should be less than or equal to 100000 (field: unit)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "unit",
        "json_path": "$.AB_testing[0].condition.unit"
      },
      "message": "visits should be less than or equal to 100000",
      "status": "error"
    }
  ]
}
```
