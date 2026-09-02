Error response with code ALREADY_USED: The custom field has already used in other places (Field: id)

```json
{
  "scoring_rules": [
    {
      "code": "ALREADY_USED",
      "status": "error",
      "details": {
        "api_name": "id",
        "id": "1000000000047",
        "json_path": "$.scoring_rules[0].custom_fields[2].id",
        "associated_places": [
          {
            "name": "L WFR",
            "id": "1000000067060",
            "type": "workflow"
          }
        ]
      },
      "message": "The custom field has already used in other places"
    }
  ]
}
```
