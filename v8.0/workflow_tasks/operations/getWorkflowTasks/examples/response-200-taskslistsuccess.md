Successful response listing automation tasks with different feature types and field mapping configurations

```json
{
  "tasks": [
    {
      "created_time": "2025-08-15T10:30:00+00:00",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "singular_label": "Lead",
        "plural_label": "Leads",
        "api_name": "Leads",
        "moduleName": "Leads",
        "id": "3479217000000000125"
      },
      "related_module": null,
      "deletable": true,
      "source": "crm",
      "created_by": {
        "name": "John Smith",
        "id": "3479217000000539001"
      },
      "notify": true,
      "feature_type": "workflow",
      "field_mappings": [
        {
          "display_value": "Follow up on new lead",
          "field": {
            "api_name": "Subject",
            "id": "3479217000000000221"
          },
          "type": "static",
          "value": "Follow up on new lead"
        },
        {
          "display_value": "Trigger Date plus 2 business day(s)",
          "field": {
            "api_name": "Due_Date",
            "id": "3479217000000000223"
          },
          "type": "execution_time",
          "value": {
            "period": "business_days",
            "unit": "2",
            "trigger_field": "${CURRENTTIME}",
            "sign": "plus"
          }
        },
        {
          "display_value": "Not Started",
          "field": {
            "api_name": "Status",
            "id": "3479217000000000229"
          },
          "type": "static",
          "value": "Not Started"
        },
        {
          "display_value": "High",
          "field": {
            "api_name": "Priority",
            "id": "3479217000000000231"
          },
          "type": "static",
          "value": "High"
        }
      ],
      "modified_time": "2025-09-10T14:20:00+00:00",
      "associated": true,
      "modified_by": {
        "name": "John Smith",
        "id": "3479217000000539001"
      },
      "name": "Follow up on new lead",
      "id": "3479217000002131001"
    },
    {
      "created_time": "2025-09-05T08:00:00+00:00",
      "lock_status": {
        "locked": true
      },
      "editable": false,
      "module": {
        "singular_label": "Deal",
        "plural_label": "Deals",
        "api_name": "Deals",
        "moduleName": "Deals",
        "id": "3479217000000000137"
      },
      "related_module": null,
      "deletable": false,
      "source": "crm",
      "created_by": {
        "name": "Jane Doe",
        "id": "3479217000000539002"
      },
      "notify": false,
      "feature_type": "approval_process",
      "field_mappings": [
        {
          "display_value": "${Deals.Deal_Name}",
          "field": {
            "api_name": "Subject",
            "id": "3479217000000000221"
          },
          "type": "merge_field",
          "value": "${Deals.Deal_Name}"
        },
        {
          "display_value": "Trigger Date plus 5 day(s)",
          "field": {
            "api_name": "Due_Date",
            "id": "3479217000000000223"
          },
          "type": "execution_time",
          "value": {
            "period": "days",
            "unit": "5",
            "trigger_field": "${CURRENTTIME}",
            "sign": "plus"
          }
        },
        {
          "display_value": "In Progress",
          "field": {
            "api_name": "Status",
            "id": "3479217000000000229"
          },
          "type": "static",
          "value": "In Progress"
        },
        {
          "display_value": "Highest",
          "field": {
            "api_name": "Priority",
            "id": "3479217000000000231"
          },
          "type": "static",
          "value": "Highest"
        }
      ],
      "modified_time": "2025-09-05T08:00:00+00:00",
      "associated": true,
      "modified_by": {
        "name": "Jane Doe",
        "id": "3479217000000539002"
      },
      "name": "${Deals.Deal_Name}",
      "id": "3479217000002131002"
    },
    {
      "created_time": "2025-10-01T12:00:00+00:00",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "singular_label": "Contact",
        "plural_label": "Contacts",
        "api_name": "Contacts",
        "moduleName": "Contacts",
        "id": "3479217000000000129"
      },
      "related_module": {
        "singular_label": "Onboarding Flow",
        "plural_label": "Onboarding Flows",
        "api_name": "Onboarding_Flows",
        "id": "3479217000002650297",
        "module_name": "ProcessFlow1"
      },
      "deletable": true,
      "source": "crm",
      "created_by": {
        "name": "John Smith",
        "id": "3479217000000539001"
      },
      "notify": true,
      "feature_type": "kiosks",
      "field_mappings": [
        {
          "display_value": "Onboard new contact",
          "field": {
            "api_name": "Subject",
            "id": "3479217000000000221"
          },
          "type": "static",
          "value": "Onboard new contact"
        },
        {
          "display_value": "Trigger Date plus 1 business day(s)",
          "field": {
            "api_name": "Due_Date",
            "id": "3479217000000000223"
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
          "display_value": "Not Started",
          "field": {
            "api_name": "Status",
            "id": "3479217000000000229"
          },
          "type": "static",
          "value": "Not Started"
        },
        {
          "display_value": "Normal",
          "field": {
            "api_name": "Priority",
            "id": "3479217000000000231"
          },
          "type": "static",
          "value": "Normal"
        },
        {
          "display_value": "${Contacts.Owner}",
          "field": {
            "api_name": "Owner",
            "id": "3479217000000000233"
          },
          "type": "merge_field",
          "value": "${Contacts.Owner}"
        }
      ],
      "modified_time": "2025-10-15T09:45:00+00:00",
      "associated": false,
      "modified_by": {
        "name": "John Smith",
        "id": "3479217000000539001"
      },
      "name": "Onboard new contact",
      "id": "3479217000002654408"
    },
    {
      "created_time": "2025-07-20T16:30:00+00:00",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "singular_label": "Task",
        "plural_label": "Tasks",
        "api_name": "Tasks",
        "moduleName": "Tasks",
        "id": "3479217000000000143"
      },
      "related_module": null,
      "deletable": true,
      "source": "crm",
      "created_by": {
        "name": "Jane Doe",
        "id": "3479217000000539002"
      },
      "notify": false,
      "feature_type": "blueprint",
      "field_mappings": [
        {
          "display_value": "Review escalated task",
          "field": {
            "api_name": "Subject",
            "id": "3479217000000000221"
          },
          "type": "static",
          "value": "Review escalated task"
        },
        {
          "display_value": "Trigger Date plus 3 day(s)",
          "field": {
            "api_name": "Due_Date",
            "id": "3479217000000000223"
          },
          "type": "execution_time",
          "value": {
            "period": "days",
            "unit": "3",
            "trigger_field": "${CURRENTTIME}",
            "sign": "plus"
          }
        },
        {
          "display_value": "Waiting on someone else",
          "field": {
            "api_name": "Status",
            "id": "3479217000000000229"
          },
          "type": "static",
          "value": "Waiting on someone else"
        },
        {
          "display_value": "Low",
          "field": {
            "api_name": "Priority",
            "id": "3479217000000000231"
          },
          "type": "static",
          "value": "Low"
        }
      ],
      "modified_time": "2025-10-20T11:15:00+00:00",
      "associated": false,
      "modified_by": {
        "name": "Jane Doe",
        "id": "3479217000000539002"
      },
      "name": "Review escalated task",
      "id": "3479217000002131012"
    }
  ],
  "info": {
    "per_page": 200,
    "count": 4,
    "page": 1,
    "more_records": false
  }
}
```
