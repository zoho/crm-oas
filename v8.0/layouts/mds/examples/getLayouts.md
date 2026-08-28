# Examples: getLayouts

**GET /settings/layouts**

## Parameter examples

### `module` (query) — StandardModule

Standard module

```json
"Leads"
```

### `module` (query) — CustomModule

Custom module

```json
"Custom_Projects"
```

### `mode` (query) — BusinessCard

Business card mode

```json
"business_card"
```

### `mode` (query) — QuickCreate

Quick create mode

```json
"quick_create"
```

### `mode` (query) — AllModes

All modes

```json
"all"
```

### `include` (query) — IncludeTotalProfiles

Include total profiles

```json
"total_profiles"
```

### `include_inner_details` (query) — ProfileType

Include profile type information

```json
"profiles.type"
```

### `include_inner_details` (query) — FieldsPortalUserTypes

Include portal user types for fields

```json
"fields.portal_user_types"
```

### `include_inner_details` (query) — FieldsAllowedPermissions

Include allowed permissions to update for fields

```json
"fields.allowed_permissions_to_update"
```

### `include_inner_details` (query) — MultipleDetails

Include multiple inner details

```json
"profiles.type,fields.portal_user_types"
```

### `include_element_types` (query) — FieldsType

Field type

```json
"field"
```

### `include_element_types` (query) — MirrorFieldType

Mirror field type

```json
"mirror_field"
```

## Response examples

### Status `200` — `application/json` — LayoutSuccessResponse

Successful layout retrieval for custom module

```json
{
  "layouts": [
    {
      "has_more_profiles": false,
      "created_time": "2025-11-20T14:44:37+05:30",
      "convert_mapping": {
        "Contacts": {
          "display_label": "Standard",
          "name": "Standard",
          "id": "4832675000000095059"
        },
        "Deals": {
          "display_label": "Standard",
          "name": "Standard",
          "id": "4832675000000095023",
          "fields": [
            {
              "api_name": "Amount",
              "field_label": "Amount",
              "id": "4832675000000000517",
              "required": false
            },
            {
              "api_name": "Deal_Name",
              "field_label": "Potential Name",
              "id": "4832675000000000519",
              "required": true
            },
            {
              "api_name": "Closing_Date",
              "field_label": "Closing Date",
              "id": "4832675000000000521",
              "required": false
            },
            {
              "api_name": "Stage",
              "field_label": "Stage",
              "id": "4832675000000000525",
              "required": true
            },
            {
              "api_name": "Pipeline",
              "field_label": "Pipeline",
              "id": "4832675000000236001",
              "required": true
            }
          ]
        },
        "Accounts": {
          "display_label": "Standard",
          "name": "Standard",
          "id": "4832675000000095047"
        }
      },
      "visible": true,
      "created_for": null,
      "portal_user_types": [
        {
          "default": true,
          "name": "ClientPortal",
          "id": "4832675000001280243",
          "_default_view": {
            "name": "Standard",
            "id": "4832675000000095059",
            "type": "layout"
          }
        }
      ],
      "profiles": [
        {
          "_default_assignment_view": {
            "name": "Standard",
            "id": "2047208000005744376",
            "type": "layout"
          },
          "default": true,
          "name": "Administrator",
          "id": "2047208000000015972",
          "_default_view": {
            "name": "Standard",
            "id": "2047208000005744376",
            "type": "layout"
          }
        },
        {
          "_default_assignment_view": {
            "name": "wizard Association",
            "id": "4832675000001271930",
            "type": "layout"
          },
          "default": true,
          "name": "Administrator",
          "id": "4832675000000015972",
          "_default_view": {
            "name": "Testing wizard 1",
            "id": "4832675000001280138",
            "type": "wizard"
          },
          "type": "normal_profile"
        },
        {
          "_default_assignment_view": {
            "name": "Testing Canvas 1",
            "id": "4832675000001280644",
            "type": "canvas"
          },
          "default": true,
          "name": "Administrator",
          "id": "4832675000000015972",
          "_default_view": {
            "name": "Testing wizard 1",
            "id": "4832675000001280138",
            "type": "wizard"
          },
          "type": "normal_profile"
        }
      ],
      "source": "campaign_integration",
      "created_by": {
        "name": "Ajay Ajay",
        "id": "2047208000000456001"
      },
      "sections": [
        {
          "isSubformSection": false,
          "type": "used",
          "display_label": "OAS Testing Module Image",
          "mode": "default_create",
          "sequence_number": 1,
          "actions_allowed": {
            "add_field": false,
            "rename": false,
            "change_tab_traversal": false,
            "reorder": false,
            "delete": false,
            "remove_field": false,
            "change_column_count": false
          },
          "tab_traversal": "left_to_right",
          "api_name": "Record_Image__s",
          "column_count": 1,
          "name": "Record Image",
          "generated_type": "default",
          "id": "2047208000005744381",
          "fields": [
            {
              "associated_module": null,
              "webhook": false,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "OAS Testing Module Image",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "image_enable",
                "add_to_other_layouts"
              ],
              "required": false,
              "display_label": "Record Image",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "2047208000005744479",
              "created_time": null,
              "filterable": false,
              "visible": true,
              "refer_from_field": null,
              "portal_user_types": [
                {
                  "permission_type": "hidden",
                  "name": "ClientPortal",
                  "id": "4832675000001280243"
                }
              ],
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "2047208000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "2047208000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": false,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Record_Image",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 66,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 255,
              "column_name": "PHOTO_FILEID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 1,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "profileimage",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Account Owner 1",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "fieldlabel",
                "removal",
                "deletion",
                "tooltip",
                "add_to_other_layouts",
                "lookup_filter",
                "recordaccess"
              ],
              "required": false,
              "display_label": "Account Owner 1",
              "read_only": false,
              "association_details": {
                "related_field": {
                  "api_name": "Owner",
                  "id": "4832675000000000377"
                },
                "lookup_field": {
                  "api_name": "Lookupfol",
                  "id": "4832675000000849962"
                }
              },
              "businesscard_supported": true,
              "sharing_properties": {
                "scheduler_status": "completed",
                "share_permission": "full-access",
                "share_preference_enabled": true
              },
              "multi_module_lookup": {},
              "id": "4832675000000849987",
              "created_time": "2025-11-18T13:09:25+05:30",
              "filterable": true,
              "visible": true,
              "refer_from_field": {
                "id": "4832675000000000377"
              },
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "4832675000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "4832675000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Account_Owner_1",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "private": null,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 221,
              "validation_rule": null,
              "modified_time": "2025-11-18T13:09:25+05:30",
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": true,
              "lookup": {
                "revalidate_filter_during_edit": false
              },
              "hipaa_compliance": null,
              "convert_mapping": {
                "Contacts": null,
                "Deals": null,
                "Accounts": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 50,
              "column_name": "LEADCF511",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 52,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "userlookup",
              "formula": {},
              "additional_column": null,
              "hipaa_compliance_enabled": false,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "mirror_field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Appointment For",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fixed_position",
                "select_modules"
              ],
              "required": true,
              "display_label": "Appointment For",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {
                "display_label": "Appointments",
                "dynamic_module_addition_allowed": false,
                "api_name": "Appointments__s",
                "modules": [
                  {
                    "api_name": "Contacts",
                    "module_name": "Contacts",
                    "id": "4832675000000000129"
                  }
                ]
              },
              "id": "4832675000000851259",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "4832675000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "4832675000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Appointment_For",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": true,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 132,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 1,
              "quick_sequence_number": "2",
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SEID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 2,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "multi_module_lookup",
              "formula": {},
              "additional_column": "APPOINTMENTFOR",
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Appointment For",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fixed_position",
                "select_modules"
              ],
              "required": true,
              "display_label": "Appointment For",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {
                "display_label": "Appointments",
                "api_name": "Appointments__s",
                "modules": [
                  {
                    "api_name": "Contacts",
                    "module_name": "Contacts",
                    "id": "4832675000000000129"
                  }
                ]
              },
              "id": "4832675000000851259",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "4832675000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "4832675000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Appointment_For",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": true,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 132,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 1,
              "quick_sequence_number": "2",
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SEID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 2,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "multi_module_lookup",
              "formula": {},
              "additional_column": "APPOINTMENTFOR",
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            }
          ],
          "properties": null
        },
        {
          "isSubformSection": false,
          "type": "used",
          "display_label": "OAS Testing Module Information",
          "mode": "default_create",
          "sequence_number": 2,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": true,
            "reorder": true,
            "delete": true,
            "remove_field": true,
            "change_column_count": true
          },
          "tab_traversal": "left_to_right",
          "api_name": "CustomModule_Information__s",
          "column_count": 2,
          "name": "CustomModule30 Information",
          "generated_type": "default",
          "id": "2047208000005744379",
          "fields": [
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "OAS Testing Module Name",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fieldlabel",
                "max_length_digits",
                "unique",
                "tooltip"
              ],
              "required": true,
              "display_label": "CustomModule Name",
              "allowed_permissions_to_update": {
                "read_write": true,
                "hidden": true,
                "read_only": true
              },
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "2047208000005744417",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "portal_user_types": [],
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "2047208000000015972"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Name",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": true,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 1,
              "quick_sequence_number": "1",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "NAME",
              "display_field": true,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 1,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Currency",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "removal",
                "add_to_other_layouts"
              ],
              "required": false,
              "display_label": "Currency",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "2047208000005744435",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "2047208000000015972"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Currency",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [
                {
                  "display_value": "INR",
                  "sequence_number": 1,
                  "reference_value": "INR",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "INR",
                  "id": "2047208000001015001",
                  "type": "used"
                },
                {
                  "display_value": "USD",
                  "sequence_number": 2,
                  "reference_value": "USD",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "USD",
                  "id": "2047208000002283021",
                  "type": "used"
                }
              ],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 39,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 1,
              "quick_sequence_number": "10",
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "CURRENCYISOCODE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 7,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "picklist",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "blueprint_supported": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "webhook": true,
              "field_label": "Account Site",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "required": false,
              "display_label": "Account Site",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "3359388000000121003",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "3359388000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "3359388000000015975"
                },
                {
                  "permission_type": "read_write",
                  "name": "Team User",
                  "id": "3359388000000584005"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "show_type": 7,
              "external": null,
              "api_name": "Account_Site",
              "parent_field": null,
              "unique": {},
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 1,
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "ACCOUNTSITE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 5,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "mirror_field",
              "lookup_field": {
                "id": "3359388000000000523",
                "api_name": "Account_Name"
              }
            }
          ],
          "properties": null
        },
        {
          "isSubformSection": false,
          "type": "used",
          "display_label": "Meeting Information",
          "mode": "view",
          "sequence_number": 1,
          "actions_allowed": {
            "add_field": true,
            "rename": false,
            "change_tab_traversal": false,
            "reorder": false,
            "delete": false,
            "remove_field": true,
            "change_column_count": false
          },
          "tab_traversal": "left_to_right",
          "api_name": "Event_Information1__s",
          "column_count": 1,
          "name": "Event Information",
          "generated_type": "default",
          "id": "111111000000009824",
          "fields": [
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Title",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fixed_position"
              ],
              "required": true,
              "display_label": "Meeting Title",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000004156",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Event_Title",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": true,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "quick_sequence_number": "1",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 255,
              "column_name": "SUBJECT",
              "display_field": true,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 1,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Meeting Venue",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fixed_position",
                "tooltip",
                "display_value_alphabetically",
                "default_value",
                "color_code",
                "record_category",
                "add_record_category",
                "remove_record_category",
                "rename_record_category",
                "modify_record_category_type"
              ],
              "required": true,
              "display_label": "Meeting Venue",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000071545",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                },
                {
                  "permission_type": "read_write",
                  "name": "Admins",
                  "id": "111111000000000501"
                },
                {
                  "permission_type": "read_write",
                  "name": "Managers",
                  "id": "111111000000000503"
                },
                {
                  "permission_type": "read_write",
                  "name": "Members",
                  "id": "111111000000000505"
                },
                {
                  "permission_type": "read_write",
                  "name": "Participants",
                  "id": "111111000000000507"
                },
                {
                  "permission_type": "read_write",
                  "name": "Requesters",
                  "id": "111111000000000509"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Meeting_Venue__s",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [
                {
                  "display_value": "In-office",
                  "sequence_number": 1,
                  "reference_value": "In-office",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "In-office",
                  "id": "111111000000071549",
                  "type": "used"
                },
                {
                  "display_value": "Client location",
                  "sequence_number": 2,
                  "reference_value": "Client location",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Client location",
                  "id": "111111000000071551",
                  "type": "used"
                },
                {
                  "display_value": "In-office",
                  "sequence_number": 3,
                  "reference_value": "In-office",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "In-office",
                  "id": "111111000000077054",
                  "type": "used"
                },
                {
                  "display_value": "Online",
                  "sequence_number": 4,
                  "reference_value": "Online",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Online",
                  "id": "111111000000071553",
                  "type": "used"
                }
              ],
              "system_mandatory": true,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 2,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "global_map_dependency": {
                "id": "4832675000000722441"
              },
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "MEETING_VENUE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": "Client location",
              "sortable": true,
              "sequence_number": 2,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "picklist",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "blueprint_supported": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Location",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "fixed_position",
                "field_masking"
              ],
              "required": false,
              "display_label": "Venue",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000004158",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Venue",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "quick_sequence_number": "2",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 255,
              "column_name": "LOCATION",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 3,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Provider",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "history_tracking",
                "display_value_alphabetically",
                "default_value",
                "option_add",
                "add_to_other_layouts",
                "color_code",
                "replace_values",
                "record_category",
                "add_record_category",
                "remove_record_category",
                "rename_record_category",
                "modify_record_category_type"
              ],
              "required": false,
              "display_label": "Provider",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000071546",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                },
                {
                  "permission_type": "read_write",
                  "name": "Admins",
                  "id": "111111000000000501"
                },
                {
                  "permission_type": "read_write",
                  "name": "Managers",
                  "id": "111111000000000503"
                },
                {
                  "permission_type": "read_write",
                  "name": "Members",
                  "id": "111111000000000505"
                },
                {
                  "permission_type": "read_write",
                  "name": "Participants",
                  "id": "111111000000000507"
                },
                {
                  "permission_type": "read_write",
                  "name": "Requesters",
                  "id": "111111000000000509"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Meeting_Provider__s",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 2,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "MEETING_PROVIDER",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 4,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "picklist",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "blueprint_supported": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "All day",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fixed_position"
              ],
              "required": false,
              "display_label": "All day",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000004160",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "All_day",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "boolean",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 301,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "quick_sequence_number": "3",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 5,
              "column_name": "ALLDAYEVENT",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": false,
              "sortable": true,
              "sequence_number": 5,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "boolean",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "From",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fixed_position",
                "tooltip"
              ],
              "required": true,
              "display_label": "Start DateTime",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000004162",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Start_DateTime",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": true,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 333,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "quick_sequence_number": "4",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "STARTDATETIME",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 6,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "datetime",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "To",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fixed_position",
                "tooltip"
              ],
              "required": true,
              "display_label": "End DateTime",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000004164",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "End_DateTime",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": true,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 333,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "quick_sequence_number": "5",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "ENDDATETIME",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 7,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "datetime",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Host",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": true,
              "customizable_properties": [],
              "required": false,
              "display_label": "Meeting Owner",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000004166",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Owner",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 8,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SMOWNERID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 8,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "ownerlookup",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Description",
              "tooltip": null,
              "textarea": {
                "type": "large"
              },
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "tooltip"
              ],
              "required": false,
              "display_label": "Description",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000004194",
              "created_time": null,
              "filterable": false,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Description",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 3,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 32000,
              "column_name": "DESCRIPTION",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 9,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "textarea",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": false,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Participants",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [],
              "required": false,
              "display_label": "Participants",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000004192",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 9,
              "external": null,
              "api_name": "Participants",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonarray",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 41,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "PARTICIPANTID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 10,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "bigint",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": false,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Participants Reminder",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "removal"
              ],
              "required": false,
              "display_label": "Remind Participants",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000004174",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 2,
              "external": null,
              "api_name": "Remind_Participants",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonarray",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 104,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "REMINDINVITEESAT",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 11,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "multireminder",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Tag",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Tag",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000004232",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Tag",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonarray",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 209,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 2000,
              "column_name": "TAGMODULEREFID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 12,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Contact Name",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal"
              ],
              "required": false,
              "display_label": "Who Id",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000004168",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Who_Id",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 4,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {
                "display_label": "Open Meetings",
                "revalidate_filter_during_edit": false,
                "api_name": "Events",
                "module": {
                  "api_name": "Contacts",
                  "id": "111111000000002654"
                },
                "id": "111111000000011709",
                "query_details": {
                  "system_query_id": null
                }
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "CONTACTID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 13,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "lookup",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": false,
              "operation_type": {
                "web_update": false,
                "api_create": true,
                "web_create": true,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Repeat",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [],
              "required": false,
              "display_label": "Recurring Activity",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000004172",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 2,
              "external": null,
              "api_name": "Recurring_Activity",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 123,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "RECURRING",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 14,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "RRULE",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": false,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Reminder",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [],
              "required": false,
              "display_label": "Remind At",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000004176",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 0,
              "external": null,
              "api_name": "Remind_At",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonarray",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 104,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "REMINDAT",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 15,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "multireminder",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Related To",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "add_to_other_layouts",
                "lookup_filter",
                "field_of_lookup"
              ],
              "required": false,
              "display_label": "What Id",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000004170",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "What_Id",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 4,
              "validation_rule": null,
              "modified_time": null,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {
                "display_label": "activities",
                "api_name": null,
                "module": {
                  "api_name": "se_module"
                },
                "id": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SEID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 17,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "lookup",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            }
          ],
          "properties": null
        },
        {
          "isSubformSection": true,
          "type": "used",
          "display_label": "Subform 1",
          "mode": "default_create",
          "sequence_number": 5,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": false,
            "reorder": true,
            "delete": true,
            "remove_field": true,
            "change_column_count": false
          },
          "tab_traversal": "left_to_right",
          "api_name": "Subform_1",
          "column_count": 1,
          "name": "Subform 1",
          "generated_type": "custom",
          "id": "111111000000217245",
          "fields": [
            {
              "associated_module": {
                "layout": {
                  "name": "Standard",
                  "id": "111111000000216917"
                },
                "module": "Subform_1",
                "id": "111111000000216916"
              },
              "webhook": false,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Subform 1",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": null,
              "required": false,
              "display_label": "Subform 1",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000217027",
              "created_time": null,
              "filterable": false,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": false,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Subform_1",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": true,
              "json_type": "jsonarray",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 500,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": true,
              "lookup": {},
              "address": null,
              "rollup_summary": {},
              "column_name": "LINKINGMXN1",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 1,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "subform",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            }
          ],
          "properties": {
            "reorder_rows": true,
            "bulk_addition": null,
            "tooltip": null,
            "maximum_rows": 25
          }
        }
      ],
      "display_label": "Standard",
      "show_business_card": true,
      "actions_allowed": {
        "edit": true,
        "rename": true,
        "clone": true,
        "downgrade": false,
        "delete": false,
        "deactivate": false,
        "set_layout_permissions": true
      },
      "modified_time": "2025-11-20T14:44:37+05:30",
      "api_name": "Standard__s",
      "name": "Standard",
      "modified_by": {
        "name": "Ajay Ajay",
        "id": "2047208000000456001"
      },
      "generated_type": "system",
      "id": "2047208000005744376",
      "total_profiles": 1,
      "status": "active"
    },
    {
      "has_more_profiles": false,
      "created_time": null,
      "convert_mapping": {
        "Invoices": {
          "display_label": "Standard",
          "name": "Standard",
          "id": "111111000000003680"
        }
      },
      "visible": true,
      "created_for": null,
      "profiles": [
        {
          "_default_assignment_view": {
            "name": "Standard",
            "id": "111111000000003674",
            "type": "layout"
          },
          "default": true,
          "name": "Administrator",
          "id": "111111000000000497",
          "_default_view": {
            "name": "Standard",
            "id": "111111000000003674",
            "type": "layout"
          }
        },
        {
          "_default_assignment_view": {
            "name": "Standard",
            "id": "111111000000003674",
            "type": "layout"
          },
          "default": true,
          "name": "Standard",
          "id": "111111000000000499",
          "_default_view": {
            "name": "Standard",
            "id": "111111000000003674",
            "type": "layout"
          }
        }
      ],
      "source": "crm",
      "created_by": null,
      "sections": [
        {
          "isSubformSection": false,
          "type": "used",
          "display_label": "Sales Order Information",
          "mode": "default_create",
          "sequence_number": 1,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": true,
            "reorder": true,
            "delete": true,
            "remove_field": true,
            "change_column_count": true
          },
          "tab_traversal": "left_to_right",
          "api_name": "Sales_Order_Information__s",
          "column_count": 2,
          "name": "Sales Order Information",
          "generated_type": "default",
          "id": "111111000000027958",
          "fields": [
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Sales Order Owner",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": true,
              "customizable_properties": [
                "field_of_lookup"
              ],
              "required": false,
              "display_label": "Sales Order Owner",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005648",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Owner",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 8,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SMOWNERID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 1,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "ownerlookup",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "SO Number",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": true,
              "customizable_properties": [
                "removal",
                "add_to_other_layouts"
              ],
              "required": false,
              "display_label": "SO Number",
              "read_only": true,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005622",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_only",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_only",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 1,
              "external": null,
              "api_name": "SO_Number",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 52,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SONUMBER",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 2,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "autonumber",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {
                "prefix": null,
                "start_number": null,
                "suffix": null
              },
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Subject",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [],
              "required": true,
              "display_label": "Subject",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005624",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Subject",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": true,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "quick_sequence_number": "1",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Subject"
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SALESORDERSUBJECT",
              "display_field": true,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 3,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 1,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {
                "starting_number_length": 1,
                "prefix": "",
                "start_number": 3,
                "suffix": ""
              },
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Deal Name",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "add_to_other_layouts",
                "lookup_filter",
                "field_of_lookup"
              ],
              "required": false,
              "display_label": "Potential Name",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005626",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Deal_Name",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 133,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {
                "display_label": "Sales Orders",
                "revalidate_filter_during_edit": false,
                "api_name": "SalesOrders",
                "module": {
                  "api_name": "Deals",
                  "crypt": false,
                  "id": "111111000000002658"
                },
                "id": "111111000000011823",
                "query_details": {
                  "system_query_id": null
                }
              },
              "convert_mapping": {
                "Invoices": "Deal_Name__s"
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "POTENTIALID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 4,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "lookup",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Customer No.",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Customer No",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005684",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Customer_No",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "CUSTOMERNUMBER",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 5,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Purchase Order",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Purchase Order",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005628",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Purchase_Order",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Purchase_Order"
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "PURCHASEORDER",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 6,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Quote Name",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "add_to_other_layouts",
                "lookup_filter",
                "field_of_lookup"
              ],
              "required": false,
              "display_label": "Quote Name",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005630",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Quote_Name",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 133,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {
                "display_label": "Sales Orders",
                "revalidate_filter_during_edit": false,
                "api_name": "SalesOrders",
                "module": {
                  "api_name": "Quotes",
                  "crypt": false,
                  "id": "111111000000002762"
                },
                "id": "111111000000026323",
                "query_details": {
                  "system_query_id": null
                }
              },
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "QUOTEID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 7,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "lookup",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Due Date",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Due Date",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005632",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Due_Date",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 24,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Due_Date"
              },
              "address": null,
              "rollup_summary": {},
              "length": 20,
              "column_name": "DUEDATE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 8,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "date",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Pending",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Pending",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005634",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Pending",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "PENDING",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 9,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Contact Name",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "add_to_other_layouts",
                "lookup_filter",
                "field_of_lookup"
              ],
              "required": false,
              "display_label": "Contact Name",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005636",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Contact_Name",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 133,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {
                "display_label": "Sales Orders",
                "revalidate_filter_during_edit": false,
                "api_name": "SalesOrders",
                "module": {
                  "api_name": "Contacts",
                  "crypt": false,
                  "id": "111111000000002654"
                },
                "id": "111111000000011745",
                "query_details": {
                  "system_query_id": null
                }
              },
              "convert_mapping": {
                "Invoices": "Contact_Name"
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "CONTACTID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 10,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "lookup",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Carrier",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "history_tracking",
                "display_value_alphabetically",
                "default_value",
                "option_add",
                "add_to_other_layouts",
                "color_code",
                "replace_values",
                "record_category",
                "add_record_category",
                "remove_record_category",
                "rename_record_category",
                "modify_record_category_type"
              ],
              "required": false,
              "display_label": "Carrier",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005638",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Carrier",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [
                {
                  "display_value": "FedEX",
                  "sequence_number": 1,
                  "reference_value": "FedEX",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "FedEX",
                  "id": "111111000000007836",
                  "type": "used"
                },
                {
                  "display_value": "UPS",
                  "sequence_number": 2,
                  "reference_value": "UPS",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "UPS",
                  "id": "111111000000007838",
                  "type": "used"
                },
                {
                  "display_value": "USPS",
                  "sequence_number": 3,
                  "reference_value": "USPS",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "USPS",
                  "id": "111111000000007840",
                  "type": "used"
                },
                {
                  "display_value": "DHL",
                  "sequence_number": 4,
                  "reference_value": "DHL",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "DHL",
                  "id": "111111000000007842",
                  "type": "used"
                },
                {
                  "display_value": "BlueDart",
                  "sequence_number": 5,
                  "reference_value": "BlueDart",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "BlueDart",
                  "id": "111111000000007844",
                  "type": "used"
                }
              ],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 2,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "CARRIER",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 11,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "picklist",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "blueprint_supported": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Excise Duty",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "max_length_digits",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "rounding_type",
                "maximum_decimal",
                "field_masking"
              ],
              "required": false,
              "display_label": "Excise Duty",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005640",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Excise_Duty",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 36,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {
                "rounding_option": "normal",
                "precision": 2
              },
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Excise_Duty"
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "EXCISEDUTY",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 12,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "currency",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": 2,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Sales Commission",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "max_length_digits",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "rounding_type",
                "maximum_decimal",
                "field_masking"
              ],
              "required": false,
              "display_label": "Sales Commission",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005642",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Sales_Commission",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 36,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {
                "rounding_option": "normal",
                "precision": 2
              },
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Sales_Commission"
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "SALESCOMMISSION",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 13,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "currency",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": 2,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Status",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "private_field",
                "tooltip",
                "hipaa_field",
                "history_tracking",
                "display_value_alphabetically",
                "default_value",
                "option_add",
                "add_to_other_layouts",
                "color_code",
                "replace_values"
              ],
              "required": false,
              "display_label": "Status",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005644",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Status",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [
                {
                  "display_value": "Created",
                  "sequence_number": 1,
                  "reference_value": "Created",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Created",
                  "id": "111111000000007846",
                  "type": "used"
                },
                {
                  "display_value": "Approved",
                  "sequence_number": 2,
                  "reference_value": "Approved",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Approved",
                  "id": "111111000000007848",
                  "type": "used"
                },
                {
                  "display_value": "Delivered",
                  "sequence_number": 3,
                  "reference_value": "Delivered",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Delivered",
                  "id": "111111000000007850",
                  "type": "used"
                },
                {
                  "display_value": "Cancelled",
                  "sequence_number": 4,
                  "reference_value": "Cancelled",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Cancelled",
                  "id": "111111000000007852",
                  "type": "used"
                }
              ],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 2,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "quick_sequence_number": "2",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Status"
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "STATUS",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 14,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "picklist",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "blueprint_supported": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Account Name",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "add_to_other_layouts",
                "lookup_filter",
                "field_of_lookup"
              ],
              "required": true,
              "display_label": "Account Name",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005646",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": true,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Account_Name",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 133,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "quick_sequence_number": "3",
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {
                "display_label": "Sales Orders",
                "revalidate_filter_during_edit": false,
                "api_name": "SalesOrders",
                "module": {
                  "api_name": "Accounts",
                  "crypt": false,
                  "id": "111111000000002656"
                },
                "id": "111111000000011664",
                "query_details": {
                  "system_query_id": null
                }
              },
              "convert_mapping": {
                "Invoices": "Account_Name"
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "ACCOUNTID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 15,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "lookup",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Created By",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "removal",
                "add_to_other_layouts"
              ],
              "required": false,
              "display_label": "Created By",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005650",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Created_By",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 20,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SMCREATORID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 16,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "ownerlookup",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Tag",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Tag",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005666",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Tag",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonarray",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 209,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 2000,
              "column_name": "TAGMODULEREFID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 16,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Modified By",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "removal",
                "add_to_other_layouts"
              ],
              "required": false,
              "display_label": "Modified By",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005652",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Modified_By",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "jsonobject",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 20,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "MODIFIEDBY",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 17,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "ownerlookup",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Created Time",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [],
              "required": false,
              "display_label": "Created Time",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005654",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Created_Time",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 200,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "CREATEDTIME",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 18,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "datetime",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Modified Time",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [],
              "required": false,
              "display_label": "Modified Time",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005656",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Modified_Time",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 200,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "MODIFIEDTIME",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 19,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "datetime",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Record Id",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": true,
              "customizable_properties": null,
              "required": false,
              "display_label": "Record Id",
              "read_only": true,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005676",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_only",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_only",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": false,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 17,
              "external": null,
              "api_name": "id",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 52,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 18,
              "column_name": "SALESORDERID",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 31,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "bigint",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": false,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Locked",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": true,
              "customizable_properties": null,
              "required": false,
              "display_label": "Locked",
              "read_only": true,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005678",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_only",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_only",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": false,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 0,
              "external": null,
              "api_name": "Locked__s",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "boolean",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 301,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 5,
              "column_name": "ISLOCKED",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": false,
              "sortable": true,
              "sequence_number": 32,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "boolean",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Last Activity Time",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fixed_position",
                "tooltip",
                "field_masking"
              ],
              "required": false,
              "display_label": "Last Activity Time",
              "read_only": true,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005680",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_only",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_only",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 8,
              "external": null,
              "api_name": "Last_Activity_Time",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 786,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "LASTACTIVITYTIME",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 33,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "datetime",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": true,
                "web_create": false,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Record Status",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": null,
              "required": false,
              "display_label": "Record Status",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005620",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": false,
                "edit": false,
                "quick_create": false,
                "create": false
              },
              "separator": false,
              "searchable": false,
              "history_tracking_enabled": false,
              "show_type": 17,
              "external": null,
              "api_name": "Record_Status__s",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [
                {
                  "display_value": "Available",
                  "sequence_number": 1,
                  "reference_value": "Available",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Available",
                  "id": "111111000000007830",
                  "type": "used"
                },
                {
                  "display_value": "Draft",
                  "sequence_number": 2,
                  "reference_value": "Draft",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Draft",
                  "id": "111111000000007832",
                  "type": "used"
                },
                {
                  "display_value": "Trash",
                  "sequence_number": 3,
                  "reference_value": "Trash",
                  "maps": [],
                  "colour_code": null,
                  "actual_value": "Trash",
                  "id": "111111000000007834",
                  "type": "used"
                }
              ],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 2,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 120,
              "column_name": "SE_PRESENCE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 42,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "picklist",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "blueprint_supported": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            }
          ],
          "properties": null
        },
        {
          "isSubformSection": false,
          "type": "used",
          "display_label": "Address Information",
          "mode": "default_create",
          "sequence_number": 2,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": true,
            "reorder": true,
            "delete": true,
            "remove_field": true,
            "change_column_count": true
          },
          "tab_traversal": "top_to_bottom",
          "api_name": "Address_Information__s",
          "column_count": 2,
          "name": "Address Information",
          "generated_type": "default",
          "id": "111111000000028053",
          "fields": [
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Billing Street",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Billing Street",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005686",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Billing_Street",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Billing_Street"
              },
              "address": null,
              "rollup_summary": {},
              "length": 250,
              "column_name": "BILLINGSTREET",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 1,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Shipping Street",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Shipping Street",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005688",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Shipping_Street",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Shipping_Street"
              },
              "address": null,
              "rollup_summary": {},
              "length": 250,
              "column_name": "SHIPPINGSTREET",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 2,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Billing City",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Billing City",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005690",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Billing_City",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Billing_City"
              },
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "BILLINGCITY",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 3,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Shipping City",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Shipping City",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005692",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Shipping_City",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Shipping_City"
              },
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "SHIPPINGCITY",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 4,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Billing State",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Billing State",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005694",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Billing_State",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Billing_State"
              },
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "BILLINGSTATE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 5,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Shipping State",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Shipping State",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005696",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Shipping_State",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Shipping_State"
              },
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "SHIPPINGSTATE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 6,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Billing Code",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Billing Code",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005698",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Billing_Code",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Billing_Code"
              },
              "address": null,
              "rollup_summary": {},
              "length": 30,
              "column_name": "BILLINGCODE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 7,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Shipping Code",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Shipping Code",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005700",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Shipping_Code",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Shipping_Code"
              },
              "address": null,
              "rollup_summary": {},
              "length": 30,
              "column_name": "SHIPPINGCODE",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 8,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Billing Country",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Billing Country",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005702",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Billing_Country",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Billing_Country"
              },
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "BILLINGCOUNTRY",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 9,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Shipping Country",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "unique",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "field_masking"
              ],
              "required": false,
              "display_label": "Shipping Country",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005704",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Shipping_Country",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 2,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Shipping_Country"
              },
              "address": null,
              "rollup_summary": {},
              "length": 100,
              "column_name": "SHIPPINGCOUNTRY",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 10,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            }
          ],
          "properties": null
        },
        {
          "isSubformSection": true,
          "type": "used",
          "display_label": "Ordered Items",
          "mode": "default_create",
          "sequence_number": 3,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": false,
            "reorder": true,
            "delete": false,
            "remove_field": true,
            "change_column_count": false
          },
          "tab_traversal": "left_to_right",
          "api_name": "Ordered_Items__s",
          "column_count": 1,
          "name": "Ordered Items",
          "generated_type": "default",
          "id": "111111000000028091",
          "fields": [
            {
              "associated_module": {
                "layout": {
                  "name": "Standard",
                  "id": "111111000000003724"
                },
                "module": "Ordered_Items",
                "id": "111111000000002768"
              },
              "webhook": false,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Ordered Items",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": null,
              "required": true,
              "display_label": "Ordered Items",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "111111000000005712",
              "created_time": null,
              "filterable": false,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": false,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Ordered_Items",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": true,
              "virtual_field": true,
              "json_type": "jsonarray",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 500,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Invoiced_Items"
              },
              "address": null,
              "rollup_summary": {},
              "column_name": "LINKINGMXN1",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 1,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "subform",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": {
                "module": "Ordered_Items",
                "id": "111111000000002768"
              },
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Sub Total",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "removal",
                "tooltip",
                "add_to_other_layouts",
                "maximum_decimal",
                "formula_expression",
                "assume_default",
                "dynamic_formula",
                "conditional_formula",
                "conditional_formula_expression"
              ],
              "required": false,
              "display_label": "Sub Total",
              "read_only": true,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005714",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Sub_Total",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 117,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Sub_Total"
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "SUBTOTAL",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 2,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "formula",
              "formula": {
                "return_type": "currency",
                "expression": "SUM(${OrderedItems.Net_Total})",
                "dynamic": false,
                "stop_compute_conditionally": false,
                "stop_compute_expression": null
              },
              "additional_column": null,
              "category": 2,
              "query_details": null,
              "decimal_place": 9,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": {
                "module": "Ordered_Items",
                "id": "111111000000002768"
              },
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Discount",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "max_length_digits",
                "removal",
                "tooltip",
                "rounding_type",
                "maximum_decimal",
                "field_masking"
              ],
              "required": false,
              "display_label": "Discount",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005716",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Discount",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 36,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {
                "rounding_option": "normal",
                "precision": 2
              },
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Discount"
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "DISCOUNT",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 3,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "currency",
              "formula": {
                "return_type": "boolean",
                "expression": "Contains(${Owner},${Last_Name})",
                "evaluation_order": 1,
                "dynamic": false,
                "stop_compute_conditionally": false,
                "assume_default": false,
                "stop_compute_expression": null
              },
              "additional_column": null,
              "category": 2,
              "decimal_place": 2,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": {
                "module": "Ordered_Items",
                "id": "111111000000002768"
              },
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Tax",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "max_length_digits",
                "removal",
                "tooltip",
                "rounding_type",
                "maximum_decimal",
                "field_masking"
              ],
              "required": false,
              "display_label": "Tax",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005718",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": {
                "show": false,
                "type": "org"
              },
              "api_name": "Tax",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 36,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {
                "rounding_option": "normal",
                "precision": 2
              },
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Tax"
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "TAX",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 4,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "currency",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": 2,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": {
                "module": "Ordered_Items",
                "id": "111111000000002768"
              },
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Adjustment",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "max_length_digits",
                "removal",
                "tooltip",
                "rounding_type",
                "maximum_decimal",
                "field_masking"
              ],
              "required": false,
              "display_label": "Adjustment",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005720",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Adjustment",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 36,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {
                "rounding_option": "normal",
                "precision": 2
              },
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Adjustment"
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "ADJUSTMENT",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 5,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "currency",
              "formula": {},
              "additional_column": null,
              "category": 2,
              "decimal_place": 2,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": {
                "module": "Subform1",
                "id": "4832675000000658658"
              },
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Aggregate Field 1",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fieldlabel",
                "removal",
                "deletion",
                "tooltip",
                "add_to_other_layouts",
                "maximum_decimal",
                "formula_expression",
                "number_separator",
                "assume_default",
                "dynamic_formula",
                "conditional_formula",
                "conditional_formula_expression"
              ],
              "required": false,
              "display_label": "Aggregate Field 1",
              "read_only": true,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "4832675000001313360",
              "created_time": "2026-01-13T10:14:29+05:30",
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "4832675000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "4832675000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": true,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Aggregate_Field_1",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "private": null,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 117,
              "validation_rule": null,
              "modified_time": "2026-01-13T10:14:29+05:30",
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": true,
              "lookup": {},
              "hipaa_compliance": null,
              "convert_mapping": {
                "Contacts": null,
                "Deals": null,
                "Accounts": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "LEADCF72",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 2,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "formula",
              "formula": {
                "return_type": "double",
                "expression": "SUM(${LinkingModule1.Formula_1})",
                "dynamic": false,
                "stop_compute_conditionally": false,
                "stop_compute_expression": null
              },
              "additional_column": null,
              "hipaa_compliance_enabled": false,
              "category": 0,
              "query_details": null,
              "decimal_place": 2,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": {
                "layout": {
                  "name": "Standard",
                  "id": "4832675000000658659"
                },
                "module": "Subform1",
                "id": "4832675000000658658"
              },
              "webhook": false,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Subform1",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": null,
              "required": false,
              "display_label": "Subform1",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": false,
              "multi_module_lookup": {},
              "id": "4832675000000658767",
              "created_time": null,
              "filterable": false,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "4832675000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "4832675000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": false,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Subform1",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "private": null,
              "virtual_field": true,
              "json_type": "jsonarray",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 500,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": true,
              "lookup": {},
              "hipaa_compliance": null,
              "convert_mapping": {
                "Contacts": null,
                "Deals": null,
                "Accounts": null
              },
              "address": null,
              "rollup_summary": {},
              "column_name": "LINKINGMXN1",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 3,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "subform",
              "formula": {},
              "additional_column": null,
              "hipaa_compliance_enabled": false,
              "category": 2,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": {
                "module": "Subform1",
                "id": "4832675000000658658"
              },
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Aggregate Field 2",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "fieldlabel",
                "removal",
                "deletion",
                "tooltip",
                "add_to_other_layouts",
                "maximum_decimal",
                "formula_expression",
                "number_separator",
                "assume_default",
                "dynamic_formula",
                "conditional_formula",
                "conditional_formula_expression"
              ],
              "required": false,
              "display_label": "Aggregate Field 2",
              "read_only": true,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "4832675000001313415",
              "created_time": "2026-01-13T10:14:55+05:30",
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "4832675000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "4832675000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": true,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Aggregate_Field_2",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "private": null,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 117,
              "validation_rule": null,
              "modified_time": "2026-01-13T10:14:55+05:30",
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": true,
              "lookup": {},
              "hipaa_compliance": null,
              "convert_mapping": {
                "Contacts": null,
                "Deals": null,
                "Accounts": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "LEADCF73",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 4,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "formula",
              "formula": {
                "return_type": "double",
                "expression": "SUM(${LinkingModule1.Number_1})",
                "dynamic": false,
                "stop_compute_conditionally": false,
                "stop_compute_expression": null
              },
              "additional_column": null,
              "hipaa_compliance_enabled": false,
              "category": 0,
              "query_details": {
                "query_id": 4832675000001314000,
                "criteria": {
                  "comparator": "equal",
                  "field": {
                    "api_name": "Pick_List_1",
                    "id": "4832675000000696400"
                  },
                  "type": "value",
                  "value": "Option 1"
                }
              },
              "decimal_place": 0,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": {
                "layout": {
                  "name": "Standard",
                  "id": "111111000000216917"
                },
                "module": "Subform_1",
                "id": "111111000000216916"
              },
              "webhook": true,
              "operation_type": {
                "web_update": false,
                "api_create": false,
                "web_create": false,
                "api_update": false
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Grand Total",
              "tooltip": {
                "name": "info_icon",
                "value": "Sample tool tip"
              },
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "removal",
                "tooltip",
                "maximum_decimal",
                "formula_expression",
                "assume_default"
              ],
              "required": false,
              "display_label": "Grand Total",
              "read_only": true,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005722",
              "created_time": null,
              "filterable": true,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Grand_Total",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "double",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 116,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": false
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Grand_Total"
              },
              "address": null,
              "rollup_summary": {},
              "length": 16,
              "column_name": "GRANDTOTAL",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 6,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "formula",
              "formula": {
                "return_type": "currency",
                "expression": "${Sub_Total}-${Discount}+${Tax}+${Adjustment}",
                "evaluation_order": 1,
                "dynamic": false,
                "stop_compute_conditionally": false,
                "assume_default": false,
                "stop_compute_expression": null
              },
              "additional_column": null,
              "category": 2,
              "decimal_place": 9,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Number 1",
              "tooltip": null,
              "display_format_properties": {
                "split": 8
              },
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "fieldlabel",
                "max_length_digits",
                "unique",
                "encrypted",
                "removal",
                "deletion",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "number_separator",
                "field_masking"
              ],
              "required": false,
              "display_label": "Number 1",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "4832675000000850773",
              "created_time": "2025-11-18T14:28:09+05:30",
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "4832675000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "4832675000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": true,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Number_1",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "private": null,
              "virtual_field": false,
              "json_type": "integer",
              "crypt": null,
              "range": {
                "from": 0,
                "to": 99
              },
              "created_source": "default",
              "display_type": -1,
              "ui_type": 32,
              "validation_rule": null,
              "modified_time": "2025-11-18T14:28:09+05:30",
              "public": false,
              "section_id": 1,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": true,
              "lookup": {},
              "hipaa_compliance": null,
              "convert_mapping": {
                "Contacts": null,
                "Deals": null,
                "Accounts": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 9,
              "column_name": "LEADCF51",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 5,
              "global_picklist": null,
              "display_format": "slider",
              "history_tracking": null,
              "data_type": "integer",
              "formula": {},
              "additional_column": null,
              "hipaa_compliance_enabled": false,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            }
          ],
          "properties": {
            "reorder_rows": true,
            "bulk_addition": null,
            "tooltip": null,
            "maximum_rows": 200
          }
        },
        {
          "isSubformSection": false,
          "type": "used",
          "display_label": "Terms and Conditions",
          "mode": "default_create",
          "sequence_number": 4,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": true,
            "reorder": true,
            "delete": true,
            "remove_field": true,
            "change_column_count": true
          },
          "tab_traversal": "top_to_bottom",
          "api_name": "Terms_and_Conditions__s",
          "column_count": 1,
          "name": "Terms and Conditions",
          "generated_type": "default",
          "id": "111111000000028081",
          "fields": [
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Terms and Conditions",
              "tooltip": null,
              "textarea": {
                "type": "large"
              },
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "tooltip",
                "default_value",
                "add_to_other_layouts"
              ],
              "required": false,
              "display_label": "Terms and Conditions",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005708",
              "created_time": null,
              "filterable": false,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Terms_and_Conditions",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 3,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 4,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {
                "display_label": "Related List Label 1",
                "revalidate_filter_during_edit": false,
                "api_name": "Related_List_Label_1",
                "module": {
                  "api_name": "Quotes",
                  "crypt": false,
                  "id": "4832675000000000169"
                },
                "id": "4832675000000850800",
                "query_details": {
                  "query_id": "4832675000000850792",
                  "criteria": {
                    "comparator": "not_equal",
                    "field": {
                      "api_name": "Contact_Name.Full_Name",
                      "id": "4832675000000000485"
                    },
                    "type": "value",
                    "value": "${EMPTY}"
                  },
                  "system_query_id": null
                }
              },
              "convert_mapping": {
                "Invoices": "Terms_and_Conditions"
              },
              "address": null,
              "rollup_summary": {},
              "length": 32000,
              "column_name": "TERMSANDCONDITIONS",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 8,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "textarea",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            }
          ],
          "properties": null
        },
        {
          "isSubformSection": false,
          "type": "used",
          "display_label": "Description Information",
          "mode": "default_create",
          "sequence_number": 5,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": true,
            "reorder": true,
            "delete": true,
            "remove_field": true,
            "change_column_count": true
          },
          "tab_traversal": "top_to_bottom",
          "api_name": "Description_Information__s",
          "column_count": 1,
          "name": "Description Information",
          "generated_type": "default",
          "id": "111111000000028086",
          "fields": [
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Description",
              "tooltip": null,
              "textarea": {
                "type": "large"
              },
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "removal",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts"
              ],
              "required": false,
              "display_label": "Description",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000005710",
              "created_time": null,
              "filterable": false,
              "visible": true,
              "mask_details": null,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Description",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 3,
              "validation_rule": null,
              "modified_time": null,
              "public": false,
              "section_id": 5,
              "email_parser": {
                "fields_update_supported": false,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": false,
              "lookup": {},
              "convert_mapping": {
                "Invoices": "Description"
              },
              "address": null,
              "rollup_summary": {},
              "length": 32000,
              "column_name": "DESCRIPTION",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": false,
              "sequence_number": 8,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "textarea",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": false,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Single Line 1",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "fieldlabel",
                "max_length_digits",
                "unique",
                "encrypted",
                "removal",
                "deletion",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "external_field",
                "field_masking"
              ],
              "required": false,
              "display_label": "Single Line 2",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "sharing_properties": {
                "scheduler_status": "completed",
                "share_permission": "full-access",
                "share_preference_enabled": true
              },
              "multi_module_lookup": {},
              "id": "4832675000001283738",
              "created_time": "2026-01-12T16:17:40+05:30",
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "4832675000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "4832675000000015975"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Single_Line_2",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "private": null,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": {
                "from": 0,
                "to": null
              },
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": "2026-01-12T16:18:01+05:30",
              "public": false,
              "section_id": 3,
              "static_values": [
                {
                  "sequence_number": 1,
                  "id": "3722469000001680088",
                  "value": "Option 1"
                },
                {
                  "sequence_number": 2,
                  "id": "3722469000001680090",
                  "value": "Option 2"
                },
                {
                  "sequence_number": 3,
                  "id": "3722469000001680092",
                  "value": "Option 3"
                }
              ],
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": true,
              "lookup": {},
              "convert_mapping": {},
              "address": null,
              "rollup_summary": {},
              "length": 255,
              "column_name": "CONTACTCF3",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 3,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": {
                "related_list_name": "Appointments Rescheduled History",
                "module": {
                  "api_name": "Appointments_Rescheduled_History__s",
                  "id": "4832675000000853664"
                },
                "duration_configured_field": null,
                "followed_fields": [
                  {
                    "api_name": "Rescheduled_By",
                    "id": "4832675000000851325"
                  },
                  {
                    "api_name": "Rescheduled_From",
                    "id": "4832675000000851317"
                  },
                  {
                    "api_name": "Rescheduled_To",
                    "id": "4832675000000851319"
                  },
                  {
                    "api_name": "Reschedule_Reason",
                    "id": "4832675000000851321"
                  },
                  {
                    "api_name": "Reschedule_Note",
                    "id": "4832675000000851323"
                  },
                  {
                    "api_name": "Rescheduled_Time",
                    "id": "4832675000000851327"
                  }
                ]
              },
              "data_type": "text",
              "formula": {},
              "static_field": false,
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Single Line 1",
              "tooltip": {
                "name": "static_text",
                "value": "Static tool tip"
              },
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "fieldlabel",
                "max_length_digits",
                "unique",
                "encrypted",
                "removal",
                "deletion",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "external_field",
                "field_masking"
              ],
              "required": false,
              "display_label": "Single Line 1",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000217664",
              "created_time": "2026-01-12T10:14:54+00:00",
              "filterable": true,
              "visible": true,
              "mask_details": {
                "complete_mask": true,
                "profiles": [
                  {
                    "name": "Administrator",
                    "id": "111111000000000497"
                  }
                ]
              },
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Single_Line_1",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": "2026-01-12T10:53:22+00:00",
              "public": false,
              "section_id": 3,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": true,
              "lookup": {},
              "address": null,
              "hipaa_compliance": null,
              "rollup_summary": {},
              "length": 255,
              "column_name": "ACCOUNTCF1",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 2,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            },
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Single Line 2",
              "tooltip": null,
              "display_format_properties": {
                "split": 8
              },
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "fieldlabel",
                "max_length_digits",
                "unique",
                "encrypted",
                "removal",
                "deletion",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "external_field",
                "field_masking"
              ],
              "required": false,
              "display_label": "Single Line 2",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "multi_module_lookup": {},
              "id": "111111000000217727",
              "created_time": "2026-01-12T10:54:19+00:00",
              "filterable": true,
              "visible": true,
              "mask_details": {
                "show_first": 3,
                "complete_mask": false,
                "show_last": 1,
                "profiles": [
                  {
                    "name": "Administrator",
                    "id": "111111000000000497"
                  }
                ]
              },
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "111111000000000497"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "111111000000000499"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Single_Line_2",
              "parent_field": {
                "api_name": "Address_1_Coordinates",
                "name": "Address 1 - Coordinates",
                "id": "4832675000000710334"
              },
              "unique": {
                "case_sensitive": false
              },
              "enable_colour_code": false,
              "child_fields": [
                {
                  "sequence_number": 1,
                  "field": {
                    "api_name": "Address_1_Coordinates_Latitude",
                    "name": "Address 1 - Latitude",
                    "id": "4832675000000710341"
                  }
                },
                {
                  "sequence_number": 2,
                  "field": {
                    "api_name": "Address_1_Coordinates_Longitude",
                    "name": "Address 1 - Longitude",
                    "id": "4832675000000710342"
                  }
                }
              ],
              "pick_list_values": [
                {
                  "display_value": "-None-",
                  "sequence_number": 1,
                  "reference_value": "-None-",
                  "maps": [
                    {
                      "api_name": "Pick_List_2",
                      "id": "4832675000001313017",
                      "pick_list_values": [
                        {
                          "display_value": "-None-",
                          "colour_code": null,
                          "actual_value": "-None-",
                          "id": "4832675000001313021"
                        }
                      ]
                    }
                  ],
                  "colour_code": null,
                  "actual_value": "-None-",
                  "id": "4832675000001312990",
                  "type": "used"
                },
                {
                  "display_value": "Option 1",
                  "sequence_number": 2,
                  "reference_value": "Option 1",
                  "maps": [
                    {
                      "api_name": "Pick_List_2",
                      "id": "4832675000001313017",
                      "pick_list_values": [
                        {
                          "display_value": "Option 1",
                          "colour_code": "#c9651a",
                          "actual_value": "Option 1",
                          "id": "4832675000001313016"
                        }
                      ]
                    }
                  ],
                  "colour_code": "#f6c1ff",
                  "actual_value": "Option 1",
                  "id": "4832675000001312983",
                  "type": "used"
                },
                {
                  "display_value": "Qualification",
                  "sequence_number": 1,
                  "deal_category": "Open",
                  "reference_value": "Qualification",
                  "maps": [],
                  "colour_code": "#ffc6c6",
                  "probability": 10,
                  "forecast_category": {
                    "name": "Pipeline",
                    "id": "4832675000000007092"
                  },
                  "actual_value": "Qualification",
                  "id": "4832675000000007104",
                  "forecast_type": "Open",
                  "type": "used"
                }
              ],
              "system_mandatory": false,
              "private": {
                "restricted": false,
                "type": "High",
                "export": false
              },
              "virtual_field": false,
              "json_type": "string",
              "crypt": {
                "mode": "encryption",
                "encrypt_case": null,
                "status": 1
              },
              "range": {
                "from": 0,
                "to": 99
              },
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": {
                "id": "4832675000001313074"
              },
              "modified_time": "2026-01-12T10:54:19+00:00",
              "public": false,
              "section_id": 3,
              "quick_sequence_number": "10",
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {
                "rounding_option": "round_off",
                "precision": 0
              },
              "custom_field": true,
              "lookup": {
                "display_label": "Related List Label 1",
                "revalidate_filter_during_edit": false,
                "api_name": "Related_List_Label_1",
                "module": {
                  "api_name": "Accounts",
                  "crypt": false,
                  "id": "4832675000000000127"
                },
                "id": "4832675000000849966",
                "query_details": {
                  "system_query_id": null
                }
              },
              "hipaa_compliance": {
                "restricted_in_export": false,
                "restricted": false
              },
              "convert_mapping": {
                "Contacts": "Title",
                "Deals": null,
                "Accounts": "Phone"
              },
              "address": {
                "type": "city"
              },
              "rollup_summary": {
                "return_type": "longinteger",
                "expression": {
                  "function_parameters": [
                    {
                      "api_name": "Call_Duration_in_seconds"
                    }
                  ],
                  "criteria": null,
                  "function": "SUM"
                },
                "based_on_module": {
                  "api_name": "Calls",
                  "id": "4832675000000017015"
                },
                "related_list": null,
                "rollup_based_on": "module"
              },
              "length": 255,
              "column_name": "ACCOUNTCF2",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": "Option 4",
              "sortable": true,
              "sequence_number": 3,
              "global_picklist": {
                "api_name": "Source",
                "id": "4832675000000491019"
              },
              "display_format": "slider",
              "history_tracking": {
                "related_list_name": "Globe History",
                "module": {
                  "api_name": "Globe_History",
                  "id": "4832675000000699487"
                },
                "duration_configured_field": {
                  "api_name": "Duration_Days",
                  "id": "4832675000000699823"
                },
                "duration_configuration": "days",
                "followed_fields": [
                  {
                    "api_name": "Mobile",
                    "id": "4832675000000000569"
                  },
                  {
                    "api_name": "Lead_Source",
                    "id": "4832675000000000573"
                  }
                ]
              },
              "data_type": "text",
              "formula": {
                "return_type": "text",
                "expression": "Substring(${Lead_Source},2,5)",
                "evaluation_order": 1,
                "dynamic": false,
                "stop_compute_conditionally": false,
                "assume_default": false,
                "stop_compute_expression": null
              },
              "additional_column": "LEADTF1",
              "hipaa_compliance_enabled": false,
              "category": 0,
              "decimal_place": 9,
              "mass_update": true,
              "blueprint_supported": false,
              "multiselectlookup": {
                "linking_details": {
                  "module": {
                    "visibility": 2,
                    "plural_label": "Leads X Contacts",
                    "api_name": "Leads_X_Contacts",
                    "id": "4832675000000696452"
                  },
                  "lookup_field": {
                    "api_name": "MXNContact",
                    "field_label": "MXNContact",
                    "id": "4832675000000696494"
                  },
                  "connected_lookup_field": {
                    "api_name": "MultiModuleLookup",
                    "field_label": "MultiModuleLookup",
                    "id": "4832675000000696496"
                  }
                },
                "connected_details": {
                  "field": {
                    "api_name": "MXNContact",
                    "field_label": "MXNContact",
                    "id": "4832675000000696488"
                  },
                  "module": {
                    "plural_label": "Contacts",
                    "api_name": "Contacts",
                    "id": "4832675000000000129"
                  },
                  "layouts": [
                    {
                      "api_name": "Standard__s",
                      "id": "4832675000000095059"
                    },
                    {
                      "api_name": "Custom_Layout_1",
                      "id": "4832675000001280303"
                    }
                  ]
                },
                "related_list": {
                  "display_label": "Contacts",
                  "api_name": "Contacts2",
                  "id": "4832675000000696587"
                }
              },
              "auto_number": {
                "starting_number_length": 1,
                "prefix": "D",
                "start_number": 1,
                "suffix": "P"
              },
              "textarea": {
                "type": "large"
              },
              "element_type": "field"
            }
          ],
          "properties": null
        },
        {
          "isSubformSection": false,
          "parent_section": null,
          "type": "used",
          "display_label": "New Section 1",
          "mode": "default_create",
          "sequence_number": 5,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": true,
            "reorder": true,
            "delete": true,
            "remove_field": true,
            "change_column_count": true
          },
          "tab_traversal": "left_to_right",
          "api_name": "New_Section_1",
          "column_count": 2,
          "is_parent_section": false,
          "name": "New Section 1",
          "generated_type": "custom",
          "id": "3722469000001636090",
          "fields": [
            {
              "associated_module": null,
              "webhook": true,
              "operation_type": {
                "web_update": true,
                "api_create": true,
                "web_create": true,
                "api_update": true
              },
              "colour_code_enabled_by_system": false,
              "field_label": "Single Line 2 renamed",
              "tooltip": null,
              "display_format_properties": null,
              "type": "used",
              "field_read_only": false,
              "customizable_properties": [
                "mandatory",
                "fieldlabel",
                "max_length_digits",
                "unique",
                "encrypted",
                "removal",
                "deletion",
                "private_field",
                "tooltip",
                "hipaa_field",
                "add_to_other_layouts",
                "external_field",
                "field_masking"
              ],
              "required": false,
              "display_label": "Single Line 2",
              "read_only": false,
              "association_details": null,
              "businesscard_supported": true,
              "subform_properties": {
                "custom_width": 265,
                "pinned_column": false
              },
              "multi_module_lookup": {},
              "id": "3722469000001341019",
              "created_time": "2025-11-25T09:59:10+05:30",
              "filterable": true,
              "visible": true,
              "refer_from_field": null,
              "profiles": [
                {
                  "permission_type": "read_write",
                  "name": "Administrator",
                  "id": "3722469000000015972"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard",
                  "id": "3722469000000015975"
                },
                {
                  "permission_type": "read_write",
                  "name": "Admin Clone 1",
                  "id": "3722469000001196003"
                },
                {
                  "permission_type": "read_write",
                  "name": "Admin Clone 2",
                  "id": "3722469000001196033"
                },
                {
                  "permission_type": "read_write",
                  "name": "Standard Clone 1",
                  "id": "3722469000001196061"
                }
              ],
              "view_type": {
                "view": true,
                "edit": true,
                "quick_create": false,
                "create": true
              },
              "separator": false,
              "searchable": true,
              "history_tracking_enabled": false,
              "show_type": 7,
              "external": null,
              "api_name": "Single_Line_2",
              "parent_field": null,
              "unique": {},
              "enable_colour_code": false,
              "child_fields": null,
              "pick_list_values": [],
              "system_mandatory": false,
              "virtual_field": false,
              "json_type": "string",
              "crypt": null,
              "range": null,
              "created_source": "default",
              "display_type": -1,
              "ui_type": 1,
              "validation_rule": null,
              "modified_time": "2025-11-25T09:59:27+05:30",
              "public": false,
              "section_id": 6,
              "email_parser": {
                "fields_update_supported": true,
                "record_operations_supported": true
              },
              "currency": {},
              "custom_field": true,
              "lookup": {},
              "convert_mapping": {
                "Contacts": null,
                "Deals": null,
                "Accounts": null
              },
              "address": null,
              "rollup_summary": {},
              "length": 255,
              "column_name": "LEADCF3",
              "display_field": false,
              "pick_list_values_sorted_lexically": false,
              "default_value": null,
              "sortable": true,
              "sequence_number": 1,
              "global_picklist": null,
              "display_format": null,
              "history_tracking": null,
              "data_type": "text",
              "formula": {},
              "additional_column": null,
              "category": 0,
              "decimal_place": null,
              "mass_update": true,
              "multiselectlookup": {},
              "auto_number": {},
              "element_type": "field"
            }
          ],
          "properties": {
            "preference": [
              {
                "comparator": "not_equal",
                "field": {
                  "api_name": "Quoted_Items",
                  "id": "4480493000000272734"
                },
                "type": "value",
                "value": "${EMPTY}"
              }
            ]
          }
        }
      ],
      "display_label": "Standard",
      "show_business_card": true,
      "actions_allowed": {
        "edit": true,
        "rename": true,
        "clone": true,
        "downgrade": false,
        "delete": false,
        "deactivate": false,
        "set_layout_permissions": true
      },
      "modified_time": null,
      "api_name": "Standard__s",
      "name": "Standard",
      "modified_by": null,
      "generated_type": "system",
      "id": "111111000000003674",
      "status": "active"
    },
    {
      "has_more_profiles": false,
      "created_time": null,
      "visible": true,
      "created_for": null,
      "profiles": [
        {
          "_default_assignment_view": {
            "name": "Standard",
            "id": "111111000000003690",
            "type": "layout"
          },
          "default": true,
          "name": "Administrator",
          "id": "111111000000000497",
          "_default_view": {
            "name": "Standard",
            "id": "111111000000003690",
            "type": "layout"
          }
        }
      ],
      "source": "crm",
      "created_by": null,
      "sections": [],
      "display_label": "Standard",
      "show_business_card": true,
      "actions_allowed": {
        "edit": true,
        "rename": false,
        "clone": false,
        "downgrade": false,
        "delete": false,
        "deactivate": false,
        "set_layout_permissions": true
      },
      "modified_time": null,
      "api_name": "Standard__s",
      "name": "Standard",
      "modified_by": null,
      "generated_type": "system",
      "id": "111111000000003690",
      "status": "active"
    }
  ]
}
```

### Status `200` — `application/json` — WithIncludeAndFieldsFilter

Layout response with include and fields query params

```json
{
  "layouts": [
    {
      "has_more_profiles": false,
      "created_time": "2024-10-23T21:02:52+05:30",
      "visible": true,
      "created_for": null,
      "profiles": [
        {
          "_default_assignment_view": {
            "name": "Standard",
            "id": "4150868000000095005",
            "type": "layout"
          },
          "default": true,
          "name": "Administrator",
          "id": "4150868000000015972",
          "_default_view": {
            "name": "Standard",
            "id": "4150868000000095005",
            "type": "layout"
          },
          "type": "normal_profile"
        },
        {
          "_default_assignment_view": {
            "name": "Standard",
            "id": "4150868000000095005",
            "type": "layout"
          },
          "default": true,
          "name": "Standard",
          "id": "4150868000000015975",
          "_default_view": {
            "name": "Standard",
            "id": "4150868000000095005",
            "type": "layout"
          },
          "type": "normal_profile"
        }
      ],
      "source": "crm",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "4150868000000419001"
      },
      "sections": [
        {
          "isSubformSection": false,
          "parent_section": null,
          "type": "used",
          "display_label": "Lead Information",
          "mode": "all",
          "sequence_number": 1,
          "actions_allowed": {
            "add_field": true,
            "rename": true,
            "change_tab_traversal": true,
            "reorder": true,
            "delete": false,
            "remove_field": true,
            "change_column_count": true
          },
          "tab_traversal": "left_to_right",
          "api_name": "LeadInformation1",
          "column_count": 2,
          "is_parent_section": false,
          "name": "Lead Information",
          "generated_type": "default",
          "id": "4150868000000095025",
          "fields": [],
          "properties": null
        }
      ],
      "display_label": "Standard",
      "show_business_card": true,
      "actions_allowed": {
        "edit": true,
        "rename": true,
        "clone": false,
        "downgrade": false,
        "delete": false,
        "deactivate": false,
        "set_layout_permissions": true
      },
      "modified_time": "2025-07-01T14:07:10+05:30",
      "api_name": "Standard",
      "name": "Standard",
      "modified_by": {
        "name": "Patricia Boyle",
        "id": "4150868000000419001"
      },
      "generated_type": "system",
      "id": "4150868000000095005",
      "total_profiles": 3,
      "status": "active"
    }
  ]
}
```

### Status `400` — `application/json` — MissingModuleParam

Missing required module parameter

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module name provided

```json
{
  "code": "INVALID_MODULE",
  "details": {},
  "message": "the module name given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — PatternNotMatched

Invalid mode parameter value

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "details": {
    "param_name": "mode"
  },
  "message": "Please check whether the input values are correct",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Invalid HTTP method used

```json
{
  "code": "INVALID_REQUEST_METHOD",
  "details": {},
  "message": "The http request method type is not a valid one",
  "status": "error"
}
```

### Status `401` — `application/json` — AuthenticationFailure

Authentication failure

```json
{
  "code": "AUTHENTICATION_FAILURE",
  "details": {},
  "message": "Authentication failed",
  "status": "error"
}
```

### Status `401` — `application/json` — OAuthScopeMismatch

OAuth scope mismatch

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "details": {},
  "message": "Invalid oauth scope to access this URL",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error"
}
```

### Status `500` — `application/json` — InternalError

Server error

```json
{
  "code": "INTERNAL_ERROR",
  "details": {},
  "message": "Internal Server Error",
  "status": "error"
}
```
