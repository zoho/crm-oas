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
