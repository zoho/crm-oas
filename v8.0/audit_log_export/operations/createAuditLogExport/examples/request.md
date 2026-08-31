### `application/json` — Default

Create audit log export with criteria filters.

```json
{
  "audit_log_export": [
    {
      "criteria": {
        "group_operator": "and",
        "group": [
          {
            "field": {
              "api_name": "module"
            },
            "comparator": "in",
            "value": [
              {
                "api_name": "Leads"
              },
              {
                "api_name": "Contacts"
              }
            ]
          },
          {
            "field": {
              "api_name": "action"
            },
            "comparator": "in",
            "value": [
              "added",
              "updated"
            ]
          }
        ]
      }
    }
  ]
}
```
