### `application/json` — TerritoryCreate

Create a territory with name, manager, and account rule criteria

```json
{
  "territories": [
    {
      "name": "Territory1000",
      "reporting_to": {
        "id": "431581000000272796"
      },
      "manager": {
        "id": "431581000000258001"
      },
      "permission_type": "read_only",
      "description": "null",
      "account_rule_criteria": {
        "comparator": "greater_than",
        "field": {
          "api_name": "Annual_Revenue",
          "id": "431581000000000625"
        },
        "value": "1001"
      },
      "lead_rule_criteria": {
        "comparator": "greater_than",
        "field": {
          "api_name": "Annual_Revenue",
          "id": "431581000000000893"
        },
        "value": "1000"
      },
      "deal_rule_criteria": {
        "comparator": "greater_than",
        "field": {
          "api_name": "Amount",
          "id": "431581000000000799"
        },
        "value": "100000"
      }
    }
  ]
}
```
