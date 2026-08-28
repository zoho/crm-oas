# Examples: getModuleByApiName

**GET /settings/modules/{moduleIdentifier}**

## Parameter examples

### `include_inner_details` (query) — FieldsLookupQueryDetailsCriteria

Include query_details.criteria within lookup details

```json
"fields.lookup.query_details.criteria"
```

## Response examples

### Status `200` — `application/json` — LeadsModule

Standard CRM module - Leads

```json
{
  "modules": [
    {
      "private_profile": null,
      "global_search_supported": true,
      "activity_badge": "Enabled",
      "$field_states": [
        "convert_scheduler"
      ],
      "recycle_bin_on_delete": true,
      "plural_label": "Leads",
      "presence_sub_menu": true,
      "chart_view": false,
      "id": "111111000000002648",
      "per_page": 50,
      "$properties": [
        "$approval_state",
        "$wizard_connection_path",
        "$converted_detail",
        "$cpq_executions",
        "$currency_symbol",
        "$zia_owner_assignment",
        "$review",
        "$review_process",
        "$approval",
        "$in_merge",
        "$process_flow",
        "$orchestration",
        "$pathfinder",
        "$stop_processing",
        "$data_source_details",
        "$zia_visions",
        "$layout_id",
        "$editable",
        "$field_states",
        "$locked_for_me",
        "$sharing_permission"
      ],
      "visibility": 1,
      "sub_menu_available": true,
      "profiles": [
        {
          "name": "Administrator",
          "id": "111111000000000497"
        },
        {
          "name": "Standard",
          "id": "111111000000000499"
        },
        {
          "name": "test",
          "id": "111111000000236122"
        },
        {
          "name": "Team User",
          "id": "111111000000263146"
        }
      ],
      "$on_demand_properties": [
        "$blocked_reason"
      ],
      "kanban_view_supported": true,
      "web_link": null,
      "lookup_field_properties": {
        "fields": [
          {
            "sequence_number": 1,
            "api_name": "Full_Name",
            "id": "111111000000004814"
          },
          {
            "sequence_number": 2,
            "api_name": "Company",
            "id": "111111000000004808"
          },
          {
            "sequence_number": 3,
            "api_name": "Email",
            "id": "111111000000004818"
          },
          {
            "sequence_number": 4,
            "api_name": "Phone",
            "id": "111111000000004820"
          },
          {
            "sequence_number": 5,
            "api_name": "Lead_Source",
            "id": "111111000000004828"
          },
          {
            "sequence_number": 6,
            "api_name": "Owner",
            "id": "111111000000004806"
          }
        ]
      },
      "viewable": true,
      "api_name": "Leads",
      "public_fields_configured": true,
      "module_name": "Leads",
      "chart_view_supported": true,
      "custom_view": {
        "display_value": "All Leads",
        "created_time": null,
        "access_type": "public",
        "criteria": {
          "comparator": "equal",
          "field": {
            "api_name": "Converted__s",
            "id": "111111000000004906"
          },
          "type": "value",
          "value": false
        },
        "system_name": "ALLVIEWS",
        "sort_by": null,
        "created_by": null,
        "shared_to": null,
        "default": true,
        "modified_time": null,
        "name": "All Open Leads",
        "system_defined": true,
        "modified_by": null,
        "id": "111111000000051262",
        "fields": [
          {
            "api_name": "Full_Name",
            "_pin": false,
            "id": "111111000000004814"
          },
          {
            "api_name": "Company",
            "_pin": false,
            "id": "111111000000004808"
          },
          {
            "api_name": "Email",
            "_pin": false,
            "id": "111111000000004818"
          },
          {
            "api_name": "Phone",
            "_pin": false,
            "id": "111111000000004820"
          },
          {
            "api_name": "Lead_Source",
            "_pin": false,
            "id": "111111000000004828"
          },
          {
            "api_name": "Owner",
            "_pin": false,
            "id": "111111000000004806"
          }
        ],
        "category": "public_views",
        "last_accessed_time": "2025-11-24T16:47:11+05:30",
        "locked": false,
        "sort_order": null,
        "favorite": null
      },
      "parent_module": {},
      "status": "visible",
      "has_more_profiles": false,
      "access_type": "org_based",
      "kanban_view": false,
      "deletable": true,
      "description": null,
      "creatable": true,
      "filter_status": true,
      "showleadchainsync": true,
      "show_social": true,
      "show_visitor": true,
      "show_googlesync": true,
      "showtiktoksync": true,
      "show_webform": true,
      "showfacebooksync": true,
      "show_emailparser": true,
      "showlinkedinsync": true,
      "masked_fields_count": 0,
      "modified_time": "2025-12-18T16:00:57+05:30",
      "actual_plural_label": "Leads",
      "lookupable": true,
      "isBlueprintSupported": true,
      "related_list_properties": {
        "sort_by": null,
        "fields": [
          "Full_Name",
          "Company",
          "Email",
          "Lead_Source",
          "Lead_Status",
          "Phone"
        ],
        "sort_order": null
      },
      "convertable": true,
      "editable": true,
      "actual_singular_label": "Lead",
      "display_field": "Full_Name",
      "search_layout_fields": [
        "Owner",
        "Company",
        "Email",
        "Phone",
        "Lead_Source",
        "Full_Name"
      ],
      "show_as_tab": true,
      "sequence_number": 2,
      "singular_label": "Lead",
      "api_supported": true,
      "quick_create": true,
      "modified_by": {
        "name": "Rajaa",
        "id": "111111000000057804"
      },
      "generated_type": "default",
      "feeds_required": false,
      "arguments": [],
      "profile_count": 4,
      "business_card_field_limit": 5
    }
  ]
}
```

### Status `200` — `application/json` — CustomModuleTeamBased

Custom module with team-based access

```json
{
  "modules": [
    {
      "has_more_profiles": false,
      "access_type": "team_based",
      "private_profile": {
        "name": "Admins",
        "id": "111111000000000501"
      },
      "global_search_supported": true,
      "related_lists": [
        {
          "visibility": 10,
          "module": {
            "api_name": "Notes",
            "id": "111111000000002676"
          },
          "personality_name": "NOTESPERSONALITY",
          "record_operations": {
            "edit": false,
            "create": false,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "1",
          "display_label": "Notes",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Notes",
          "customize_display_label": false,
          "name": "Notes",
          "action": null,
          "href": "sdfvg/{ENTITYID}/Notes",
          "id": "111111000000270034",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "Attachments",
            "id": "111111000000000011"
          },
          "personality_name": "ATTACHMENTSPERSONALITY",
          "record_operations": {
            "edit": false,
            "create": false,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "2",
          "display_label": "Attachments",
          "customize_sort": true,
          "customize_fields": false,
          "api_name": "Attachments",
          "customize_display_label": false,
          "name": "Attachments",
          "action": null,
          "href": "sdfvg/{ENTITYID}/Attachments",
          "id": "111111000000270036",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "Emails",
            "id": "111111000000002772"
          },
          "personality_name": "EMAILSPERSONALITY",
          "record_operations": {
            "edit": false,
            "create": false,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "3",
          "display_label": "Emails",
          "customize_sort": true,
          "customize_fields": false,
          "api_name": "Emails",
          "customize_display_label": false,
          "name": "Emails",
          "action": null,
          "href": null,
          "id": "111111000000270038",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "Tasks",
            "id": "111111000000002670"
          },
          "personality_name": "TASKSPERSONALITY",
          "record_operations": {
            "edit": true,
            "create": true,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "6",
          "display_label": "Open Tasks",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Tasks",
          "customize_display_label": false,
          "name": "Tasks",
          "action": null,
          "href": "sdfvg/{ENTITYID}/Tasks",
          "id": "111111000000270044",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "Events",
            "id": "111111000000002672"
          },
          "personality_name": "EVENTSPERSONALITY",
          "record_operations": {
            "edit": true,
            "create": true,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "7",
          "display_label": "Open Meetings",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Events",
          "customize_display_label": false,
          "name": "Events",
          "action": null,
          "href": "sdfvg/{ENTITYID}/Events",
          "id": "111111000000270048",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "Calls",
            "id": "111111000000002674"
          },
          "personality_name": "CALLSPERSONALITY",
          "record_operations": {
            "edit": true,
            "create": true,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "8",
          "display_label": "Open Calls",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Calls",
          "customize_display_label": false,
          "name": "Calls",
          "action": null,
          "href": "sdfvg/{ENTITYID}/Calls",
          "id": "111111000000270046",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "Tasks",
            "id": "111111000000002670"
          },
          "personality_name": "TASKSHISTORYPERSONALITY",
          "record_operations": {
            "edit": true,
            "create": true,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "9",
          "display_label": "Closed Tasks",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Tasks_History",
          "customize_display_label": false,
          "name": "Tasks History",
          "action": null,
          "href": "sdfvg/{ENTITYID}/Tasks_History",
          "id": "111111000000270052",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "Events",
            "id": "111111000000002672"
          },
          "personality_name": "EVENTSHISTORYPERSONALITY",
          "record_operations": {
            "edit": true,
            "create": true,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "10",
          "display_label": "Closed Meetings",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Events_History",
          "customize_display_label": false,
          "name": "Events History",
          "action": null,
          "href": "sdfvg/{ENTITYID}/Events_History",
          "id": "111111000000270056",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "Calls",
            "id": "111111000000002674"
          },
          "personality_name": "CALLSHISTORYPERSONALITY",
          "record_operations": {
            "edit": true,
            "create": true,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "11",
          "display_label": "Closed Calls",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Calls_History",
          "customize_display_label": false,
          "name": "Calls History",
          "action": null,
          "href": "sdfvg/{ENTITYID}/Calls_History",
          "id": "111111000000270054",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": {
            "api_name": "CheckLists",
            "id": "111111000000002692"
          },
          "personality_name": "CHECKLISTSPERSONALITY",
          "record_operations": {
            "edit": false,
            "create": false,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "default",
          "sequence_number": "12",
          "display_label": "Checklists",
          "customize_sort": false,
          "customize_fields": false,
          "api_name": "CheckLists",
          "customize_display_label": false,
          "name": "CheckLists",
          "action": null,
          "href": "sdfvg/{ENTITYID}/CheckLists",
          "id": "111111000000270060",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": null,
          "parent_related_lists": null,
          "personality_name": "CHRONOLOGICALVIEWPERSONALITY",
          "record_operations": {
            "edit": true,
            "create": true,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "grouped",
          "sequence_number": "13",
          "display_label": "ChronologicalView",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Activities_Chronological_View",
          "customize_display_label": true,
          "name": "ChronologicalView",
          "action": null,
          "href": null,
          "id": "111111000000270050",
          "status": "visible"
        },
        {
          "visibility": 10,
          "module": null,
          "parent_related_lists": null,
          "personality_name": "CHRONOLOGICALVIEWHISTORYPERSONALITY",
          "record_operations": {
            "edit": true,
            "create": true,
            "bulk_edit": false,
            "delete": false,
            "disassociate": false,
            "assign": false
          },
          "type": "grouped",
          "sequence_number": "14",
          "display_label": "ChronologicalView History",
          "customize_sort": true,
          "customize_fields": true,
          "api_name": "Activities_Chronological_View_History",
          "customize_display_label": true,
          "name": "ChronologicalView History",
          "action": null,
          "href": null,
          "id": "111111000000270058",
          "status": "visible"
        }
      ],
      "deletable": true,
      "description": null,
      "source": "crm",
      "creatable": true,
      "layouts": [
        {
          "display_label": "Standard",
          "name": "Standard",
          "profiles": [
            {
              "_default_assignment_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              },
              "default": true,
              "name": "Admins",
              "id": "111111000000000501",
              "_default_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              }
            },
            {
              "_default_assignment_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              },
              "default": true,
              "name": "Managers",
              "id": "111111000000000503",
              "_default_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              }
            },
            {
              "_default_assignment_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              },
              "default": true,
              "name": "Members",
              "id": "111111000000000505",
              "_default_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              }
            },
            {
              "_default_assignment_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              },
              "default": true,
              "name": "Participants",
              "id": "111111000000000507",
              "_default_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              }
            },
            {
              "_default_assignment_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              },
              "default": true,
              "name": "Requesters",
              "id": "111111000000000509",
              "_default_view": {
                "name": "Standard",
                "id": "111111000000268895",
                "type": "layout"
              }
            }
          ],
          "generated_type": "system",
          "id": "111111000000268895",
          "source": "crm",
          "status": "active"
        }
      ],
      "recycle_bin_on_delete": true,
      "business_card_fields": [
        {
          "api_name": "Name",
          "id": "111111000000268938"
        },
        {
          "api_name": "Owner",
          "id": "111111000000268940"
        },
        {
          "api_name": "Email",
          "id": "111111000000268942"
        },
        {
          "api_name": "Modified_By",
          "id": "111111000000268948"
        }
      ],
      "modified_time": "2025-11-21T12:12:26+05:30",
      "plural_label": "sdfvg",
      "presence_sub_menu": true,
      "actual_plural_label": "sdfvg",
      "lookupable": true,
      "id": "111111000000268896",
      "isBlueprintSupported": true,
      "per_page": 10,
      "$properties": [
        "$approval_state",
        "$wizard_connection_path",
        "$cpq_executions",
        "$currency_symbol",
        "$review",
        "$review_process",
        "$approval",
        "$in_merge",
        "$process_flow",
        "$orchestration",
        "$pathfinder",
        "$zia_visions",
        "$editable",
        "$field_states",
        "$sharing_permission"
      ],
      "visibility": 1,
      "convertable": false,
      "sub_menu_available": true,
      "editable": true,
      "actual_singular_label": "sdfvgdfvsg",
      "profiles": [
        {
          "name": "Admins",
          "id": "111111000000000501"
        },
        {
          "name": "Managers",
          "id": "111111000000000503"
        },
        {
          "name": "Members",
          "id": "111111000000000505"
        },
        {
          "name": "Participants",
          "id": "111111000000000507"
        },
        {
          "name": "Requesters",
          "id": "111111000000000509"
        }
      ],
      "$on_demand_properties": [
        "$blocked_reason"
      ],
      "kanban_view_supported": true,
      "web_link": null,
      "sequence_number": 125,
      "singular_label": "sdfvgdfvsg",
      "lookup_field_properties": {
        "fields": [
          {
            "sequence_number": 1,
            "api_name": "Name",
            "id": "111111000000268938"
          },
          {
            "sequence_number": 2,
            "api_name": "Email",
            "id": "111111000000268942"
          },
          {
            "sequence_number": 3,
            "api_name": "Owner",
            "id": "111111000000268940"
          },
          {
            "sequence_number": 4,
            "api_name": "Modified_Time",
            "id": "111111000000268952"
          }
        ]
      },
      "viewable": true,
      "api_supported": true,
      "api_name": "sdfvg",
      "quick_create": true,
      "modified_by": {
        "name": "12345FIRST1234567890123456789012345678901234567890 123456LAST0987654321123456789009876543211234567890",
        "id": "111111000000057804"
      },
      "generated_type": "custom",
      "feeds_required": false,
      "public_fields_configured": false,
      "arguments": [],
      "module_name": "CustomModule3",
      "chart_view_supported": true,
      "profile_count": 5,
      "business_card_field_limit": 5,
      "custom_view": {
        "display_value": "All sdfvg",
        "access_type": "public",
        "criteria": null,
        "sort_by": null,
        "default": true,
        "modified_time": null,
        "id": "111111000000268908",
        "last_accessed_time": null,
        "locked": false,
        "sort_order": null,
        "created_time": null,
        "wrap_text": true,
        "system_name": "ALLVIEWS",
        "module": {
          "api_name": "sdfvg",
          "id": "111111000000268896"
        },
        "created_by": null,
        "shared_to": null,
        "name": "CustomModule Default CustomView",
        "system_defined": true,
        "modified_by": null,
        "fields": [
          {
            "api_name": "Name",
            "_pin": false,
            "id": "111111000000268938"
          },
          {
            "api_name": "Email",
            "_pin": false,
            "id": "111111000000268942"
          },
          {
            "api_name": "Owner",
            "_pin": false,
            "id": "111111000000268940"
          },
          {
            "api_name": "Modified_Time",
            "_pin": false,
            "id": "111111000000268952"
          }
        ],
        "category": "public_views",
        "favorite": null
      },
      "parent_module": {},
      "status": "visible"
    }
  ]
}
```

### Status `200` — `application/json` — StaticSubformModule

Static subform module

```json
{
  "modules": [
    {
      "private_profile": null,
      "global_search_supported": true,
      "recycle_bin_on_delete": true,
      "plural_label": "Subform 2",
      "presence_sub_menu": false,
      "id": "111111000000270418",
      "visibility": 2,
      "sub_menu_available": false,
      "static_subform_properties": {
        "fields": [
          {
            "api_name": "Pick_List_1",
            "id": "111111000000271161"
          }
        ]
      },
      "profiles": [
        {
          "name": "Administrator",
          "id": "111111000000000497"
        }
      ],
      "viewable": true,
      "api_name": "Subform_2",
      "public_fields_configured": false,
      "module_name": "LinkingModule2",
      "parent_module": {
        "api_name": "CM",
        "id": "111111000000257585"
      },
      "status": "visible",
      "has_more_profiles": false,
      "access_type": "org_based",
      "deletable": true,
      "description": null,
      "creatable": true,
      "modified_time": "2025-11-21T15:10:43+05:30",
      "actual_plural_label": "Subform 2",
      "lookupable": false,
      "isBlueprintSupported": false,
      "convertable": false,
      "editable": true,
      "actual_singular_label": "Subform 2",
      "show_as_tab": false,
      "sequence_number": 25,
      "singular_label": "Subform 2",
      "api_supported": true,
      "quick_create": false,
      "modified_by": {
        "name": "Rajaa",
        "id": "111111000000057804"
      },
      "generated_type": "static_subform",
      "feeds_required": false,
      "arguments": [],
      "profile_count": 4,
      "business_card_field_limit": 5
    }
  ]
}
```

### Status `200` — `application/json` — FieldTrackerModule

Field tracker module

```json
{
  "modules": [
    {
      "private_profile": null,
      "global_search_supported": true,
      "recycle_bin_on_delete": true,
      "track_current_data": true,
      "plural_label": "Pick List 1 History",
      "presence_sub_menu": false,
      "id": "111111000000271197",
      "visibility": 2,
      "sub_menu_available": false,
      "profiles": [
        {
          "name": "Administrator",
          "id": "111111000000000497"
        }
      ],
      "viewable": true,
      "api_name": "Pick_List_1_History",
      "public_fields_configured": false,
      "module_name": "LinkingModule3",
      "parent_module": {
        "api_name": "CM",
        "id": "111111000000257585"
      },
      "status": "user_hidden",
      "has_more_profiles": false,
      "access_type": "org_based",
      "deletable": false,
      "description": null,
      "creatable": false,
      "modified_time": "2025-11-21T16:47:22+05:30",
      "actual_plural_label": "Pick List 1 History",
      "lookupable": false,
      "isBlueprintSupported": false,
      "convertable": false,
      "editable": false,
      "actual_singular_label": "Pick List 1 History",
      "show_as_tab": false,
      "sequence_number": 126,
      "singular_label": "Pick List 1 History",
      "api_supported": true,
      "quick_create": false,
      "modified_by": {
        "name": "Rajaa",
        "id": "111111000000057804"
      },
      "generated_type": "field_tracker",
      "feeds_required": false,
      "arguments": [],
      "profile_count": 1,
      "business_card_field_limit": 5
    }
  ]
}
```

### Status `200` — `application/json` — ModuleWithTerritory

Module with territory assignment

```json
{
  "modules": [
    {
      "private_profile": null,
      "global_search_supported": true,
      "recycle_bin_on_delete": true,
      "plural_label": "Contacts",
      "presence_sub_menu": true,
      "id": "111111000000002650",
      "visibility": 1,
      "sub_menu_available": true,
      "profiles": [
        {
          "name": "Administrator",
          "id": "111111000000000497"
        },
        {
          "name": "Standard",
          "id": "111111000000000499"
        }
      ],
      "viewable": true,
      "api_name": "Contacts",
      "public_fields_configured": false,
      "module_name": "Contacts",
      "parent_module": {},
      "status": "visible",
      "has_more_profiles": false,
      "access_type": "org_based",
      "deletable": true,
      "description": null,
      "creatable": true,
      "modified_time": "2025-11-05T12:27:24+05:30",
      "actual_plural_label": "Contacts",
      "lookupable": true,
      "isBlueprintSupported": true,
      "convertable": false,
      "editable": true,
      "actual_singular_label": "Contact",
      "show_as_tab": true,
      "sequence_number": 3,
      "singular_label": "Contact",
      "api_supported": true,
      "quick_create": true,
      "modified_by": {
        "name": "Rajaa",
        "id": "111111000000057804"
      },
      "generated_type": "default",
      "feeds_required": false,
      "arguments": [],
      "profile_count": 4,
      "business_card_field_limit": 5,
      "territory": {
        "name": "All Territories",
        "id": "0",
        "subordinates": false
      }
    }
  ]
}
```

### Status `400` — `application/json` — UnsupportedModule

Unsupported module API name

```json
{
  "code": "NOT_SUPPORTED",
  "details": {
    "resource_path_index": 2
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — ModuleNotSupportedInApi

Module not supported in API

```json
{
  "code": "NOT_SUPPORTED",
  "details": {},
  "message": "the given module is not supported in api",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiNotSupported

API not supported error

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {},
  "message": "api not supported",
  "status": "error"
}
```

### Status `400` — `application/json` — ApiVersionNotSupported

API version not supported error

```json
{
  "code": "API_NOT_SUPPORTED",
  "details": {
    "supported_version": 2
  },
  "message": "The api version 1 is not supported. Please use the version 2 or above.",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequest

Invalid request parameters

```json
{
  "code": "INVALID_REQUEST",
  "details": {},
  "message": "api name cannot be empty",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module identifier

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "resource_path_index": 2
  },
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```
