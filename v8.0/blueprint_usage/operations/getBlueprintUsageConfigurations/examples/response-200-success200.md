Successful retrieval of a module's blueprint usage configuration

```json
{
  "blueprints": [
    {
      "process": {
        "name": {
          "unsupported_characters": [
            "%",
            "&"
          ],
          "max_length": 50
        },
        "description": {
          "unsupported_characters": [
            "%",
            "&"
          ],
          "max_length": 500
        },
        "type": [
          {
            "blueprint_type": "normal",
            "unsupported_components": null
          },
          {
            "blueprint_type": "continuous",
            "unsupported_components": [
              {
                "name": "input_components",
                "input_components": [
                  "kiosk",
                  "widget"
                ]
              },
              {
                "name": "transitions",
                "types": [
                  "parallel_transition"
                ]
              }
            ]
          }
        ]
      },
      "states": {
        "supported_components": [
          {
            "name": "actions",
            "supported_subcomponents": [
              "Escalation Alerts"
            ],
            "mandate_subcomponent": true
          },
          {
            "name": "timebox",
            "supported_subcomponents": null,
            "mandate_subcomponent": true
          }
        ],
        "limit": 50
      },
      "transitions": {
        "name": {
          "unsupported_characters": [
            "%",
            "&"
          ],
          "max_length": 50
        },
        "description": {
          "unsupported_characters": [
            "%",
            "&"
          ],
          "max_length": 500
        },
        "trigger_type": [
          {
            "name": "automatic",
            "supported_transition_types": [
              {
                "name": "standalone_transition",
                "common_source": true,
                "limit": 50,
                "supported_components": [
                  {
                    "name": "timebox",
                    "mandate_subcomponent": false,
                    "supported_subcomponents": null
                  },
                  {
                    "name": "transition_groups",
                    "mandate_subcomponent": true,
                    "supported_subcomponents": [
                      "after"
                    ]
                  }
                ]
              }
            ]
          },
          {
            "name": "manual",
            "supported_transition_types": [
              {
                "name": "standalone_transition",
                "common_source": true,
                "limit": 50,
                "supported_components": [
                  {
                    "name": "transition_groups",
                    "mandate_subcomponent": true,
                    "supported_subcomponents": [
                      "before",
                      "during",
                      "after"
                    ]
                  }
                ]
              },
              {
                "name": "parallel_transition",
                "common_source": false,
                "limit": 5,
                "supported_components": [
                  {
                    "name": "transition_groups",
                    "mandate_subcomponent": true,
                    "supported_subcomponents": [
                      "before",
                      "after"
                    ]
                  }
                ]
              },
              {
                "name": "child_transition",
                "common_source": false,
                "limit": 5,
                "supported_components": [
                  {
                    "name": "transition_groups",
                    "mandate_subcomponent": true,
                    "supported_subcomponents": [
                      "before",
                      "during"
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      "actions": [
        {
          "api_name": "tags",
          "name": "Tags",
          "display_name": "Tags",
          "associate_action": false,
          "clickable": true,
          "limit_per_action": 10,
          "new": true,
          "limit": 1,
          "sub_actions": [
            {
              "api_name": "add_tags",
              "name": "AddTags",
              "display_name": "Add Tag(s)"
            },
            {
              "api_name": "remove_tags",
              "name": "RemoveTags",
              "display_name": "Remove Tag(s)"
            }
          ]
        },
        {
          "name": "Alert",
          "api_name": "email_notifications",
          "display_name": "Email Notification",
          "associate_action": true,
          "clickable": true,
          "limit_per_action": null,
          "new": true,
          "limit": 5
        },
        {
          "name": "Task",
          "api_name": "tasks",
          "display_name": "Tasks",
          "associate_action": true,
          "clickable": true,
          "limit_per_action": null,
          "new": true,
          "limit": 5
        },
        {
          "name": "CreateRecord",
          "api_name": "create_record",
          "display_name": "Create Record",
          "associate_action": true,
          "clickable": true,
          "limit_per_action": null,
          "new": true,
          "limit": 5
        },
        {
          "name": "AddMeeting",
          "api_name": "add_meeting",
          "display_name": "Add Meeting",
          "associate_action": true,
          "clickable": true,
          "limit_per_action": null,
          "new": false,
          "limit": 5
        },
        {
          "name": "ScheduleCall",
          "api_name": "schedule_call",
          "display_name": "Schedule Call",
          "associate_action": true,
          "clickable": true,
          "limit_per_action": null,
          "new": false,
          "limit": 5
        },
        {
          "name": "Convert",
          "api_name": "convert",
          "display_name": "Convert",
          "associate_action": true,
          "clickable": true,
          "limit_per_action": null,
          "unsupported_actions": [
            "tasks",
            "fieldupdates",
            "tags"
          ],
          "new": false,
          "limit": 5
        },
        {
          "name": "Webhook",
          "api_name": "webhooks",
          "display_name": "Webhooks",
          "associate_action": true,
          "clickable": true,
          "limit_per_action": null,
          "new": false,
          "limit": 5
        },
        {
          "name": "Deluge",
          "api_name": "functions",
          "display_name": "Function",
          "associate_action": true,
          "clickable": true,
          "limit_per_action": null,
          "new": false,
          "limit": 5
        },
        {
          "name": "Circuits",
          "api_name": "circuits",
          "display_name": "Circuit",
          "associate_action": false,
          "clickable": false,
          "limit_per_action": null,
          "new": false,
          "limit": 5
        },
        {
          "name": "Whatsappnotification",
          "api_name": "whatsapp_notification",
          "display_name": "WhatsApp Notification",
          "associate_action": false,
          "clickable": false,
          "limit_per_action": null,
          "new": false,
          "limit": 3
        },
        {
          "name": "SMS",
          "api_name": "sms",
          "display_name": "SMS",
          "associate_action": false,
          "clickable": false,
          "limit_per_action": null,
          "new": false,
          "limit": 3
        },
        {
          "name": "SLA Alert",
          "api_name": "sla_alert",
          "display_name": " Default SLA Alert",
          "associate_action": false,
          "clickable": true,
          "limit_per_action": null,
          "new": false,
          "limit": 1
        },
        {
          "name": "Escalation Alerts",
          "api_name": "trigger_details",
          "display_name": "Escalation Alerts",
          "associate_action": false,
          "clickable": true,
          "limit_per_action": null,
          "new": false,
          "limit": 3,
          "execute_type": [
            {
              "name": "before",
              "period": [
                {
                  "name": "hours",
                  "display_name": "Hour(s)"
                },
                {
                  "name": "minute",
                  "display_name": "Minute(s)"
                },
                {
                  "name": "days",
                  "display_name": "Day(s)"
                }
              ],
              "timebox_required": true
            },
            {
              "name": "on",
              "period": null,
              "timebox_required": false
            },
            {
              "name": "after",
              "period": [
                {
                  "name": "hours",
                  "display_name": "Hour(s)"
                },
                {
                  "name": "minute",
                  "display_name": "Minute(s)"
                },
                {
                  "name": "days",
                  "display_name": "Day(s)"
                },
                {
                  "name": "b_hours",
                  "display_name": "Bsuiness Hour(s)"
                },
                {
                  "name": "b_days",
                  "display_name": "Bsuiness Day(s)"
                }
              ],
              "timebox_required": true
            }
          ],
          "sub_actions": [
            {
              "api_name": "field_updates",
              "name": "Fieldupdate",
              "display_name": "Field Update"
            },
            {
              "api_name": "sla",
              "name": "SLA",
              "display_name": "SLA"
            },
            {
              "api_name": "email_notifications",
              "name": "Alert",
              "display_name": "Alert"
            },
            {
              "api_name": "tasks",
              "name": "Task",
              "display_name": "Task"
            },
            {
              "api_name": "webhooks",
              "name": "Webhook",
              "display_name": "Webhook"
            },
            {
              "api_name": "functions",
              "name": "Deluge",
              "display_name": "Deluge"
            }
          ],
          "mandate_subactions": true
        }
      ],
      "input_components": {
        "types": [
          {
            "name": "Fields",
            "api_name": "fields",
            "validation_supported": true,
            "standalone_component": false,
            "unsupported_values": [
              "layout"
            ],
            "limit_per_component": null
          },
          {
            "name": "Field of Lookup",
            "api_name": "field_of_lookup",
            "validation_supported": true,
            "standalone_component": false,
            "unsupported_values": [
              "lookup"
            ],
            "limit_per_component": null
          },
          {
            "name": "Associated Items",
            "api_name": "associated_items",
            "validation_supported": false,
            "standalone_component": false,
            "unsupported_values": null,
            "limit_per_component": null,
            "sub_components": [
              {
                "name": "Notes",
                "api_name": "notes",
                "validation_supported": false,
                "standalone_component": false,
                "unsupported_values": null,
                "limit_per_component": 1
              },
              {
                "name": "Attachments",
                "api_name": "attachments",
                "validation_supported": false,
                "standalone_component": false,
                "unsupported_values": null,
                "limit_per_component": 1
              },
              {
                "name": "Related Lists",
                "api_name": "related_list",
                "validation_supported": true,
                "standalone_component": false,
                "unsupported_values": null,
                "limit_per_component": 5
              }
            ]
          },
          {
            "name": "Message",
            "api_name": "info_message",
            "validation_supported": false,
            "standalone_component": false,
            "unsupported_values": null,
            "limit_per_component": null
          },
          {
            "name": "Tags",
            "api_name": "tags",
            "validation_supported": false,
            "standalone_component": false,
            "unsupported_values": null,
            "limit_per_component": 1
          },
          {
            "name": "Checklists",
            "api_name": "checklist",
            "validation_supported": false,
            "standalone_component": false,
            "unsupported_values": null,
            "limit_per_component": 1
          },
          {
            "name": "Widgets",
            "api_name": "widgets",
            "validation_supported": false,
            "standalone_component": true,
            "unsupported_values": null,
            "limit_per_component": 1
          },
          {
            "name": "Kiosk",
            "api_name": "kiosk",
            "validation_supported": false,
            "standalone_component": true,
            "unsupported_values": null,
            "limit_per_component": 1
          }
        ],
        "limit": 50
      },
      "owners": {
        "display_name": "Owners",
        "types": [
          "user",
          "role",
          "user_group",
          "portal",
          "team_user",
          "team_profile"
        ],
        "limit": 100
      },
      "transition_groups": [
        {
          "name": "before",
          "display_name": "BEFORE",
          "supported_components": [
            {
              "name": "owners",
              "mandate_subcomponent": false,
              "supported_subcomponents": null
            },
            {
              "name": "criteria",
              "mandate_subcomponent": false,
              "supported_subcomponents": null
            }
          ]
        },
        {
          "name": "during",
          "display_name": "DURING",
          "supported_components": [
            {
              "name": "input_components",
              "mandate_subcomponent": false,
              "supported_subcomponents": null
            }
          ]
        },
        {
          "name": "after",
          "display_name": "AFTER",
          "supported_components": [
            {
              "name": "actions",
              "mandate_subcomponent": false,
              "supported_subcomponents": [
                "Tags",
                "Alert",
                "Task",
                "Field update",
                "CreateRecord",
                "AddMeeting",
                "ScheduleCall",
                "Convert",
                "Webhook",
                "Deluge",
                "Functions",
                "Whatsapp notification",
                "SMS",
                "Circuits"
              ]
            }
          ]
        }
      ],
      "timebox": {
        "period": [
          {
            "name": "hours",
            "display_name": "Hour(s)"
          },
          {
            "name": "minute",
            "display_name": "Minute(s)"
          },
          {
            "name": "days",
            "display_name": "Day(s)"
          },
          {
            "name": "business_hour(s)",
            "display_name": "Business Hour(s)"
          },
          {
            "name": "business_day(s)",
            "display_name": "Business Day(s)"
          }
        ],
        "minimum_values": {
          "unit": 15,
          "period": "minutes"
        }
      }
    }
  ]
}
```
