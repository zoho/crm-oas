Successful Cadence retrieval response

```json
{
  "cadences": [
    {
      "summary": {
        "whatsapp_follow_up_count": 0,
        "task_follow_up_count": 1,
        "call_follow_up_count": 1,
        "email_follow_up_count": 0
      },
      "created_time": "2025-11-07T14:52:24+00:00",
      "module": {
        "api_name": "Leads",
        "id": "111112000000002628"
      },
      "description": "description",
      "execution_details": {
        "unenroll_properties": [
          {
            "details": null,
            "id": "111112000000092054",
            "type": "automatic_unenroll"
          },
          {
            "details": {
              "unenroll_date": "2025-11-30"
            },
            "id": "111112000000092056",
            "type": "end_date"
          },
          {
            "details": {
              "criteria": {
                "comparator": "equal",
                "field": {
                  "api_name": "Annual_Revenue",
                  "id": "111112000000004814"
                },
                "type": "value",
                "value": "123"
              }
            },
            "id": "111112000000092058",
            "type": "criteria"
          },
          {
            "details": {
              "details": {
                "criteria": {
                  "comparator": "equal",
                  "field": {
                    "api_name": "Subject",
                    "id": "111112000000004066"
                  },
                  "type": "value",
                  "value": "teste"
                },
                "state": null,
                "specific": false
              },
              "type": "Tasks"
            },
            "id": "111112000000092060",
            "type": "followup_criteria"
          },
          {
            "details": {
              "details": {
                "criteria": {
                  "comparator": "equal",
                  "field": {
                    "api_name": "Created_By",
                    "id": "111112000000004224"
                  },
                  "type": "value",
                  "value": {
                    "name": "Poongodi89 S",
                    "id": "111112000000057662"
                  }
                },
                "state": {
                  "name": "FollowUp2",
                  "id": "111112000000092010"
                },
                "specific": true
              },
              "type": "Calls"
            },
            "id": "111112000000092106",
            "type": "followup_criteria"
          }
        ],
        "execute_every": {
          "unit": 1,
          "period": "hours"
        }
      },
      "type": "custom_view",
      "created_by": {
        "name": "Poongodi89 S",
        "id": "111112000000057662"
      },
      "modified_time": "2025-11-07T15:32:03+00:00",
      "modified_by": {
        "name": "Poongodi89 S",
        "id": "111112000000057662"
      },
      "name": "cadence",
      "follow_ups": [
        {
          "parent_follow_up": null,
          "action": {
            "created_time": "2025-11-07T15:10:47+05:30",
            "lock_status": {
              "locked": false
            },
            "related_details": null,
            "editable": true,
            "module": {
              "api_name": "Leads",
              "id": "111112000000002628"
            },
            "related_module": null,
            "deletable": true,
            "source": "crm",
            "type": "tasks",
            "created_by": {
              "name": "Poongodi89 S",
              "id": "111112000000057662"
            },
            "notify": false,
            "feature_type": "cadences",
            "field_mappings": [
              {
                "display_value": "task1",
                "field": {
                  "api_name": "Subject",
                  "id": "111112000000004066"
                },
                "type": "static",
                "value": "task1"
              },
              {
                "display_value": "Trigger Date plus 1 business day(s)",
                "field": {
                  "api_name": "Due_Date",
                  "id": "111112000000004068"
                },
                "type": "execution_time",
                "value": {
                  "period": "business_days",
                  "unit": "1",
                  "trigger_field": "${CURRENTTIME}",
                  "sign": "plus"
                }
              },
              {
                "display_value": "Poongodi89 S",
                "field": {
                  "api_name": "Owner",
                  "id": "111112000000004064"
                },
                "type": "static",
                "value": {
                  "name": "Poongodi89 S",
                  "id": "111112000000057662"
                }
              },
              {
                "display_value": "Not Started",
                "field": {
                  "api_name": "Status",
                  "id": "111112000000004074"
                },
                "type": "static",
                "value": "Not Started"
              },
              {
                "display_value": "High",
                "field": {
                  "api_name": "Priority",
                  "id": "111112000000004076"
                },
                "type": "static",
                "value": "High"
              }
            ],
            "modified_time": "2025-11-07T15:10:47+05:30",
            "associated": true,
            "modified_by": {
              "name": "Poongodi89 S",
              "id": "111112000000057662"
            },
            "name": "task1",
            "id": "111112000000091250"
          },
          "id": "111112000000092009"
        },
        {
          "execute_after": {
            "unit": 10,
            "period": "minutes",
            "id": "111112000000092016"
          },
          "parent_follow_up": {
            "id": "111112000000092009",
            "type": "tasks"
          },
          "action": {
            "name": "Calls",
            "details": {
              "layout": {
                "name": "Standard",
                "id": "111112000000003660"
              },
              "field_mappings": [
                {
                  "display_value": "Outbound",
                  "field": {
                    "api_name": "Call_Type",
                    "id": "111112000000004208"
                  },
                  "type": "static",
                  "value": "Outbound"
                },
                {
                  "display_value": "Scheduled",
                  "field": {
                    "api_name": "Outgoing_Call_Status",
                    "id": "111112000000004236"
                  },
                  "type": "static",
                  "value": "Scheduled"
                },
                {
                  "display_value": "Trigger Date plus 1 business day(s) 12:00 AM",
                  "field": {
                    "api_name": "Call_Start_Time",
                    "id": "111112000000004216"
                  },
                  "type": "execution_time",
                  "value": {
                    "unit": "1",
                    "period": "business_days",
                    "trigger_field": "${CURRENTTIME}",
                    "sign": "plus",
                    "time": "00:00"
                  }
                },
                {
                  "display_value": "${CURRENTUSER}",
                  "field": {
                    "api_name": "Owner",
                    "id": "111112000000004204"
                  },
                  "type": "static",
                  "value": {
                    "name": "${CURRENTUSER}"
                  }
                },
                {
                  "display_value": "Demo",
                  "field": {
                    "api_name": "Call_Purpose",
                    "id": "111112000000004262"
                  },
                  "type": "static",
                  "value": "Demo"
                },
                {
                  "display_value": "test",
                  "field": {
                    "api_name": "Call_Agenda",
                    "id": "111112000000004264"
                  },
                  "type": "static",
                  "value": "test"
                },
                {
                  "display_value": "test subject",
                  "field": {
                    "api_name": "Subject",
                    "id": "111112000000004206"
                  },
                  "type": "static",
                  "value": "test subject"
                },
                {
                  "display_value": {
                    "unit": "15",
                    "period": "minutes"
                  },
                  "field": {
                    "api_name": "Reminder",
                    "id": "111112000000004232"
                  },
                  "type": "static",
                  "value": {
                    "unit": "15",
                    "period": "minutes"
                  }
                }
              ],
              "module": {
                "api_name": "Calls",
                "id": "111112000000002654"
              }
            },
            "id": "111112000000092020",
            "type": "schedule_call"
          },
          "id": "111112000000092010",
          "triggers": [
            "Completed"
          ]
        }
      ],
      "id": "111112000000092007",
      "draft_cadence": {
        "id": "111112000000092213",
        "name": "Draft Cadence"
      },
      "parent_cadence": {
        "id": "111112000000069836",
        "name": "Parent Cadence"
      },
      "custom_view": {
        "name": "All Leads",
        "id": "111112000000051112"
      },
      "status": "inactive"
    }
  ]
}
```
