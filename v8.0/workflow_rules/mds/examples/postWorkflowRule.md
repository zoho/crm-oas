# Examples: postWorkflowRule

**POST /settings/automation/workflow_rules**

## Request examples

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

## Response examples

### Status `201` — `application/json` — SuccessResponse

POST- Success response for status 201

```json
{
  "workflow_rules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "3361265000006294001"
      },
      "message": "workflow created",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response with code INVALID_DATA: invalid data (Field: workflow_rules)

```json
{
  "code": "INVALID_DATA",
  "details": {
    "api_name": "workflow_rules",
    "json_path": "$.workflow_rules"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.workflow_rules[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Error response with code INVALID_DATA: Invalid data (Field: type)

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "message": "invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "create",
          "edit",
          "create_or_edit",
          "delete",
          "field_update",
          "rollup_summary_update",
          "section_update",
          "date_or_datetime",
          "score_increase",
          "score_update",
          "score_decrease",
          "recommendation",
          "field_update",
          "score_increase",
          "score_decrease",
          "score_update",
          "scheduled_call_field_update",
          "scheduled_call_section_update",
          "scheduled_call_edit",
          "scheduled_call_createedit",
          "outgoing_call_ring",
          "outgoing_call_start",
          "outgoing_call_section_update",
          "outgoing_call_createedit",
          "outgoing_call_field_update",
          "outgoing_call_edit",
          "incoming_call_ring",
          "incoming_call_start",
          "incoming_call_edit",
          "incoming_call_field_update",
          "incoming_call_createedit",
          "incoming_call_section_update",
          "anyaction",
          "delete",
          "missed_call",
          "create",
          "reschedule",
          "cancel",
          "reassign",
          "delete",
          "overdue",
          "marked_as_complete",
          "anyaction",
          "email_received",
          "mail_sent",
          "mail_sent_clicked",
          "mail_sent_replied",
          "mail_sent_opened",
          "mail_sent_bounced",
          "email_received_notreplied",
          "email_received_opened_notreplied",
          "mail_sent_replied_within",
          "mail_sent_opened_notreplied",
          "mail_sent_notreplied",
          "mail_sent_notopened",
          "fb_post_on_page",
          "fb_comment_on_page",
          "fb_like_on_post",
          "fb_send_message",
          "tw_mention_on",
          "tw_retweet_on_tweet",
          "tw_comment_on_tweet",
          "tw_send_message"
        ],
        "json_path": "$.workflow_rules[*].execute_when.type"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MeetingCallInvalidDataResponse

Error response with code INVALID_DATA: Invalid Owner Id)

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.field_mappings[3].id"
      },
      "message": "Invalid User ID",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissingResponse1

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: details)

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].type"
        },
        "api_name": "details",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TriggerDependentFieldMissingResponse1

Error response with code DEPENDENT_FIELD_MISSING: Dependent Field missing (Field: repeat)

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.workflow_rules[0].execute_when.type"
        },
        "api_name": "repeat",
        "json_path": "$.workflow_rules[0].execute_when.details.repeat"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ScheduledActionsDependentFieldMissingResponse

Error response with code DEPENDENT_FIELD_MISSING: unit/period is missing

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "execute_after",
          "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].execute_after"
        },
        "api_name": "unit",
        "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].execute_after.unit"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — AssociateActionDependentFieldMissingResponse

Error response with code DEPENDENT_FIELD_MISSING: Missing Associated Action Id

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].type"
        },
        "api_name": "id",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].id"
      },
      "message": "Dependent Field missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExpectedFieldMissingResponse1

Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "workflow_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.module.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.module.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ScheduledActionsExpectedFieldMissingResponse

Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "workflow_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "period",
            "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].execute_after.period"
          },
          {
            "api_name": "unit",
            "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].execute_after.unit"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MeetingExpectedFieldMissingResponse

Error response with code EXPECTED_FIELD_MISSING: Specify atleast one field

```json
{
  "workflow_rules": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "assign_record_owner_as_host",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.host_unavailable.assign_record_owner_as_host"
          },
          {
            "api_name": "assign_task",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.host_unavailable.assign_task"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Error response with code MANDATORY_NOT_FOUND: Required field is missing (Field: name)

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "name",
        "json_path": "$.workflow_rules[*].name"
      },
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MeetingAmbiguityErrorResponse

Error response with code AMBIGUITY_DURING_PROCESSING: Ambiguity during processing (Field: meeting_duration)

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "meeting_duration",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.meeting_duration"
          },
          {
            "api_name": "field_mappings",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.field_mappings"
          }
        ]
      },
      "message": "As All Day is passed true, meeting_duration cannot be configured",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActionVsTriggerADPResponse1

Error response with code AMBIGUITY_DURING_PROCESSING: action not supported for this trigger

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "type",
            "json_path": "$.workflow_rules[0].execute_when.type"
          },
          {
            "api_name": "type",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].type"
          }
        ]
      },
      "message": "action not supported for this trigger",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActionLimitExceededResponse

Error response with code LIMIT_EXCEEDED: per-type action limit exceeded in instant/scheduled actions

```json
{
  "workflow_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "actions",
        "limit": 5,
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions"
      },
      "message": "actions limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NotAllowedErrorResponse

Error response with code NOT_ALLOWED: The unsupported action is given

```json
{
  "workflow_rules": [
    {
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "type",
        "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions[0].actions[0].type"
      },
      "message": "The unsupported action is given",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatchResponse

Error response with code DEPENDENT_MISMATCH: Dependent Field is not matching (Field: module)

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "module_selection",
          "json_path": "$.workflow_rules[0].conditions[0].criteria_details.relational_criteria.module_selection"
        },
        "api_name": "module",
        "json_path": "$.workflow_rules[0].conditions[0].criteria_details.relational_criteria.module"
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleMandatoryNotFoundResponse

Error response with code MANDATORY_NOT_FOUND: module is required

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "module",
        "json_path": "$.workflow_rules[*].module"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ModuleInvalidDataResponse

Error response with code INVALID_DATA: invalid module api_name or id

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "module",
        "json_path": "$.workflow_rules[*].module"
      },
      "message": "the module name given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NameSpecialCharsResponse

Error response with code INVALID_DATA: workflow name contains special characters

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.workflow_rules[*].name"
      },
      "message": "Special characters found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — NameLengthExceededResponse

Error response with code INVALID_DATA: workflow name exceeds max length

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.workflow_rules[*].name",
        "maximum_length": 100
      },
      "message": "value too long",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CannotCreateInactiveResponse

Error response with code INVALID_DATA: cannot create an inactive workflow rule

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "active",
        "json_path": "$.workflow_rules[*].status.active"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ExecuteWhenMissingResponse

Error response with code MANDATORY_NOT_FOUND: execute_when is required

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "execute_when",
        "json_path": "$.workflow_rules[*].execute_when"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ConditionsLimitExceededResponse

Error response with code LIMIT_EXCEEDED: conditions count exceeds edition limit

```json
{
  "workflow_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "conditions",
        "limit": 3,
        "json_path": "$.workflow_rules[*].conditions"
      },
      "message": "conditions limit exceeded",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — RelCriteriaModuleSelectionMissingResponse

Error response with code MANDATORY_NOT_FOUND: module_selection missing for relational_criteria

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "module_selection",
        "json_path": "$.workflow_rules[0].conditions[0].criteria_details.relational_criteria.module_selection"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActionTypeMissingResponse

Error response with code INVALID_DATA: action type is required

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].type"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ActionNotSupportedForModuleResponse

Error response with code AMBIGUITY_DURING_PROCESSING: action type not supported for module, or action's bound module does not match relational_criteria.module

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "module",
            "json_path": "$.workflow_rules[*].module"
          },
          {
            "api_name": "type",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].type"
          }
        ]
      },
      "message": "action not supported for this module",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ScheduledActionsRepeatConflictResponse

Error response with code DEPENDENT_MISMATCH: scheduled_actions not supported with repeat=true

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "repeat",
          "json_path": "$.workflow_rules[0].execute_when.details.repeat"
        },
        "api_name": "scheduled_actions",
        "json_path": "$.workflow_rules[0].conditions[0].scheduled_actions"
      },
      "message": "Dependent Field is not matching",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FeatureDisabledResponse

Error response with code FEATURE_DISABLED: a dependent feature is disabled

```json
{
  "workflow_rules": [
    {
      "code": "FEATURE_DISABLED",
      "details": {},
      "message": "Please enable the feature",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — FailureResponse

Error response with code FAILURE: unexpected server-side error

```json
{
  "workflow_rules": [
    {
      "code": "FAILURE",
      "details": {},
      "message": "Unable to process your request. Please verify whether you have provided valid data.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ChatNotificationMessageMissingResponse

Error response: MANDATORY_NOT_FOUND  - chat notification message missing

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "message",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.message"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ChatNotificationNotifyToMissingResponse

Error response: DEPENDENT_FIELD_MISSING  - notify_to id/name missing for user/channel type

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "id",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.notify_to.id"
      },
      "message": "Required dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ChatNotificationInvalidTypeResponse

Error response: INVALID_DATA  - invalid notify_to type for chat notification

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.notify_to.type"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ChatNotificationFieldAmbiguityResponse

Error response: AMBIGUITY_DUE_TO  - notify_to field id and api_name mismatch

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.notify_to.notify_fields.fields[0].id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.notify_to.notify_fields.fields[0].api_name"
          }
        ]
      },
      "message": "Ambiguity during processing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — SocialActionDetailsMissingResponse

Error response: DEPENDENT_FIELD_MISSING  - social action details/content missing

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "details",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details"
      },
      "message": "Required dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — CircuitsDetailsMissingResponse

Error response: MANDATORY_NOT_FOUND  - circuits details or circuit_id missing

```json
{
  "workflow_rules": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "details",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details"
      },
      "message": "Required field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TagInvalidResponse

Error response: INVALID_DATA  - tag name/id does not exist for the module

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "tags",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.tags[0]"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TagAmbiguityResponse

Error response: AMBIGUITY_DUE_TO  - tag name and id resolve to different tags

```json
{
  "workflow_rules": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "name",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.tags[0].name"
          },
          {
            "api_name": "id",
            "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.tags[0].id"
          }
        ]
      },
      "message": "Ambiguity during processing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — TagEmptyResponse

Error response: INVALID_DATA  - tags array is empty

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "tags",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.tags"
      },
      "message": "Tags array cannot be empty",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — EmailCreateRecordModuleInvalidResponse

Error response: INVALID_DATA  - create_record_email module must be Leads or Contacts

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "module",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.module"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — EmailCreateRecordTooManyMappingsResponse

Error response: LIMIT_EXCEEDED  - create_record_email allows exactly 1 field_mapping

```json
{
  "workflow_rules": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "api_name": "field_mappings",
        "limit": 1,
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.field_mappings"
      },
      "message": "too many records",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ConvertDependentFieldMissingResponse

Error response: DEPENDENT_FIELD_MISSING  - convert action missing mandatory fields for Leads

```json
{
  "workflow_rules": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "api_name": "add_to_existing_contact",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.add_to_existing_contact"
      },
      "message": "Required dependent field is missing",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — ConnectedRecordModuleInvalidResponse

Error response: INVALID_DATA  - create_connected_record module is not a valid child module

```json
{
  "workflow_rules": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "module",
        "json_path": "$.workflow_rules[0].conditions[0].instant_actions.actions[0].details.module"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse

Error response: NO_PERMISSION  - manage automation permission missing

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "MANAGE_WORKFLOW"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```

### Status `403` — `application/json` — WorkflowRulesPermission

Error response: NO_PERMISSION  - workflow rules feature not available

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "WORKFLOW_RULES"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```

### Status `403` — `application/json` — FeatureNotSupportedResponse

Error response: FEATURE_NOT_SUPPORTED  - workflow feature not available in this edition

```json
{
  "code": "FEATURE_NOT_SUPPORTED",
  "details": {},
  "message": "feature not available in this edition",
  "status": "error"
}
```
