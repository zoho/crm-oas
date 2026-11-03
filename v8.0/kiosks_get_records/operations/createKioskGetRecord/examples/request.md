### `application/json` — CreateChildGetRecord

Create a child-type get record with grouped criteria

```json
{
  "get_records": [
    {
      "name": "GetRecords 3",
      "module": {
        "api_name": "Leads",
        "id": "2296900000010857048",
        "name": "Leads"
      },
      "criteria": {
        "group_operator": "and",
        "group": [
          {
            "field": {
              "api_name": "Annual_Revenue",
              "id": "2296900000010863615",
              "field_label": "Annual Revenue",
              "data_type": "currency",
              "decimal_place": 2
            },
            "comparator": "not_equal",
            "value": {
              "id": "2296900000010863615",
              "api_name": "Annual_Revenue"
            },
            "type": "value"
          },
          {
            "field": {
              "api_name": "City",
              "id": "2296900000010863627",
              "field_label": "City",
              "data_type": "text"
            },
            "comparator": "equal",
            "value": {
              "api_name": "users.last_name",
              "id": "2296900000010863437",
              "data_type": "text"
            },
            "type": "field"
          }
        ]
      },
      "sort_order": {
        "order_by_name": "descending",
        "order_by_field": {
          "display_label": "Modified Time",
          "api_name": "Modified_Time",
          "id": "2296900000010863622"
        }
      },
      "selection_details": {
        "result_type": "multiple",
        "selection_type": "mandate",
        "range": 20,
        "limit": 10
      },
      "selected_fields": [],
      "type": "child",
      "parent_record_field": {
        "id": "2296900000011244175"
      },
      "child_relationship": {
        "id": "2296900000010872872",
        "display_label": "Calls"
      }
    }
  ]
}
```
