Successful retrieval of a kiosk's first screen state, elements, and field metadata

```json
{
  "kiosk_preview": [
    {
      "executable_info": {
        "state": {
          "name": "Screen 1",
          "id": "2296900000011317679"
        },
        "transitions": [
          {
            "prop_name": "primary",
            "is_connected_end": true,
            "name": "Done",
            "id": "2296900000011317677"
          }
        ]
      },
      "data": {
        "GetRecords_1": [
          {
            "name": "First Name d Last Name d",
            "id": "2296900000000774844"
          }
        ]
      },
      "elements": [
        {
          "get_record": {
            "selection_details": {
              "selection_type": "mandate",
              "result_type": "multiple",
              "limit": 10
            },
            "open_record": true,
            "api_name": "GetRecords_1",
            "module": {
              "display_label": "Leads",
              "api_name": "Leads",
              "name": "Leads",
              "id": "2296900000010857048"
            },
            "name": "GetRecords 1",
            "id": "2296900000011317646",
            "selected_fields": [
              {
                "ui_type": 1,
                "api_name": "Company",
                "field_label": "Company",
                "data_type": "text",
                "id": "2296900000010863602"
              },
              {
                "ui_type": 27,
                "api_name": "First_Name",
                "field_label": "First Name",
                "data_type": "text",
                "id": "2296900000010863603"
              },
              {
                "ui_type": 8,
                "api_name": "Owner",
                "field_label": "Lead Owner",
                "data_type": "ownerlookup",
                "id": "2296900000010863601"
              }
            ]
          },
          "type": "get_records",
          "value": null,
          "get_record_data": [
            {
              "First_Name": "First Name d",
              "Company": "dsdsdsds d",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000000774844"
            },
            {
              "First_Name": null,
              "Company": "crrmtest",
              "Owner": {
                "name": "Test Kiosk Last Name",
                "id": "2296900000000727010"
              },
              "id": "2296900000007352025"
            },
            {
              "First_Name": null,
              "Company": "crrmtest check",
              "Owner": {
                "name": "Test Kiosk Last Name",
                "id": "2296900000000727010"
              },
              "id": "2296900000007341123"
            },
            {
              "First_Name": null,
              "Company": "crrmtest",
              "Owner": {
                "name": "Test Kiosk Last Name",
                "id": "2296900000000727010"
              },
              "id": "2296900000007233167"
            },
            {
              "First_Name": null,
              "Company": "crrmtest",
              "Owner": {
                "name": "Test Kiosk Last Name",
                "id": "2296900000000727010"
              },
              "id": "2296900000004525001"
            },
            {
              "First_Name": null,
              "Company": "crrmtest",
              "Owner": {
                "name": "Test Kiosk Last Name",
                "id": "2296900000000727010"
              },
              "id": "2296900000007233079"
            },
            {
              "First_Name": null,
              "Company": "crrmtest",
              "Owner": {
                "name": "Test Kiosk Last Name",
                "id": "2296900000000727010"
              },
              "id": "2296900000007233101"
            },
            {
              "First_Name": null,
              "Company": "crrmtest",
              "Owner": {
                "name": "Test Kiosk Last Name",
                "id": "2296900000000727010"
              },
              "id": "2296900000007233123"
            },
            {
              "First_Name": null,
              "Company": "crrmtest",
              "Owner": {
                "name": "Test Kiosk Last Name",
                "id": "2296900000000727010"
              },
              "id": "2296900000007233145"
            },
            {
              "First_Name": null,
              "Company": "cc",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000002844006"
            },
            {
              "First_Name": null,
              "Company": "cc",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000002598025"
            },
            {
              "First_Name": null,
              "Company": "cc check app",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000002835242"
            },
            {
              "First_Name": null,
              "Company": "cc check app",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000002835161"
            },
            {
              "First_Name": "34",
              "Company": "df",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000001977122"
            },
            {
              "First_Name": null,
              "Company": "Salem",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000001227214"
            },
            {
              "First_Name": "l",
              "Company": "Salem",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000001227072"
            },
            {
              "First_Name": null,
              "Company": "Salem",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000001227017"
            },
            {
              "First_Name": null,
              "Company": "Salem",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000001186001"
            },
            {
              "First_Name": null,
              "Company": "Salem",
              "Owner": {
                "name": "Dylan Vasquez",
                "id": "2296900000000471001"
              },
              "id": "2296900000000855037"
            }
          ],
          "more_records": false
        },
        {
          "field": {
            "allow_multiple_upload": null,
            "field_label": "Single Line 1",
            "length": 255,
            "tooltip": null,
            "_merge_field": "${ProcessFlow5.2296900000011317713.2296900000010864732}",
            "number_separator": false,
            "required": false,
            "ui_type": 1,
            "read_only": false,
            "api_name": "Screen_1_Single_Line_1",
            "data_type": "text",
            "currency": null,
            "id": "2296900000011317738",
            "_pick_list_type": null,
            "decimal_place": null,
            "pick_list_values": null
          },
          "type": "field",
          "value": "2296900000008663001"
        }
      ],
      "width": "670px",
      "kiosk": {
        "name": "new",
        "id": "2296900000011316567"
      },
      "title": "Screen 1",
      "previous_states": [
        {
          "name": "Start",
          "id": "2296900000011317633",
          "type": "start_state"
        },
        {
          "name": "GetRecords 1",
          "id": "2296900000011317668",
          "type": "get_records"
        }
      ],
      "button_align": "right_to_left"
    }
  ]
}
```
