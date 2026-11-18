### `application/json` — SamplePostRequest

Create a Blueprint

```json
{
  "blueprints": [
    {
      "owners": [
        {
          "resources": [
            {
              "id": "1231231231"
            }
          ],
          "type": "users"
        }
      ],
      "criteria": {
        "comparator": "greater_than",
        "field": {
          "api_name": "Annual_Revenue",
          "id": "111111000000004782"
        },
        "type": "value",
        "value": "100"
      },
      "chart_data": {
        "nodes": [
          {
            "position_x": 330,
            "position_y": 340,
            "state": {
              "api_name": "State_1"
            }
          },
          {
            "position_x": 880,
            "position_y": 320,
            "state": {
              "api_name": "State_2"
            }
          }
        ],
        "canvas_size": {
          "width": 1374,
          "height": 922
        },
        "connections": [
          {
            "from": {
              "end_point": {
                "position_x": 0.5,
                "position_y": 1,
                "direction_x": 0,
                "direction_y": 1
              },
              "state": {
                "api_name": "State_1"
              }
            },
            "api_name": "Transition_1",
            "to": {
              "end_point": {
                "position_x": 0,
                "position_y": 0.5,
                "direction_x": 0,
                "direction_y": 0
              },
              "state": {
                "api_name": "State_2"
              }
            },
            "transition": {
              "api_name": "Transition_1",
              "name": "Transition 1"
            }
          }
        ]
      },
      "continuous": false,
      "module": {
        "api_name": "Leads",
        "id": "111111000000002624",
        "precedence": 1
      },
      "pipeline": {
        "id": "111111000000007865",
        "api_name": "Initial Stages",
        "display_value": "Initial Stages"
      },
      "transitions": [
        {
          "criteria": {
            "comparator": "greater_than",
            "field": {
              "api_name": "Annual_Revenue",
              "id": "111111000000004782"
            },
            "type": "value",
            "value": "100"
          },
          "trigger_type": "manual",
          "module": {
            "api_name": "Leads",
            "id": "111111000000002594"
          },
          "layout": {
            "api_name": "Standard__s",
            "name": "Standard",
            "id": "111111000000003620"
          },
          "description": "Test Transition",
          "owners": [
            {
              "resources": [
                {
                  "id": "1231231231"
                }
              ],
              "type": "users"
            }
          ],
          "common": true,
          "include_states": [
            {
              "state": {
                "name": "Option 9",
                "api_name": "111111000000085130"
              }
            }
          ],
          "during_inputs": [
            {
              "validation_filter": {
                "criteria": {
                  "comparator": "greater_than",
                  "field": {
                    "api_name": "Annual_Revenue",
                    "id": "111111000000004782"
                  },
                  "type": "value",
                  "value": "100"
                },
                "validation_message": "Test Message"
              },
              "sequence": 1,
              "field": {
                "api_name": "Designation",
                "id": "111111000000004762"
              },
              "optional": false,
              "type": "field"
            },
            {
              "sequence": 2,
              "optional": true,
              "type": "checklist",
              "title": null,
              "items": [
                {
                  "sequence": 1,
                  "name": "Item 1",
                  "optional": false
                },
                {
                  "sequence": 2,
                  "name": "Item 2",
                  "optional": false
                },
                {
                  "sequence": 3,
                  "name": "Item 3",
                  "optional": false
                }
              ]
            },
            {
              "sequence": 3,
              "configured_fields": [
                {
                  "validation_filter": null,
                  "handler": {},
                  "sequence": 1,
                  "field": {
                    "api_name": "Subject",
                    "id": "111111000000004028"
                  },
                  "optional": false,
                  "id": "111111000000077406"
                }
              ],
              "optional": true,
              "id": null,
              "type": "related_list",
              "related_list": {
                "module": {
                  "api_name": "111111000000002616",
                  "id": "111111000000002616"
                },
                "id": "Tasks"
              }
            }
          ],
          "api_name": "Transition_1",
          "name": "Transition 1",
          "transition_type": "standalone_transition",
          "actions": [
            {
              "id": "111111000000077438",
              "type": "tasks"
            },
            {
              "id": "111111000000077429",
              "type": "email_notifications"
            },
            {
              "id": "111111000000077442",
              "type": "field_updates"
            }
          ],
          "color_code": "#2385ef"
        }
      ],
      "states": [
        {
          "name": "Contacted",
          "api_name": "State_2",
          "pick_list_value": {
            "id": "111111000000007311",
            "actual_value": "Contacted"
          },
          "module": {
            "api_name": "Leads",
            "id": "111111000000002624"
          },
          "state_escalation": {
            "period": "days",
            "value": 10,
            "trigger_details": [
              {
                "period": "days",
                "execute_type": "on",
                "value": 1,
                "actions": [
                  {
                    "details": {
                      "escalate_to": [
                        {
                          "id": "111111000000057619",
                          "type": "user"
                        }
                      ],
                      "id": "111111000000077429",
                      "name": "SLA"
                    },
                    "id": "111111000000077429",
                    "name": "SLA",
                    "type": "sla"
                  },
                  {
                    "name": "Test Mail",
                    "details": {
                      "name": "Test Mail",
                      "id": "111111000000077429"
                    },
                    "id": "111111000000077429",
                    "type": "email_notifications"
                  }
                ]
              }
            ]
          }
        },
        {
          "name": "-None-",
          "api_name": "State_1",
          "pick_list_value": {
            "id": "111111000000007321"
          },
          "module": {
            "api_name": "Leads",
            "id": "111111000000002624"
          }
        }
      ],
      "layout": {
        "api_name": "Standard__s",
        "name": "Standard",
        "id": "111111000000003620"
      },
      "field": {
        "api_name": "Lead_Status",
        "field_label": "Lead Status",
        "id": "111111000000004796"
      },
      "api_name": "Lead_Bp_1",
      "name": "Lead Bp 1",
      "description": "Test description",
      "connections": [
        {
          "to_state": {
            "name": "Contacted",
            "api_name": "State_2"
          },
          "api_name": "Transition_1",
          "transitions": {
            "api_name": "Transition_1",
            "name": "Transition 1",
            "precedence": 1
          },
          "from_state": {
            "name": "-None-",
            "api_name": "State_1"
          }
        }
      ]
    }
  ]
}
```
