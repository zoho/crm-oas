Error response with code ALREADY_USED: The criteria is already given in the same rule under different index (Field: criteria)

```json
{
  "scoring_rules": [
    {
      "code": "ALREADY_USED",
      "details": {
        "api_name": "criteria",
        "exists_in": {
          "api_name": "criteria",
          "json_path": "$.scoring_rules[0].field_rules[0].criteria"
        },
        "json_path": "$.scoring_rules[0].field_rules[1].criteria"
      },
      "message": "The criteria is already given in the same rule under different index",
      "status": "error"
    }
  ]
}
```
