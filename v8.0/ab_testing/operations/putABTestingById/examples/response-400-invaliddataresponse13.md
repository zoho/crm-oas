INVALID_DATA error for exceeding maximum value on the traffic field

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
