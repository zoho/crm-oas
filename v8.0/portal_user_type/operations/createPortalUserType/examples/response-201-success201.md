Portal user type created successfully (201)

```json
{
  "user_type": [
    {
      "default": false,
      "personality_module": {
        "plural_label": "Contacts",
        "api_name": "Contacts",
        "id": "111113000000002666"
      },
      "name": "Client Portal V8",
      "active": true,
      "invitation_field": {
        "api_name": "Email",
        "id": "111113000000004612"
      },
      "id": "111113000000168122",
      "modules": [
        {
          "plural_label": "Contacts",
          "shared_type": "private",
          "api_name": "Contacts",
          "permissions": {
            "view": true,
            "edit": true,
            "edit_shared_records": false,
            "create": true,
            "delete": true
          },
          "id": "111113000000002666",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Last_Name",
              "id": "111113000000004604"
            },
            {
              "read_only": false,
              "api_name": "Full_Name",
              "id": "111113000000004606"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000004660"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000004662"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000004668"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000004694"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000004696"
            },
            {
              "read_only": false,
              "api_name": "Contact_X_CM01",
              "id": "111113000000131043"
            },
            {
              "read_only": false,
              "api_name": "Last_Enriched_Time__s",
              "id": "111113000000006734"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003678",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003678",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000070019",
            "type": "canvas_view"
          }
        },
        {
          "plural_label": "Products",
          "shared_type": "public",
          "api_name": "Products",
          "permissions": {
            "view": true
          },
          "id": "111113000000002768",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Product_Name",
              "id": "111113000000005278"
            },
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000005308"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000005310"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000005312"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000005332"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000005326"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000003684",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000003684",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000053489",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Custom Module",
          "shared_type": "private",
          "api_name": "Custom_Module",
          "permissions": {
            "view": true,
            "edit": false,
            "edit_shared_records": false,
            "create": false,
            "delete": false
          },
          "id": "111113000000125002",
          "filters": [
            {
              "display_label": "Lookup 1",
              "api_name": "Lookup_1",
              "id": "111113000000127669"
            }
          ],
          "fields": [
            {
              "read_only": false,
              "api_name": "Currency",
              "id": "111113000000125065"
            },
            {
              "read_only": true,
              "api_name": "Exchange_Rate",
              "id": "111113000000125067"
            },
            {
              "read_only": false,
              "api_name": "Layout",
              "id": "111113000000125071"
            },
            {
              "read_only": true,
              "api_name": "Locked__s",
              "id": "111113000000125093"
            },
            {
              "read_only": true,
              "api_name": "Change_Log_Time__s",
              "id": "111113000000125111"
            },
            {
              "read_only": false,
              "api_name": "Name",
              "id": "111113000000125047"
            },
            {
              "read_only": false,
              "api_name": "Lookup_1",
              "id": "111113000000127669"
            },
            {
              "read_only": false,
              "api_name": "Multi_Select_Lookup_1",
              "id": "111113000000131001"
            }
          ],
          "layouts": [
            {
              "display_label": "Standard",
              "name": "Standard",
              "id": "111113000000125001",
              "_default_view": {
                "display_label": "Standard",
                "name": "Standard",
                "id": "111113000000125001",
                "type": "layout"
              }
            }
          ],
          "views": {
            "id": "111113000000125014",
            "type": "custom_view"
          }
        },
        {
          "plural_label": "Notes",
          "shared_type": "private",
          "api_name": "Notes",
          "permissions": {
            "view": true,
            "delete_attachment": false,
            "edit": false,
            "create": false,
            "create_attachment": false,
            "delete": false
          },
          "id": "111113000000002694",
          "filters": null,
          "fields": [
            {
              "read_only": false,
              "api_name": "Owner",
              "id": "111113000000004322"
            },
            {
              "read_only": false,
              "api_name": "Note_Title",
              "id": "111113000000004324"
            },
            {
              "read_only": false,
              "api_name": "Note_Content",
              "id": "111113000000004326"
            },
            {
              "read_only": false,
              "api_name": "Parent_Id",
              "id": "111113000000004328"
            },
            {
              "read_only": false,
              "api_name": "Created_By",
              "id": "111113000000004330"
            },
            {
              "read_only": false,
              "api_name": "Modified_By",
              "id": "111113000000004332"
            },
            {
              "read_only": false,
              "api_name": "Created_Time",
              "id": "111113000000004334"
            },
            {
              "read_only": false,
              "api_name": "Modified_Time",
              "id": "111113000000004336"
            },
            {
              "read_only": false,
              "api_name": "id",
              "id": "111113000000004338"
            },
            {
              "read_only": false,
              "api_name": "Associated_Id__s",
              "id": "111113000000004340"
            },
            {
              "read_only": false,
              "api_name": "Record_Status__s",
              "id": "111113000000004342"
            }
          ],
          "layouts": null,
          "views": null
        }
      ]
    }
  ]
}
```
