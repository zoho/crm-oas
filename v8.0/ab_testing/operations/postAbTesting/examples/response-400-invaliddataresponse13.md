INVALID_DATA error when traffic value exceeds the maximum

```json
{
  "AB_testing": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "traffic",
        "maximum_length": 3,
        "json_path": "$.AB_testing[*].traffic"
      },
      "status": "error"
    }
  ]
}
```
