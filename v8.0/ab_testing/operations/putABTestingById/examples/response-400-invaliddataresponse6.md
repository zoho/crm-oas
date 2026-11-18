INVALID_DATA: weeks should be less than or equal to 12 (Field: unit)

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "unit",
        "json_path": "$.AB_testing[0].condition.unit"
      },
      "message": "weeks should be less than or equal to 12",
      "status": "error"
    }
  ]
}
```
