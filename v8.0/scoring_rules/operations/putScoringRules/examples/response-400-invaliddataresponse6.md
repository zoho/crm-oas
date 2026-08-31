Error response with code INVALID_DATA: Reference field api_name given seems to be invalid (Field: api_name)

```json
{
  "scoring_rules": [
    {
      "code": "INVALID_DATA",
      "status": "error",
      "details": {
        "api_name": "api_name",
        "json_path": "$.scoring_rules[0].custom_fields[0].reference_field.api_name",
        "supported_values": [
          "Positive_Score",
          "Negative_score",
          "Touch_Point_score",
          "Touch_Point_Positive_Score",
          "Touch_Point_Negative_Score",
          "Score"
        ]
      },
      "message": "Reference field api_name given seems to be invalid"
    }
  ]
}
```
