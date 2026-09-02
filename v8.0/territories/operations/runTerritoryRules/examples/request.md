### `application/json` — RunRulesExample

Criteria-based territory rule execution for a module

```json
{
  "run_rules": {
    "based_on": "criteria",
    "criteria": {
      "comparator": "equal",
      "field": {
        "api_name": "Account_Name"
      },
      "value": "test"
    },
    "module": {
      "id": "11111000736439"
    }
  }
}
```
