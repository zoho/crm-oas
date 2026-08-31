### `application/json` — SamplePostRequest

Sample request body

```json
{
  "workflow_rules": [
    {
      "name": "WORKFLOWRULE-POST",
      "description": null,
      "module": {
        "api_name": "Contacts",
        "id": "3361265000000000129"
      },
      "execute_when": {
        "type": "create",
        "details": {
          "trigger_module": {
            "api_name": "Contacts",
            "id": "3361265000000000129"
          }
        }
      },
      "conditions": [
        {
          "sequence_number": 1,
          "criteria_details": {
            "criteria": {
              "group_operator": "AND",
              "group": [
                {
                  "comparator": "equal",
                  "field": {
                    "api_name": "Annual_Revenue",
                    "id": "3361265000000000555"
                  },
                  "value": "${NOTEMPTY}"
                },
                {
                  "comparator": "equal",
                  "field": {
                    "api_name": "Phone",
                    "id": "3361265000000000557"
                  },
                  "value": "${NOTEMPTY}"
                }
              ]
            }
          },
          "instant_actions": {
            "actions": [
              {
                "name": "CreateRecord-POST",
                "details": {
                  "layout": {
                    "id": "3361265000000095023",
                    "name": "Standard"
                  },
                  "module": {
                    "id": "3361265000000000131",
                    "api_name": "Deals"
                  },
                  "field_mappings": [
                    {
                      "field": {
                        "id": "3361265000000000515",
                        "api_name": "Owner"
                      },
                      "type": "static",
                      "value": {
                        "id": "3361265000002134004",
                        "name": "user2 testUser"
                      }
                    },
                    {
                      "field": {
                        "id": "3361265000000000519",
                        "api_name": "Deal_Name"
                      },
                      "type": "static",
                      "value": "CreateRecord-POST"
                    },
                    {
                      "field": {
                        "id": "3361265000000000521",
                        "api_name": "Closing_Date"
                      },
                      "type": "execution_time",
                      "value": {
                        "period": "business_days",
                        "unit": "2",
                        "sign": "plus",
                        "trigger_field": "${CURRENTTIME}"
                      }
                    },
                    {
                      "field": {
                        "id": "3361265000000236001",
                        "api_name": "Pipeline"
                      },
                      "type": "static",
                      "value": "Test"
                    },
                    {
                      "field": {
                        "id": "3361265000000000525",
                        "api_name": "Stage"
                      },
                      "type": "static",
                      "value": "Qualification"
                    }
                  ],
                  "apply_restriction": true
                },
                "type": "create_record"
              },
              {
                "name": "AddMeeting-POST",
                "details": {
                  "meeting_duration": {
                    "unit": 2,
                    "period": "minutes"
                  },
                  "host_unavailable": {
                    "assign_record_owner_as_host": true
                  },
                  "layout": {
                    "id": "3361265000000095045",
                    "name": "Standard"
                  },
                  "module": {
                    "id": "3361265000000000145",
                    "api_name": "Events"
                  },
                  "field_mappings": [
                    {
                      "field": {
                        "id": "3361265000000000249",
                        "api_name": "Event_Title"
                      },
                      "type": "static",
                      "value": "AddMeeting-POST"
                    },
                    {
                      "field": {
                        "id": "3361265000000101001",
                        "api_name": "Start_DateTime"
                      },
                      "type": "execution_time",
                      "value": {
                        "period": "minutes",
                        "unit": "2",
                        "sign": "plus",
                        "trigger_field": "${CURRENTTIME}"
                      }
                    },
                    {
                      "field": {
                        "id": "3361265000000057003",
                        "api_name": "All_day"
                      },
                      "type": "static",
                      "value": "true"
                    },
                    {
                      "field": {
                        "id": "3361265000000000247",
                        "api_name": "Owner"
                      },
                      "type": "static",
                      "value": {
                        "id": "3361265000002134004",
                        "name": "user2 testUser"
                      }
                    }
                  ]
                },
                "type": "add_meeting"
              },
              {
                "name": "ScheduleCall-POST",
                "details": {
                  "layout": {
                    "id": "3361265000000095033",
                    "name": "Standard"
                  },
                  "module": {
                    "id": "3361265000000017015",
                    "api_name": "Calls"
                  },
                  "field_mappings": [
                    {
                      "field": {
                        "id": "3361265000000017021",
                        "api_name": "Call_Type"
                      },
                      "type": "static",
                      "value": "Outbound"
                    },
                    {
                      "field": {
                        "id": "3361265000000245003",
                        "api_name": "Outgoing_Call_Status"
                      },
                      "type": "static",
                      "value": "Scheduled"
                    },
                    {
                      "field": {
                        "id": "3361265000000017029",
                        "api_name": "Call_Start_Time"
                      },
                      "type": "execution_time",
                      "value": {
                        "period": "business_days",
                        "unit": "2",
                        "sign": "plus",
                        "trigger_field": "${CURRENTTIME}"
                      }
                    },
                    {
                      "field": {
                        "id": "3361265000000017017",
                        "api_name": "Owner"
                      },
                      "type": "static",
                      "value": {
                        "id": "3361265000002134004",
                        "name": "user2 testUser"
                      }
                    },
                    {
                      "field": {
                        "id": "3361265000000017023",
                        "api_name": "Call_Purpose"
                      },
                      "type": "static",
                      "value": "Demo"
                    },
                    {
                      "field": {
                        "id": "3361265000000536391",
                        "api_name": "Call_Agenda"
                      },
                      "type": "static",
                      "value": "Demo"
                    }
                  ]
                },
                "type": "schedule_call"
              },
              {
                "type": "add_tags",
                "name": "criteria",
                "details": {
                  "over_write": false,
                  "tags": [
                    {
                      "id": "3361265000001715141",
                      "name": "criteria",
                      "color_code": "#879BFC"
                    }
                  ],
                  "module": {
                    "api_name": "Contacts",
                    "id": "3361265000000000129"
                  }
                }
              },
              {
                "type": "remove_tags",
                "name": "criteria",
                "details": {
                  "tags": [
                    {
                      "id": "3361265000001715141",
                      "name": "criteria",
                      "color_code": "#879BFC"
                    }
                  ],
                  "module": {
                    "api_name": "Contacts",
                    "id": "3361265000000000129"
                  }
                }
              },
              {
                "details": {
                  "add_to_existing_contact": false,
                  "add_to_existing_account": true,
                  "move_attachment_to": {
                    "id": "3361265000000000129",
                    "api_name": "Contacts"
                  },
                  "carry_tags": [
                    {
                      "id": "3361265000000000129",
                      "api_name": "Contacts"
                    },
                    {
                      "id": "3361265000000000127",
                      "api_name": "Accounts"
                    },
                    {
                      "id": "3361265000000000131",
                      "api_name": "Deals"
                    }
                  ],
                  "field_mappings": [
                    {
                      "field": {
                        "id": "3361265000000000519",
                        "api_name": "Deal_Name"
                      },
                      "type": "static",
                      "value": "CreatedViaConvert"
                    },
                    {
                      "field": {
                        "id": "3361265000000000521",
                        "api_name": "Closing_Date"
                      },
                      "type": "execution_time",
                      "value": {
                        "period": "days",
                        "unit": "2",
                        "sign": "plus",
                        "trigger_field": "${CURRENTTIME}"
                      }
                    },
                    {
                      "field": {
                        "id": "3361265000000000525",
                        "api_name": "Stage"
                      },
                      "type": "static",
                      "value": "Qualification"
                    },
                    {
                      "field": {
                        "id": "3361265000000236001",
                        "api_name": "Pipeline"
                      },
                      "type": "static",
                      "value": "Standard (Standard)"
                    }
                  ],
                  "create_deal": true,
                  "change_owner": {
                    "apply_assignment_threshold": false,
                    "id": "4554012000000623001"
                  },
                  "contact_role": "3361265000000000052"
                },
                "type": "convert",
                "name": "Create Contact, Account and Deal"
              }
            ]
          },
          "scheduled_actions": [
            {
              "execute_after": {
                "period": "minutes",
                "unit": 2
              },
              "actions": [
                {
                  "id": "3361265000006458562",
                  "type": "email_notifications",
                  "name": "EmailNotification",
                  "related_details": {
                    "best_time": true
                  }
                },
                {
                  "name": "To users : user2 testUser",
                  "type": "assign_owner",
                  "details": {
                    "module": {
                      "api_name": "Vendors",
                      "id": "3361265000000000165"
                    },
                    "assign_to": [
                      {
                        "type": "user",
                        "resource": {
                          "id": "3361265000002134004",
                          "name": "user2 testUser"
                        }
                      },
                      {
                        "type": "role",
                        "resource": {
                          "id": "3361265000000015969",
                          "name": "Manager"
                        },
                        "allow_agent_user": true
                      },
                      {
                        "type": "group",
                        "resource": {
                          "id": "3361265000002284248",
                          "name": "APGroup"
                        }
                      },
                      {
                        "type": "profile",
                        "resource": {
                          "id": "3361265000001212003",
                          "name": "Managers"
                        },
                        "associated_to": "team_profile"
                      }
                    ],
                    "related_records": [
                      {
                        "api_name": "Events"
                      },
                      {
                        "api_name": "Calls"
                      }
                    ],
                    "notify": true,
                    "lookup_field": {
                      "id": "3361265000000000447",
                      "api_name": "Vendor_Name"
                    },
                    "apply_assignment_threshold": true,
                    "user_availability_based_on": [
                      "online_status"
                    ]
                  },
                  "related_details": {
                    "lookup_field": {
                      "id": "3361265000000000447",
                      "api_name": "Vendor_Name"
                    }
                  }
                },
                {
                  "id": "3361265000004189028",
                  "type": "tasks",
                  "name": "test"
                },
                {
                  "id": "3361265000006477034",
                  "type": "webhooks",
                  "name": "Test"
                },
                {
                  "id": "3361265000006131248",
                  "type": "functions",
                  "name": "Function"
                },
                {
                  "type": "field_updates",
                  "name": "FieldUpdate",
                  "id": "3361265000006526009",
                  "related_details": {
                    "lookup_field": {
                      "id": "3361265000000000447",
                      "api_name": "Vendor_Name"
                    }
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```
