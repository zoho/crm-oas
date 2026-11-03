### `application/json` — ScreenStateUpdate

Update a Screen state

```json
{
  "states": [
    {
      "name": "Screen 1",
      "from_transition": {
        "id": "3480060000005475069"
      },
      "type": "screen",
      "details": {
        "screen_details": {
          "button_align": "right_to_left",
          "elements": [
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 1,
                "field_label": "Single Line 1",
                "api_name": "dummy_field_1",
                "required": false,
                "read_only": false,
                "data_type": "text"
              }
            },
            {
              "type": "get_records",
              "value": null,
              "selected_fields": [
                {
                  "api_name": "Last_Name",
                  "id": "3480060000000000559"
                },
                {
                  "api_name": "Company",
                  "id": "3480060000000000555"
                },
                {
                  "api_name": "Email",
                  "id": "3480060000000000563"
                }
              ],
              "open_record": true,
              "ui_type": 133,
              "get_record": {
                "name": "GetRecords 1",
                "id": "3480060000005475080"
              }
            },
            {
              "type": "data_hubs",
              "value": null,
              "data_hub": {
                "ui_type": 133,
                "field_label": "Query 1",
                "id": "3480060000005476254",
                "api_name": "dummy_field_3",
                "required": false,
                "read_only": false,
                "data_type": "lookup"
              }
            },
            {
              "type": "zia_insights",
              "zia_insight": {
                "field_label": "Zia Insights",
                "api_name": "ZiaElement_dummy_0",
                "required": false,
                "read_only": false,
                "component_name": "prediction",
                "parent_record_field": {
                  "id": "3480060000005475080",
                  "api_name": "abc"
                }
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 1,
                "field_label": "Single Line 2",
                "api_name": "dummy_field_7",
                "required": false,
                "read_only": true,
                "_merge_field": "$!users.id",
                "data_type": "text"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 1,
                "field_label": "Single Line 3",
                "api_name": "dummy_field_8",
                "required": false,
                "read_only": false,
                "data_type": "text"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 110,
                "length": 2000,
                "field_label": "Multi-Line 1",
                "api_name": "dummy_field_9",
                "required": true,
                "read_only": false,
                "_merge_field": "$!users.first_name",
                "data_type": "textarea"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 110,
                "length": 2000,
                "field_label": "Multi-Line 2",
                "api_name": "dummy_field_10",
                "required": false,
                "read_only": false,
                "data_type": "textarea",
                "tooltip": {
                  "value": "asdfsdfasdf",
                  "name": "info_icon"
                }
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 33,
                "field_label": "Phone 1",
                "api_name": "dummy_field_11",
                "required": false,
                "read_only": false,
                "_merge_field": "$!users.phone",
                "data_type": "phone",
                "tooltip": {
                  "value": "dskhjafbkjsfd",
                  "name": "static_text"
                }
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 33,
                "field_label": "Phone 2",
                "api_name": "dummy_field_12",
                "required": false,
                "read_only": false,
                "data_type": "phone"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 32,
                "length": 9,
                "field_label": "Number 1",
                "api_name": "dummy_field_13",
                "required": false,
                "read_only": false,
                "data_type": "integer"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 36,
                "length": 16,
                "decimal_place": 2,
                "currency": {
                  "rounding_option": "normal",
                  "precision": 2
                },
                "field_label": "Currency 1",
                "api_name": "dummy_field_14",
                "required": false,
                "read_only": false,
                "data_type": "currency"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 143,
                "length": 16,
                "decimal_place": 2,
                "currency": {
                  "rounding_option": "round_off",
                  "precision": 2
                },
                "field_label": "Currency 2",
                "api_name": "dummy_field_15",
                "required": false,
                "read_only": false,
                "data_type": "currency",
                "tooltip": {
                  "value": "asdf",
                  "name": "info_icon"
                }
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 38,
                "length": 16,
                "number_separator": true,
                "decimal_place": 2,
                "field_label": "Decimal 3",
                "api_name": "dummy_field_16",
                "required": false,
                "read_only": false,
                "data_type": "double"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 38,
                "length": 10,
                "number_separator": false,
                "decimal_place": 1,
                "field_label": "Decimal 4",
                "api_name": "dummy_field_17",
                "required": false,
                "read_only": false,
                "data_type": "double"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 34,
                "field_label": "Percent 3",
                "api_name": "dummy_field_18",
                "required": false,
                "read_only": false,
                "data_type": "percent"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 21,
                "length": 450,
                "field_label": "URL 1",
                "api_name": "dummy_field_19",
                "required": false,
                "read_only": false,
                "data_type": "website"
              }
            },
            {
              "type": "field",
              "value": true,
              "field": {
                "value": true,
                "ui_type": 301,
                "field_label": "Checkbox 1",
                "api_name": "dummy_field_20",
                "required": false,
                "read_only": false,
                "data_type": "boolean"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "value": false,
                "ui_type": 301,
                "field_label": "Checkbox 2",
                "api_name": "dummy_field_21",
                "required": false,
                "read_only": false,
                "data_type": "boolean"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 25,
                "field_label": "Email 1",
                "api_name": "dummy_field_22",
                "required": false,
                "read_only": false,
                "data_type": "email"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 202,
                "field_label": "Date 1",
                "api_name": "dummy_field_23",
                "required": false,
                "read_only": false,
                "data_type": "date"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 333,
                "field_label": "Date/Time 1",
                "api_name": "dummy_field_24",
                "required": false,
                "read_only": false,
                "data_type": "datetime"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 2,
                "field_label": "Pick List 1",
                "api_name": "dummy_field_25",
                "required": false,
                "read_only": false,
                "pick_list_values": [
                  {
                    "display_value": "Option 1",
                    "actual_value": "Option 1"
                  },
                  {
                    "display_value": "Option 2",
                    "actual_value": "Option 2"
                  },
                  {
                    "actual_value": "Option 3",
                    "display_value": "Option 3"
                  }
                ],
                "_pick_list_type": "local",
                "data_type": "picklist"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 2,
                "field_label": "Pick List 2",
                "api_name": "dummy_field_26",
                "required": false,
                "read_only": false,
                "pick_list_values": [
                  {
                    "display_value": "-None-",
                    "actual_value": "-None-"
                  },
                  {
                    "display_value": "Advertisement",
                    "actual_value": "Advertisement"
                  },
                  {
                    "display_value": "Cold Call",
                    "actual_value": "Cold Call"
                  },
                  {
                    "display_value": "Employee Referral",
                    "actual_value": "Employee Referral"
                  },
                  {
                    "display_value": "External Referral",
                    "actual_value": "External Referral"
                  },
                  {
                    "display_value": "Public Relations",
                    "actual_value": "Public Relations"
                  },
                  {
                    "display_value": "Trade Show",
                    "actual_value": "Trade Show"
                  },
                  {
                    "display_value": "Seminar Partner",
                    "actual_value": "Seminar Partner"
                  },
                  {
                    "display_value": "Online Store",
                    "actual_value": "Online Store"
                  },
                  {
                    "display_value": "Chat",
                    "actual_value": "Chat"
                  },
                  {
                    "display_value": "Sales Email Alias",
                    "actual_value": "Sales Email Alias"
                  },
                  {
                    "display_value": "Internal Seminar",
                    "actual_value": "Internal Seminar"
                  },
                  {
                    "display_value": "Web Download",
                    "actual_value": "Web Download"
                  },
                  {
                    "display_value": "Web Research",
                    "actual_value": "Web Research"
                  },
                  {
                    "display_value": "X (Twitter)",
                    "actual_value": "X (Twitter)"
                  },
                  {
                    "display_value": "Facebook",
                    "actual_value": "Facebook"
                  },
                  {
                    "display_value": "Partner",
                    "actual_value": "Partner"
                  }
                ],
                "_pick_list_type": "global_set",
                "data_type": "picklist",
                "global_picklist": {
                  "api_name": "Source",
                  "id": "3480060000000491019"
                }
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 100,
                "field_label": "Multi-Select 1",
                "api_name": "dummy_field_27",
                "required": false,
                "read_only": false,
                "pick_list_values": [
                  {
                    "display_value": "Option 1",
                    "actual_value": "Option 1"
                  },
                  {
                    "display_value": "Option 2",
                    "actual_value": "Option 2"
                  },
                  {
                    "actual_value": "Option 3",
                    "display_value": "Option 3"
                  }
                ],
                "data_type": "multiselectpicklist"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 221,
                "field_label": "User Lookup 1",
                "api_name": "dummy_field_28",
                "required": false,
                "read_only": false,
                "data_type": "userlookup"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 555,
                "length": 1,
                "field_label": "File Upload 1",
                "api_name": "dummy_field_29",
                "required": false,
                "read_only": false,
                "data_type": "fileupload"
              }
            },
            {
              "type": "field",
              "value": null,
              "field": {
                "ui_type": 555,
                "length": 5,
                "field_label": "File Upload 2",
                "api_name": "dummy_field_30",
                "required": false,
                "read_only": false,
                "data_type": "fileupload",
                "allow_multiple_upload": true
              }
            }
          ],
          "buttons": [
            {
              "name": "Done",
              "prop_name": "primary"
            }
          ],
          "width": "670px",
          "title": "Screen 1"
        }
      }
    }
  ]
}
```

### `application/json` — DecisionStateUpdate

Update a Decision state

```json
{
  "states": [
    {
      "name": "Decision 2",
      "type": "decision",
      "details": {
        "path_details": [
          {
            "name": "Path 1",
            "id": "5113009000000745339",
            "default": false,
            "filter_conditions": {
              "pattern": "(((((1and2)and3))and4))",
              "criteria_groupings": [
                {
                  "type": "kiosk_fields",
                  "value": "${NOTEMPTY}",
                  "criteria": {
                    "field": {
                      "api_name": "Last_Name",
                      "id": "5113009000000744601",
                      "field_label": "Last Name",
                      "data_type": "text"
                    },
                    "comparator": "equal",
                    "value": "sampleupdated",
                    "type": "value"
                  },
                  "sequence_number": 1
                },
                {
                  "type": "kiosk_fields",
                  "value": "${NOTEMPTY}",
                  "criteria": {
                    "field": {
                      "api_name": "Title",
                      "id": "5113009000000744727",
                      "field_label": "Title",
                      "data_type": "text"
                    },
                    "comparator": "equal",
                    "value": "updatedtitle",
                    "type": "value"
                  },
                  "sequence_number": 2
                },
                {
                  "type": "kiosk_fields",
                  "value": "${NOTEMPTY}",
                  "criteria": {
                    "group_operator": "and",
                    "group": [
                      {
                        "group_operator": "and",
                        "group": [
                          {
                            "field": {
                              "api_name": "Address",
                              "id": "5113009000000744608",
                              "field_label": "Address",
                              "data_type": "textarea"
                            },
                            "comparator": "equal",
                            "value": "zoho",
                            "type": "value"
                          },
                          {
                            "field": {
                              "api_name": "Completed",
                              "id": "5113009000000744734",
                              "field_label": "Completed",
                              "data_type": "boolean"
                            },
                            "comparator": "equal",
                            "value": "true",
                            "type": "value"
                          }
                        ]
                      },
                      {
                        "field": {
                          "api_name": "Number",
                          "id": "5113009000000744622",
                          "field_label": "Number",
                          "data_type": "integer"
                        },
                        "comparator": "equal",
                        "value": "hello",
                        "type": "field"
                      }
                    ]
                  },
                  "sequence_number": 3
                },
                {
                  "type": "current_record",
                  "value": "${NOTEMPTY}",
                  "criteria": {
                    "field": {
                      "api_name": "Full_Name",
                      "id": "5113009000000000485",
                      "field_label": "Contact Name",
                      "data_type": "text"
                    },
                    "comparator": "equal",
                    "value": "Rishabh",
                    "type": "value"
                  },
                  "sequence_number": 4
                }
              ]
            }
          }
        ]
      },
      "id": "5113009000000745358"
    }
  ]
}
```

### `application/json` — ActionStateUpdate

Update an Action state

```json
{
  "states": [
    {
      "name": "Action 1",
      "from_transition": {
        "id": "3480060000005475069"
      },
      "type": "action",
      "details": {
        "type": "field_updates",
        "execute_for_record": {
          "name": "GetRecords 1",
          "id": "4676645000001212047"
        },
        "get_record": {
          "id": "467664500000121204",
          "name": "GetRecords 5"
        },
        "field_updates": {
          "id": "4676645000001212731",
          "name": "Action 1"
        }
      }
    }
  ]
}
```

### `application/json` — GetRecordsStateUpdate

Update a Get Records state

```json
{
  "states": [
    {
      "name": "GetRecords 2",
      "from_transition": {
        "id": "3480060000005475069"
      },
      "type": "get_records",
      "details": {
        "get_record": {
          "id": "2296900000011011184",
          "name": "GetRecords 2"
        }
      }
    }
  ]
}
```
