Successful response with action and get_records kiosk states

```json
{
  "states": [
    {
      "associated_fields": null,
      "name": "Action 117",
      "id": "4676645000000888060",
      "type": "action",
      "transitions": [
        {
          "name": "Action 117",
          "id": "4676645000000888061"
        }
      ]
    },
    {
      "associated_fields": [],
      "name": "GetRecords 131",
      "id": "4676645000000888425",
      "type": "get_records",
      "transitions": [
        {
          "name": "GetRecords 131",
          "id": "4676645000000888426"
        }
      ]
    },
    {
      "associated_fields": null,
      "name": "Decision 21",
      "id": "4676645000000887142",
      "type": "decision",
      "transitions": [
        {
          "name": "Path 1",
          "id": "4676645000000887137"
        },
        {
          "name": "Default",
          "id": "4676645000000887139"
        }
      ]
    },
    {
      "associated_fields": [
        {
          "api_name": "Pick_List_1",
          "id": "4676645000000877779"
        },
        {
          "api_name": "Query_1",
          "id": "4676645000000885198"
        },
        {
          "api_name": "GetRecords_1",
          "id": "4676645000000885247"
        },
        {
          "api_name": "Single_Line_1",
          "id": "4676645000000885268"
        },
        {
          "api_name": "Multi_Line_1",
          "id": "4676645000000885283"
        },
        {
          "api_name": "Phone_1",
          "id": "4676645000000885298"
        },
        {
          "api_name": "Number_1",
          "id": "4676645000000885313"
        },
        {
          "api_name": "Currency_1",
          "id": "4676645000000885328"
        },
        {
          "api_name": "URL_1",
          "id": "4676645000000885343"
        },
        {
          "api_name": "Date_Time_1",
          "id": "4676645000000885358"
        },
        {
          "api_name": "Email_1",
          "id": "4676645000000885373"
        },
        {
          "api_name": "Checkbox_1",
          "id": "4676645000000885388"
        },
        {
          "api_name": "GetRecords_1",
          "id": "4676645000000885247"
        }
      ],
      "name": "Screen 1",
      "details": {
        "screen_details": {
          "width": "670px",
          "title": "Screen 1",
          "button_align": "right_to_left"
        }
      },
      "id": "4676645000000877750",
      "type": "screen",
      "transitions": [
        {
          "name": "Done",
          "id": "4676645000000877748"
        }
      ]
    }
  ]
}
```
