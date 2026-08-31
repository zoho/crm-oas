Error response with code INVALID_DATA: Invalid data type (Field: score)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "score",
        "expected_data_type": "integer",
        "json_path": "$.scoring_rules[0].field_rules[0].score"
      },
      "status": "error"
    }
  ]
}
```
