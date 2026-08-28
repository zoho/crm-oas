# Examples: getWizardDetails

**GET /settings/wizards/{id}**

## Response examples

### Status `200` — `application/json` — WizardDetailsForLayout

Detailed wizard definition for a specific layout.

```json
{
  "wizards": [
    {
      "display_label": "Harry Potter",
      "created_time": "2025-11-28T12:15:16+05:30",
      "modified_time": "2025-11-28T12:15:16+05:30",
      "module": {
        "api_name": "Contacts",
        "id": "111113000000002652"
      },
      "name": "Harry Potter",
      "modified_by": {
        "name": "Drogon Nine",
        "id": "111113000000057672"
      },
      "profiles": [
        {
          "display_label": "Administrator",
          "name": "Administrator",
          "id": "111113000000000501"
        }
      ],
      "active": true,
      "source": "crm",
      "portal_user_types": null,
      "id": "111113000000106221",
      "created_by": {
        "name": "Drogon Nine",
        "id": "111113000000057672"
      },
      "containers": [
        {
          "layout": {
            "display_label": "Standard",
            "name": "Standard",
            "id": "111113000000003656"
          },
          "chart_data": {
            "nodes": [
              {
                "pos_y": 108,
                "pos_x": 637,
                "start_node": true,
                "screen": {
                  "display_label": "Screen 1",
                  "id": "111113000000106223"
                }
              },
              {
                "pos_y": 218,
                "pos_x": 957,
                "start_node": false,
                "screen": {
                  "display_label": "Screen 2",
                  "id": "111113000000106225"
                }
              },
              {
                "pos_y": 328,
                "pos_x": 637,
                "start_node": false,
                "screen": {
                  "display_label": "Screen 3",
                  "id": "111113000000106227"
                }
              }
            ],
            "connections": [
              {
                "source_screen": {
                  "display_label": "Screen 2",
                  "id": "111113000000106225"
                },
                "target_screen": {
                  "display_label": "Screen 3",
                  "id": "111113000000106227"
                },
                "id": "111113000000106411"
              },
              {
                "source_screen": {
                  "display_label": "Screen 1",
                  "id": "111113000000106223"
                },
                "target_screen": {
                  "display_label": "Screen 2",
                  "id": "111113000000106225"
                },
                "id": "111113000000106413"
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
          },
          "screens": [
            {
              "display_label": "Screen 1",
              "api_name": "Screen_1",
              "id": "111113000000106223",
              "conditional_rules": [
                {
                  "query_id": "111113000000106338",
                  "criteria": {
                    "comparator": "not_equal",
                    "field": {
                      "api_name": "Skype_ID",
                      "id": "111113000000004606"
                    },
                    "type": "value",
                    "value": "${EMPTY}"
                  },
                  "actions": [
                    {
                      "field": {
                        "api_name": "Twitter",
                        "id": "111113000000004632"
                      },
                      "id": "111113000000106351",
                      "type": "set_mandatory"
                    }
                  ],
                  "execute_on": "create_edit"
                }
              ],
              "segments": [
                {
                  "sequence_number": 1,
                  "display_label": "Title of Screen 1",
                  "column_count": 2,
                  "name": "Text_1",
                  "id": "111113000000106234",
                  "type": "text_label",
                  "content": "Hi ${!Contacts.Last_Name} \nWelcome to Screen 1"
                },
                {
                  "sequence_number": 2,
                  "display_label": "Contact Information",
                  "column_count": 2,
                  "elements": [
                    {
                      "sequence_number": 0,
                      "resource": {
                        "name": "Salutation",
                        "id": "111113000000004622"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 1,
                      "resource": {
                        "name": "Owner",
                        "id": "111113000000004564"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 2,
                      "resource": {
                        "name": "Lead_Source",
                        "id": "111113000000004566"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 3,
                      "resource": {
                        "name": "First_Name",
                        "id": "111113000000004568"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 4,
                      "resource": {
                        "name": "Last_Name",
                        "id": "111113000000004570"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 5,
                      "resource": {
                        "name": "Account_Name",
                        "id": "111113000000004574"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 6,
                      "resource": {
                        "name": "Vendor_Name",
                        "id": "111113000000004576"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 7,
                      "resource": {
                        "name": "Email",
                        "id": "111113000000004578"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 8,
                      "resource": {
                        "name": "Title",
                        "id": "111113000000004582"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 9,
                      "resource": {
                        "name": "Department",
                        "id": "111113000000004584"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 10,
                      "resource": {
                        "name": "Phone",
                        "id": "111113000000004586"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 11,
                      "resource": {
                        "name": "Home_Phone",
                        "id": "111113000000004588"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 12,
                      "resource": {
                        "name": "Other_Phone",
                        "id": "111113000000004590"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 13,
                      "resource": {
                        "name": "Fax",
                        "id": "111113000000004592"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 14,
                      "resource": {
                        "name": "Mobile",
                        "id": "111113000000004594"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 15,
                      "resource": {
                        "name": "Date_of_Birth",
                        "id": "111113000000004596"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 16,
                      "resource": {
                        "name": "Assistant",
                        "id": "111113000000004598"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 17,
                      "resource": {
                        "name": "Asst_Phone",
                        "id": "111113000000004600"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 18,
                      "resource": {
                        "name": "Reporting_To",
                        "id": "111113000000004602"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 19,
                      "resource": {
                        "name": "Email_Opt_Out",
                        "id": "111113000000004604"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 20,
                      "resource": {
                        "name": "Skype_ID",
                        "id": "111113000000004606"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 21,
                      "resource": {
                        "name": "Secondary_Email",
                        "id": "111113000000004624"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 22,
                      "resource": {
                        "name": "Twitter",
                        "id": "111113000000004632"
                      },
                      "type": "field"
                    }
                  ],
                  "id": "111113000000106232",
                  "type": "composite"
                },
                {
                  "sequence_number": 3,
                  "display_label": "Dummy",
                  "buttons": [
                    {
                      "color": "#fff",
                      "shape": "capsule",
                      "visibility": "show",
                      "target_screen": {
                        "name": "Screen 2",
                        "id": "111113000000106225"
                      },
                      "type": "transition",
                      "sequence_number": 1,
                      "display_label": "Next",
                      "background_color": "#00A3F3",
                      "name": "WB_Next",
                      "id": "111113000000106258",
                      "category": "wizard_button"
                    }
                  ],
                  "column_count": 2,
                  "id": "111113000000106236",
                  "type": "buttons"
                }
              ]
            },
            {
              "display_label": "Screen 3",
              "api_name": "Screen_3",
              "id": "111113000000106227",
              "segments": [
                {
                  "sequence_number": 1,
                  "display_label": "Description Information",
                  "column_count": 2,
                  "elements": [
                    {
                      "sequence_number": 1,
                      "resource": {
                        "name": "Description",
                        "id": "111113000000004686"
                      },
                      "type": "field"
                    }
                  ],
                  "id": "111113000000106242",
                  "type": "composite"
                },
                {
                  "sequence_number": 2,
                  "display_label": "Dummy",
                  "buttons": [
                    {
                      "color": "#fff",
                      "shape": "capsule",
                      "visibility": "show",
                      "type": "save",
                      "sequence_number": 1,
                      "display_label": "Save",
                      "background_color": "#00A3F3",
                      "name": "WB_Save",
                      "id": "111113000000106399",
                      "category": "wizard_button"
                    }
                  ],
                  "column_count": 2,
                  "id": "111113000000106244",
                  "type": "buttons"
                }
              ]
            },
            {
              "display_label": "Screen 2",
              "api_name": "Screen_2",
              "id": "111113000000106225",
              "segments": [
                {
                  "sequence_number": 1,
                  "display_label": "Address Information",
                  "column_count": 2,
                  "elements": [
                    {
                      "sequence_number": 1,
                      "resource": {
                        "name": "Mailing_Street",
                        "id": "111113000000004666"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 2,
                      "resource": {
                        "name": "Other_Street",
                        "id": "111113000000004668"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 3,
                      "resource": {
                        "name": "Mailing_City",
                        "id": "111113000000004670"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 4,
                      "resource": {
                        "name": "Other_City",
                        "id": "111113000000004672"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 5,
                      "resource": {
                        "name": "Mailing_State",
                        "id": "111113000000004674"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 6,
                      "resource": {
                        "name": "Other_State",
                        "id": "111113000000004676"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 7,
                      "resource": {
                        "name": "Mailing_Zip",
                        "id": "111113000000004678"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 8,
                      "resource": {
                        "name": "Other_Zip",
                        "id": "111113000000004680"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 9,
                      "resource": {
                        "name": "Mailing_Country",
                        "id": "111113000000004682"
                      },
                      "type": "field"
                    },
                    {
                      "sequence_number": 10,
                      "resource": {
                        "name": "Other_Country",
                        "id": "111113000000004684"
                      },
                      "type": "field"
                    }
                  ],
                  "id": "111113000000106238",
                  "type": "composite"
                },
                {
                  "sequence_number": 2,
                  "display_label": "Dummy",
                  "buttons": [
                    {
                      "color": "#fff",
                      "shape": "capsule",
                      "visibility": "show",
                      "target_screen": {
                        "name": "Screen 3",
                        "id": "111113000000106227"
                      },
                      "type": "transition",
                      "sequence_number": 1,
                      "display_label": "Next",
                      "background_color": "#00A3F3",
                      "name": "WB_Next_1",
                      "id": "111113000000106358",
                      "category": "wizard_button"
                    }
                  ],
                  "column_count": 2,
                  "id": "111113000000106240",
                  "type": "buttons"
                }
              ]
            }
          ],
          "id": "111113000000003656"
        }
      ]
    }
  ]
}
```

### Status `400` — `application/json` — MissingParameter

The required module parameter was not found.

```json
{
  "status": "error",
  "code": "REQUIRED_PARAM_MISSING",
  "message": "The parameter 'module' is required.",
  "details": {
    "api_name": "module"
  }
}
```

### Status `400` — `application/json` — ExpectedParameterMissing

One of the expected layout parameters is missing.

```json
{
  "status": "error",
  "code": "EXPECTED_PARAM_MISSING",
  "message": "One of the expected parameter is missing",
  "details": {
    "param_names": [
      "layout_rid",
      "layout_id"
    ]
  }
}
```

### Status `400` — `application/json` — InvalidModule

The module specified is invalid.

```json
{
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "The module name seems to be invalid",
  "details": {}
}
```

### Status `401` — `application/json` — OauthScopeMismatch

OAuth token lacks ZohoCRM.settings.wizards.READ scope.

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `401` — `application/json` — InvalidToken

OAuth token is invalid or expired.

```json
{
  "code": "INVALID_TOKEN",
  "details": {},
  "message": "invalid oauth token",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

User lacks permission to read wizards.

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Zoho CRM: Settings Permission"
    ]
  },
  "message": "Permission denied to read wizards",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Invalid URL pattern or wizard identifier.

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```
