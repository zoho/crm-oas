### `application/json` — ValidWizardCreation

Valid request creating a wizard with 3 screens

```json
{
  "wizards": [
    {
      "containers": [
        {
          "screens": [
            {
              "segments": [
                {
                  "display_label": "Contact Information",
                  "elements": [
                    {
                      "type": "field",
                      "resource": {
                        "name": "Owner",
                        "id": "111113000000004564"
                      },
                      "sequence_number": 1
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Lead_Source",
                        "id": "111113000000004566"
                      },
                      "sequence_number": 2
                    },
                    {
                      "resource": {
                        "id": "111113000000004622",
                        "name": "Salutation"
                      },
                      "sequence_number": 0,
                      "type": "field"
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "First_Name",
                        "id": "111113000000004568"
                      },
                      "sequence_number": 3
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Last_Name",
                        "id": "111113000000004570"
                      },
                      "sequence_number": 4
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Account_Name",
                        "id": "111113000000004574"
                      },
                      "sequence_number": 5
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Vendor_Name",
                        "id": "111113000000004576"
                      },
                      "sequence_number": 6
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Email",
                        "id": "111113000000004578"
                      },
                      "sequence_number": 7
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Title",
                        "id": "111113000000004582"
                      },
                      "sequence_number": 8
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Department",
                        "id": "111113000000004584"
                      },
                      "sequence_number": 9
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Phone",
                        "id": "111113000000004586"
                      },
                      "sequence_number": 10
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Home_Phone",
                        "id": "111113000000004588"
                      },
                      "sequence_number": 11
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Other_Phone",
                        "id": "111113000000004590"
                      },
                      "sequence_number": 12
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Fax",
                        "id": "111113000000004592"
                      },
                      "sequence_number": 13
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Mobile",
                        "id": "111113000000004594"
                      },
                      "sequence_number": 14
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Date_of_Birth",
                        "id": "111113000000004596"
                      },
                      "sequence_number": 15
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Assistant",
                        "id": "111113000000004598"
                      },
                      "sequence_number": 16
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Asst_Phone",
                        "id": "111113000000004600"
                      },
                      "sequence_number": 17
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Reporting_To",
                        "id": "111113000000004602"
                      },
                      "sequence_number": 18
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Email_Opt_Out",
                        "id": "111113000000004604"
                      },
                      "sequence_number": 19
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Skype_ID",
                        "id": "111113000000004606"
                      },
                      "sequence_number": 20
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Secondary_Email",
                        "id": "111113000000004624"
                      },
                      "sequence_number": 21
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Twitter",
                        "id": "111113000000004632"
                      },
                      "sequence_number": 22
                    }
                  ],
                  "name": "Contact Information",
                  "type": "composite",
                  "sequence_number": 2,
                  "reference_id": "{{52253}}"
                },
                {
                  "display_label": "Title of Screen 1",
                  "content": "Hi ${!Contacts.Last_Name} \nWelcome to Screen 1",
                  "type": "text_label",
                  "sequence_number": 1,
                  "reference_id": "{{35303}}"
                },
                {
                  "display_label": "Dummy",
                  "buttons": [
                    {
                      "display_label": "Next",
                      "sequence_number": 1,
                      "shape": "capsule",
                      "background_color": "#00A3F3",
                      "color": "#fff",
                      "type": "transition",
                      "category": "wizard_button",
                      "visibility": "show",
                      "reference_id": "{{42315}}",
                      "target_screen": {
                        "reference_id": "{{77454}}",
                        "display_label": "Screen 2"
                      }
                    }
                  ],
                  "name": "Dummy",
                  "type": "buttons",
                  "sequence_number": 3,
                  "reference_id": "{{34468}}"
                }
              ],
              "conditional_rules": [
                {
                  "actions": [
                    {
                      "type": "set_mandatory",
                      "field": {
                        "id": "111113000000004632"
                      }
                    }
                  ],
                  "criteria": {
                    "field": {
                      "api_name": "Skype_ID",
                      "id": "111113000000004606"
                    },
                    "comparator": "not_equal",
                    "value": "${EMPTY}",
                    "type": "value"
                  },
                  "execute_on": "create_edit"
                }
              ],
              "display_label": "Screen 1",
              "reference_id": "{{51388}}"
            },
            {
              "segments": [
                {
                  "display_label": "Address Information",
                  "elements": [
                    {
                      "type": "field",
                      "resource": {
                        "name": "Mailing_Street",
                        "id": "111113000000004666"
                      },
                      "sequence_number": 1
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Other_Street",
                        "id": "111113000000004668"
                      },
                      "sequence_number": 2
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Mailing_City",
                        "id": "111113000000004670"
                      },
                      "sequence_number": 3
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Other_City",
                        "id": "111113000000004672"
                      },
                      "sequence_number": 4
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Mailing_State",
                        "id": "111113000000004674"
                      },
                      "sequence_number": 5
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Other_State",
                        "id": "111113000000004676"
                      },
                      "sequence_number": 6
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Mailing_Zip",
                        "id": "111113000000004678"
                      },
                      "sequence_number": 7
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Other_Zip",
                        "id": "111113000000004680"
                      },
                      "sequence_number": 8
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Mailing_Country",
                        "id": "111113000000004682"
                      },
                      "sequence_number": 9
                    },
                    {
                      "type": "field",
                      "resource": {
                        "name": "Other_Country",
                        "id": "111113000000004684"
                      },
                      "sequence_number": 10
                    }
                  ],
                  "name": "Address Information",
                  "type": "composite",
                  "sequence_number": 1,
                  "reference_id": "{{93069}}"
                },
                {
                  "display_label": "Dummy",
                  "buttons": [
                    {
                      "display_label": "Next",
                      "sequence_number": 1,
                      "shape": "capsule",
                      "background_color": "#00A3F3",
                      "color": "#fff",
                      "type": "transition",
                      "category": "wizard_button",
                      "visibility": "show",
                      "reference_id": "{{12356}}",
                      "target_screen": {
                        "reference_id": "{{64996}}",
                        "display_label": "Screen 3"
                      }
                    }
                  ],
                  "name": "Dummy",
                  "type": "buttons",
                  "sequence_number": 2,
                  "reference_id": "{{39718}}"
                }
              ],
              "display_label": "Screen 2",
              "reference_id": "{{77454}}"
            },
            {
              "segments": [
                {
                  "display_label": "Description Information",
                  "elements": [
                    {
                      "type": "field",
                      "resource": {
                        "name": "Description",
                        "id": "111113000000004686"
                      },
                      "sequence_number": 1
                    }
                  ],
                  "name": "Description Information",
                  "type": "composite",
                  "sequence_number": 1,
                  "reference_id": "{{79174}}"
                },
                {
                  "display_label": "Dummy",
                  "buttons": [
                    {
                      "display_label": "Save",
                      "sequence_number": 1,
                      "shape": "capsule",
                      "background_color": "#00A3F3",
                      "color": "#fff",
                      "type": "save",
                      "category": "wizard_button",
                      "visibility": "show",
                      "reference_id": "{{3520}}"
                    }
                  ],
                  "name": "Dummy",
                  "type": "buttons",
                  "sequence_number": 2,
                  "reference_id": "{{18525}}"
                }
              ],
              "display_label": "Screen 3",
              "reference_id": "{{64996}}"
            }
          ],
          "layout": {
            "id": "111113000000003656",
            "name": "Standard"
          },
          "chart_data": {
            "nodes": [
              {
                "pos_x": 637,
                "pos_y": 108,
                "start_node": true,
                "screen": {
                  "reference_id": "{{51388}}",
                  "display_label": "Screen 1"
                }
              },
              {
                "pos_x": 957,
                "pos_y": 218,
                "start_node": false,
                "screen": {
                  "reference_id": "{{77454}}",
                  "display_label": "Screen 2"
                }
              },
              {
                "pos_x": 637,
                "pos_y": 328,
                "start_node": false,
                "screen": {
                  "reference_id": "{{64996}}",
                  "display_label": "Screen 3"
                }
              }
            ],
            "connections": [
              {
                "source_button": {
                  "reference_id": "{{42315}}",
                  "display_label": "Next"
                },
                "target_screen": {
                  "reference_id": "{{77454}}",
                  "display_label": "Screen 2"
                }
              },
              {
                "source_button": {
                  "reference_id": "{{12356}}",
                  "display_label": "Next"
                },
                "target_screen": {
                  "reference_id": "{{64996}}",
                  "display_label": "Screen 3"
                }
              }
            ],
            "color_palette": {
              "button_background": [
                "#ADD9FF",
                "#C4F0B3",
                "#FFD6BC",
                "#F8E199",
                "#FFC6C6"
              ]
            }
          }
        }
      ],
      "name": "Harry Potter",
      "module": {
        "id": "111113000000002652",
        "api_name": "Contacts"
      },
      "active": true,
      "profiles": [
        {
          "id": "111113000000000501",
          "name": "Administrator"
        }
      ]
    }
  ]
}
```
