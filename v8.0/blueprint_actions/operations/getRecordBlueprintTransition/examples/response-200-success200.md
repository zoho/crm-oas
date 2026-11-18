Available Blueprint transitions with fields and validations for the record

```json
{
  "blueprint": {
    "process_info": {
      "field_id": "4554588000000000379",
      "api_name": "Rating",
      "field_name": "Rating",
      "field_label": "Rating",
      "column_name": "RATING",
      "field_value": "-None-",
      "escalation": {
        "days": "1",
        "status": "due"
      },
      "continuous": false,
      "name": "Accounts BP 1",
      "current_picklist": {
        "colour_code": null,
        "id": "4554588000000002203",
        "value": "-None-"
      },
      "id": "4554588000001194020"
    },
    "transitions": [
      {
        "next_transitions": [],
        "data": {},
        "type": "manual",
        "criteria_message": null,
        "execution_time": null,
        "sequence": 1,
        "next_field_value": "Acquired",
        "text_color_code": "#FFFFFF",
        "name": "tr1",
        "criteria_matched": true,
        "id": "4554588000001194015",
        "parent_transition": {
          "id": "4554588000001194014",
          "name": "Parent Transition 1"
        },
        "fields": [],
        "color_code": "#2385ef",
        "percent_partial_save": 0,
        "is_accessible": true
      },
      {
        "next_transitions": [],
        "type": "manual",
        "criteria_message": "( ( City is Chennai AND Country isn't India ) AND State isn't TN )",
        "criteria_details": {
          "group_operator": "AND",
          "group": [
            {
              "group_operator": "AND",
              "group": [
                {
                  "comparator": "equal",
                  "field": {
                    "api_name": "City",
                    "id": "4554588000000004419"
                  },
                  "value": "Chennai"
                },
                {
                  "comparator": "not_equal",
                  "field": {
                    "api_name": "Country",
                    "id": "4554588000000004425"
                  },
                  "value": "India"
                }
              ]
            },
            {
              "comparator": "not_equal",
              "field": {
                "api_name": "State",
                "id": "4554588000000004421"
              },
              "value": "TN"
            }
          ]
        },
        "execution_time": null,
        "sequence": 2,
        "next_field_value": "Junk",
        "text_color_code": "#FFFFFF",
        "name": "tr2",
        "criteria_matched": false,
        "id": "4554588000001194016",
        "parent_transition": {
          "id": "4554588000001194014",
          "name": "Parent Transition 1"
        },
        "fields": [],
        "color_code": "#2385ef",
        "percent_partial_save": 0,
        "is_accessible": true
      }
    ]
  }
}
```
