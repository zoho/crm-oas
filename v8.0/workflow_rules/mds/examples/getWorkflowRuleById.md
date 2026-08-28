# Examples: getWorkflowRuleById

**GET /settings/automation/workflow_rules/{id}**

## Response examples

### Status `200` — `application/json` — GetSuccessResponse

Successful retrieval of a specific workflow rule's full configuration


```json
{
  "workflow_rules": [
    {
      "created_time": "2025-12-01T11:09:10+05:30",
      "execute_when": {
        "details": {
          "trigger_module": {
            "api_name": "Leads",
            "id": "4011656000000000125"
          }
        },
        "type": "create"
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "4011656000000000125"
      },
      "deprecated": false,
      "deletable": true,
      "description": "ds",
      "source": "crm",
      "created_by": {
        "name": "Rishi LocalTest",
        "id": "4011656000000603001"
      },
      "last_executed_time": null,
      "modified_time": "2025-12-01T11:15:03+05:30",
      "name": "fwsefw",
      "modified_by": {
        "name": "Rishi LocalTest",
        "id": "4011656000000603001"
      },
      "lock": {
        "locked_by": null,
        "message": null,
        "status": false
      },
      "id": "4011656000002144049",
      "category": "default",
      "conditions": [
        {
          "sequence_number": 1,
          "instant_actions": {
            "actions": [
              {
                "related_details": null,
                "name": "To users : user2 testUser",
                "details": {
                  "apply_assignment_threshold": true,
                  "assign_to": [
                    {
                      "resource": {
                        "name": "user2 testUser",
                        "id": "3361265000002134004",
                        "type": "user"
                      },
                      "details": null,
                      "type": "user"
                    }
                  ],
                  "module": {
                    "api_name": "Leads",
                    "id": "3361265000000000125"
                  },
                  "related_records": [
                    {
                      "api_name": "Tasks",
                      "id": "3361265000000000143"
                    },
                    {
                      "api_name": "Events",
                      "id": "3361265000000000145"
                    }
                  ],
                  "user_availability_based_on": [
                    "online_status"
                  ],
                  "notify": true
                },
                "id": "3361265000006526168",
                "type": "assign_owner"
              },
              {
                "related_details": {
                  "lookup_field": {
                    "api_name": "Lookup",
                    "id": "3361265000002147008"
                  }
                },
                "name": "title",
                "details": {
                  "module": {
                    "api_name": "Contacts",
                    "id": "3361265000000000129"
                  }
                },
                "id": "3361265000006486997",
                "type": "field_updates"
              },
              {
                "name": "criteria",
                "details": {
                  "module": {
                    "api_name": "Leads",
                    "id": "3361265000000000125"
                  },
                  "over_write": false,
                  "tags": [
                    {
                      "name": "criteria",
                      "id": "3361265000001715037",
                      "color_code": "#FD87BD"
                    }
                  ]
                },
                "id": "3361265000006526169",
                "type": "add_tags"
              },
              {
                "name": "test_webhook",
                "id": "3361265000003613045",
                "type": "webhooks"
              },
              {
                "name": "Leads",
                "details": {
                  "layout": {
                    "display_label": "cloneLayout",
                    "name": "cloneLayout",
                    "id": "3361265000006165015"
                  },
                  "field_mappings": [
                    {
                      "display_value": "testUser user2",
                      "field": {
                        "api_name": "Owner",
                        "id": "3361265000000000553"
                      },
                      "type": "static",
                      "value": {
                        "name": "testUser user2",
                        "id": "3361265000002134004"
                      }
                    },
                    {
                      "display_value": "CreateRecord",
                      "field": {
                        "api_name": "Company",
                        "id": "3361265000000000555"
                      },
                      "type": "static",
                      "value": "CreateRecord"
                    },
                    {
                      "display_value": "CreateRecord",
                      "field": {
                        "api_name": "Last_Name",
                        "id": "3361265000000000559"
                      },
                      "type": "static",
                      "value": "CreateRecord"
                    }
                  ],
                  "module": {
                    "api_name": "Leads",
                    "id": "3361265000000000125"
                  },
                  "apply_restriction": false
                },
                "id": "3361265000006526170",
                "type": "create_record"
              }
            ]
          },
          "scheduled_actions": [
            {
              "execute_after": {
                "period": "business_hours",
                "unit": 1
              },
              "id": "3361265000006526188",
              "actions": [
                {
                  "name": "criteria",
                  "details": {
                    "module": {
                      "api_name": "Leads",
                      "id": "3361265000000000125"
                    },
                    "over_write": false,
                    "tags": [
                      {
                        "name": "criteria",
                        "id": "3361265000001715037",
                        "color_code": "#FD87BD"
                      }
                    ]
                  },
                  "id": "3361265000006526192",
                  "type": "remove_tags"
                },
                {
                  "related_details": null,
                  "name": "LeadTask",
                  "id": "3361265000002157092",
                  "type": "tasks"
                },
                {
                  "name": "RB",
                  "id": "3361265000005845301",
                  "type": "functions"
                },
                {
                  "related_details": null,
                  "name": "testEmail",
                  "id": "3361265000004539004",
                  "type": "email_notifications"
                },
                {
                  "name": "AddMeeting",
                  "details": {
                    "layout": {
                      "name": "Standard",
                      "id": "3361265000000095045"
                    },
                    "field_mappings": [
                      {
                        "display_value": "AddMeeting",
                        "field": {
                          "api_name": "Event_Title",
                          "id": "3361265000000000249"
                        },
                        "type": "static",
                        "value": "AddMeeting"
                      },
                      {
                        "display_value": "Trigger Date plus 2 business day(s) 12:00 AM",
                        "field": {
                          "api_name": "Start_DateTime",
                          "id": "3361265000000101001"
                        },
                        "type": "execution_time",
                        "value": {
                          "unit": "2",
                          "period": "business_days",
                          "trigger_field": "${CURRENTTIME}",
                          "sign": "plus",
                          "time": "00:00"
                        }
                      },
                      {
                        "display_value": "false",
                        "field": {
                          "api_name": "All_day",
                          "id": "3361265000000057003"
                        },
                        "type": "static",
                        "value": "false"
                      },
                      {
                        "display_value": "testUser user2",
                        "field": {
                          "api_name": "Owner",
                          "id": "3361265000000000247"
                        },
                        "type": "static",
                        "value": {
                          "name": "testUser user2",
                          "id": "3361265000002134004"
                        }
                      }
                    ],
                    "module": {
                      "api_name": "Events",
                      "id": "3361265000000000145"
                    },
                    "meeting_duration": {
                      "unit": 2,
                      "period": "minutes"
                    },
                    "host_unavailable": {
                      "assign_record_owner_as_host": true
                    }
                  },
                  "id": "3361265000006526193",
                  "type": "add_meeting"
                },
                {
                  "name": "Calls",
                  "details": {
                    "layout": {
                      "name": "Standard",
                      "id": "3361265000000095033"
                    },
                    "field_mappings": [
                      {
                        "display_value": "Outbound",
                        "field": {
                          "api_name": "Call_Type",
                          "id": "3361265000000017021"
                        },
                        "type": "static",
                        "value": "Outbound"
                      },
                      {
                        "display_value": "Scheduled",
                        "field": {
                          "api_name": "Outgoing_Call_Status",
                          "id": "3361265000000245003"
                        },
                        "type": "static",
                        "value": "Scheduled"
                      },
                      {
                        "display_value": "Trigger Date plus 2 business day(s) 12:00 AM",
                        "field": {
                          "api_name": "Call_Start_Time",
                          "id": "3361265000000017029"
                        },
                        "type": "execution_time",
                        "value": {
                          "unit": "2",
                          "period": "business_days",
                          "trigger_field": "${CURRENTTIME}",
                          "sign": "plus",
                          "time": "00:00"
                        }
                      },
                      {
                        "display_value": "testUser user2",
                        "field": {
                          "api_name": "Owner",
                          "id": "3361265000000017017"
                        },
                        "type": "static",
                        "value": {
                          "name": "testUser user2",
                          "id": "3361265000002134004"
                        }
                      },
                      {
                        "display_value": "Demo",
                        "field": {
                          "api_name": "Call_Purpose",
                          "id": "3361265000000017023"
                        },
                        "type": "static",
                        "value": "Demo"
                      },
                      {
                        "display_value": "Demo",
                        "field": {
                          "api_name": "Call_Agenda",
                          "id": "3361265000000536391"
                        },
                        "type": "static",
                        "value": "Demo"
                      }
                    ],
                    "module": {
                      "api_name": "Calls",
                      "id": "3361265000000017015"
                    }
                  },
                  "id": "3361265000006526194",
                  "type": "schedule_call"
                }
              ]
            }
          ],
          "criteria_details": {
            "relational_criteria": {
              "module_selection": null,
              "criteria": null,
              "module": null
            },
            "criteria": {
              "comparator": "not_equal",
              "field": {
                "api_name": "Company",
                "id": "3361265000000000555"
              },
              "type": "value",
              "value": "${EMPTY}"
            }
          },
          "id": "3361265000006526161"
        }
      ],
      "status": {
        "active": true
      }
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse

NO_PERMISSION error for workflow rule retrieval


```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```
