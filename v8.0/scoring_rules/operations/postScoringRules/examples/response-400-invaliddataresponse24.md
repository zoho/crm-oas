Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "supported_values": [
          "Positive_Score",
          "Negative_Score",
          "Touch_Point_Positive_Score",
          "Touch_Point_Negative_Score",
          "Touch_Point_Score",
          "Score"
        ],
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name"
      },
      "status": "error"
    }
  ]
}
```
