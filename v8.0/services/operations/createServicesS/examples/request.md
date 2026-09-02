### `application/json` — SamplePostRequest

Successful creation of a service with specific-day availability and job-sheet configuration

```json
{
  "data": [
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Available_Till": null,
      "Available_From": null,
      "Location": "Client Address",
      "Service_Name": "firstService",
      "Duration": 60,
      "Availability_Type": "Every Business Days",
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Price": 434,
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Available_Till": "2026-01-16",
      "Available_From": "2026-01-10",
      "Availability_Type": "Specific Date Range",
      "Location": "Business Address and Client Address",
      "Service_Name": "secondService",
      "Duration": 30,
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Price": 343,
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Available_Till": null,
      "Available_From": null,
      "Location": "Client Address",
      "Service_Name": "thirdService",
      "Duration": 30,
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Availability_Type": "Specific Date(s)",
      "Available_Dates": [
        "2026-01-13",
        "2026-01-14",
        "2026-01-15"
      ],
      "Available_Timings": [
        {
          "From": "01:00",
          "To": "04:00"
        },
        {
          "From": "06:00",
          "To": "08:00"
        }
      ],
      "Price": 666,
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Available_Till": null,
      "Available_From": null,
      "Location": "Business Address",
      "Availability_Type": "Specific Day(s)",
      "Service_Name": "fourthService",
      "Duration": 30,
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Available_Days": [
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
      ],
      "Price": 3848,
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    },
    {
      "Owner": {
        "id": "111115000000058229",
        "full_name": "madesh04",
        "name": "madesh04"
      },
      "Job_Sheet_Required": "Yes",
      "Available_Till": "2026-01-22",
      "Available_From": "2026-01-02",
      "Availability_Type": "Specific Date Range",
      "Location": "Business Address",
      "Service_Name": "fifthService",
      "Duration": 60,
      "Members": [
        {
          "Members": {
            "name": "madesh04",
            "id": "111115000000058229"
          }
        }
      ],
      "Available_Timings": [
        {
          "From": "00:00",
          "To": "06:00"
        },
        {
          "From": "07:00",
          "To": "14:00"
        }
      ],
      "Price": 777,
      "Tax": [
        {
          "id": null,
          "value": "Sales Tax - 0.0 %"
        },
        {
          "id": null,
          "value": "Vat - 0.0 %"
        }
      ],
      "Description": "service description",
      "$zia_owner_assignment": "owner_recommendation_unavailable",
      "zia_suggested_users": {},
      "Layout": {
        "id": "111115000000070573"
      }
    }
  ],
  "skip_mandatory": false
}
```
