### `application/json` — SamplePutRequest

Sample request body

```json
{
  "transitions": [
    {
      "name": "Test Transition",
      "id": "1234567890123",
      "description": "Test Transition Description",
      "trigger_type": "manual",
      "transition_type": "standalone_transition",
      "color_code": "#F27E22",
      "module": {
        "api_name": "Leads",
        "id": "111112000000000030"
      },
      "during_inputs": [
        {
          "type": "notes",
          "optional": false,
          "sequence": 1,
          "field": {
            "api_name": "Account_Name",
            "id": "111111000000059320"
          },
          "message": "new message added",
          "validation_filter": {
            "validation_message": "Amount revenue should be more than 1000",
            "criteria": {
              "field": {
                "api_name": "Lead Lookup.Amount",
                "id": "111111000000059321"
              },
              "comparator": "greater_than",
              "value": "1000"
            }
          },
          "configured_fields": [
            {
              "field": {
                "api_name": "Subject",
                "id": "111111000000059420"
              },
              "optional": false
            },
            {
              "field": {
                "api_name": "Priority",
                "id": "111111000000059421"
              },
              "validation_filter": {
                "validation_message": "priority should be high or highest or low or lowest",
                "criteria": {
                  "field": {
                    "api_name": "Lead Lookup.Amount",
                    "id": "111111000000059321"
                  },
                  "comparator": "greater_than",
                  "value": "1000"
                }
              },
              "optional": false
            }
          ],
          "related_list": {
            "id": "111111000000078890",
            "name": "Tasks",
            "module": {
              "id": "111111000000059891",
              "api_name": "Tasks"
            },
            "layout": {
              "id": "111111000000058891",
              "api_name": "standard"
            }
          },
          "title": "Check List",
          "items": [
            {
              "name": "Item 1",
              "optional": true,
              "sequence": 1
            },
            {
              "name": "Item 2",
              "optional": false,
              "sequence": 2
            }
          ],
          "kiosk": {
            "id": "13212313000002323",
            "name": "kiosk name"
          }
        },
        {
          "type": "attachment",
          "optional": true,
          "sequence": 2
        },
        {
          "type": "tags",
          "optional": false,
          "sequence": 3
        },
        {
          "type": "info",
          "optional": false,
          "sequence": 4,
          "message": "new message added"
        },
        {
          "type": "field",
          "field": {
            "api_name": "Account_Name",
            "id": "111111000000059320"
          },
          "optional": false,
          "sequence": 4
        },
        {
          "type": "field",
          "field": {
            "api_name": "Lead_Lookup.Amount",
            "id": "111111000000059321"
          },
          "optional": true,
          "sequence": 5,
          "validation_filter": {
            "validation_message": "Amount revenue should be more than 1000",
            "criteria": {
              "field": {
                "api_name": "Lead Lookup.Amount",
                "id": "111111000000059321"
              },
              "comparator": "greater_than",
              "value": "1000"
            }
          }
        },
        {
          "type": "related_list",
          "sequence": 6,
          "related_list": {
            "id": "111111000000078890",
            "name": "Tasks",
            "module": {
              "id": "111111000000059891",
              "api_name": "Tasks"
            },
            "layout": {
              "id": "111111000000058891",
              "api_name": "standard"
            }
          },
          "configured_fields": [
            {
              "field": {
                "api_name": "Subject",
                "id": "111111000000059420"
              },
              "optional": false
            },
            {
              "field": {
                "api_name": "Priority",
                "id": "111111000000059421"
              },
              "validation_filter": {
                "validation_message": "priority should be high or highest or low or lowest",
                "criteria": {
                  "field": {
                    "api_name": "Lead Lookup.Amount",
                    "id": "111111000000059321"
                  },
                  "comparator": "greater_than",
                  "value": "1000"
                }
              },
              "optional": false
            }
          ]
        },
        {
          "type": "kiosk",
          "sequence": 1,
          "optional": false,
          "kiosk": {
            "id": "13212313000002323",
            "name": "kiosk name"
          }
        },
        {
          "type": "related_list",
          "sequence": 7,
          "related_list": {
            "id": "111111000000078890",
            "name": "Quote_Lead_RL",
            "module": {
              "id": "111111000000059891",
              "api_name": "Quotes"
            },
            "layout": {
              "id": "111111000000058891",
              "api_name": "standard"
            }
          },
          "configured_fields": [
            {
              "field": {
                "api_name": "Subject",
                "id": "111111000000059422"
              },
              "validation_filter": null,
              "optional": false
            },
            {
              "name": "Quoted_Items",
              "optional": false,
              "subform_fields": [
                {
                  "field": {
                    "api_name": "Subject",
                    "id": "111111000000059422"
                  },
                  "validation_filter": null,
                  "optional": false
                },
                {
                  "field": {
                    "api_name": "Product_Name",
                    "id": "111111000000059423"
                  },
                  "validation_filter": null,
                  "optional": false
                },
                {
                  "field": {
                    "api_name": "List_Price",
                    "id": "111111000000059424"
                  },
                  "validation_filter": null,
                  "optional": false
                }
              ]
            }
          ]
        },
        {
          "type": "checklist",
          "title": "Check List",
          "items": [
            {
              "name": "Item 1",
              "optional": true,
              "sequence": 1
            },
            {
              "name": "Item 2",
              "optional": false,
              "sequence": 2
            }
          ],
          "optional": false,
          "sequence": 8
        }
      ],
      "actions": [
        {
          "type": "field_updates",
          "id": "111111000000059424"
        },
        {
          "type": "add_tags",
          "details": {
            "module": {
              "id": "111111000000059420",
              "api_name": "Contacts"
            },
            "tags": [
              {
                "name": "testtag",
                "color": "#0000FF"
              },
              {
                "name": "tag1",
                "color": "#800080"
              }
            ],
            "overwrite": true
          },
          "name": null,
          "id": "111111000000059424"
        },
        {
          "type": "email_notifications",
          "id": "111111000000059424"
        },
        {
          "type": "tasks",
          "id": "111111000000059424"
        }
      ],
      "owners": [
        {
          "type": "users",
          "resources": [
            {
              "id": "111111000000000039"
            },
            {
              "id": "111111000000000039"
            }
          ]
        },
        {
          "type": "role",
          "resources": [
            {
              "id": "111111000000000241"
            }
          ]
        },
        {
          "type": "group",
          "resources": [
            {
              "id": "111111000000059384"
            }
          ]
        },
        {
          "type": "record_owner",
          "resources": []
        },
        {
          "type": "portal_user_type",
          "resources": [
            {
              "id": "111111000000059396"
            }
          ]
        }
      ],
      "criteria": {
        "group_operator": "and",
        "group": [
          {
            "group_operator": "and",
            "group": [
              {
                "comparator": "equal",
                "field": {
                  "api_name": "Annual_Revenue",
                  "id": "111111000000059456"
                },
                "value": "20000"
              },
              {
                "comparator": "not_equal",
                "field": {
                  "api_name": "City",
                  "id": "111111000000059434"
                },
                "value": "Chennai"
              }
            ]
          }
        ]
      }
    }
  ]
}
```
