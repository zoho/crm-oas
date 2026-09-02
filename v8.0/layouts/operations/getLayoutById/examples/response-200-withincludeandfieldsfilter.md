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
