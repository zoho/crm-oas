### `application/json` — TerritoryUpdateById

Update territory by ID

```json
{
  "territories": [
    {
      "id": "431581000000798016",
      "name": "Territory1234",
      "reporting_to": {
        "id": "431581000000272796"
      },
      "manager": null,
      "permission_type": "read_only",
      "description": null,
      "account_rule_criteria": null,
      "lead_rule_criteria": null,
      "deal_rule_criteria": {
        "comparator": "greater_than",
        "field": {
          "api_name": "Amount",
          "id": "431581000000000799"
        },
        "value": "2000000"
      }
    }
  ]
}
```
