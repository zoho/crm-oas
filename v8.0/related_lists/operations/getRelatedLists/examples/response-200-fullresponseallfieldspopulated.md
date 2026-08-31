Related list with all optional fields populated

```json
{
  "related_lists": [
    {
      "id": "4150868000000091023",
      "sequence_number": "1",
      "display_label": "Contacts",
      "api_name": "Contacts",
      "module": {
        "api_name": "Contacts",
        "id": "4150868000000002175"
      },
      "name": "Contacts",
      "action": "add_existing",
      "href": "Contacts/{ENTITYID}/Contacts",
      "type": "default",
      "connectedlookupApiName": "Account_Name",
      "customize_sort": true,
      "customize_fields": true,
      "customize_display_label": true,
      "status": "visible",
      "visibility": 1,
      "personality_name": "contacts_personality",
      "record_operations": {
        "edit": true,
        "create": true,
        "bulk_edit": false,
        "delete": true,
        "disassociate": true,
        "assign": false
      },
      "connectedmodule": "Accounts",
      "linkingmodule": "Contacts_X_Accounts",
      "parent_related_lists": [
        {
          "api_name": "Deals",
          "id": "4150868000000091050"
        }
      ],
      "_layout_specific_properties": [
        {
          "sequence_number": "2",
          "status": "visible",
          "layout": {
            "name": "Standard",
            "id": "4150868000000091100"
          }
        }
      ]
    }
  ]
}
```
