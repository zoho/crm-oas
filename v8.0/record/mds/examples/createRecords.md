# Examples: createRecords

**POST /{module}**

## Parameter examples

### `module` (path) — Example

```json
"Leads"
```

## Request examples

### `application/json` — LeadsCreateExample

Create a new Lead record

```json
{
  "data": [
    {
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Company": "ABC Corp",
      "First_Name": "Patricia",
      "Last_Name": "Boyle",
      "Email": "boyle@abc.com",
      "Phone": "111-1234567",
      "Fax": "555-7654321",
      "Mobile": "555-9876543",
      "Website": "www.abc.com",
      "Lead_Source": "Web Download",
      "Lead_Status": "Not Contacted",
      "Industry": "Technology",
      "No_of_Employees": 250,
      "Annual_Revenue": 500000,
      "Email_Opt_Out": false,
      "Skype_ID": "patricia.boyle",
      "Street": "24 Vine Street",
      "City": "Newark",
      "State": "New Jersey",
      "Zip_Code": "07102",
      "Country": "USA",
      "Description": "Interested in enterprise licensing",
      "Rating": "Hot",
      "Secondary_Email": "patricia.b@abc.com"
    }
  ]
}
```

### `application/json` — ContactsCreateExample

Create a new Contact record

```json
{
  "data": [
    {
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "First_Name": "Kane",
      "Last_Name": "Kingslei",
      "Full_Name": "Anna Kingsley",
      "Account_Name": {
        "name": "Bentley Systems",
        "id": "5725767000007910001"
      },
      "Email": "anna.kingsley@bentley.com",
      "Title": "VP of Sales",
      "Department": "Sales",
      "Phone": "555-33445561",
      "Home_Phone": "555-3344557",
      "Other_Phone": "555-3344558",
      "Fax": "555-3344559",
      "Mobile": "555-3344550",
      "Date_of_Birth": "1985-04-12",
      "Assistant": "Diane Cole",
      "Email_Opt_Out": false,
      "Skype_ID": "anna.kingsley",
      "Mailing_Street": "220 Market Street",
      "Mailing_City": "Philadelphia",
      "Mailing_State": "Pennsylvania",
      "Mailing_Zip": "19103",
      "Mailing_Country": "USA",
      "Description": "Primary decision maker"
    }
  ]
}
```

### `application/json` — AccountsCreateExample

Create a new Account record

```json
{
  "data": [
    {
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Account_Name": "Bentley Systems",
      "Phone": "555-2233445",
      "Fax": "555-2233446",
      "Parent_Account": {
        "name": "Bentley Holdings",
        "id": "5725767000007908001"
      },
      "Website": "www.bentleysystems.com",
      "Ticker_Symbol": "BSY",
      "Account_Type": "Customer",
      "Ownership": "Private",
      "Industry": "Engineering",
      "Employees": 1200,
      "Annual_Revenue": 25000000,
      "SIC_Code": "3827",
      "Billing_Street": "1000 Commerce Drive",
      "Billing_City": "Exton",
      "Billing_State": "Pennsylvania",
      "Billing_Code": "19341",
      "Billing_Country": "USA",
      "Shipping_Street": "1000 Commerce Drive",
      "Shipping_City": "Exton",
      "Shipping_State": "Pennsylvania",
      "Shipping_Code": "19341",
      "Shipping_Country": "USA",
      "Description": "Key strategic account",
      "Account_Number": "10023",
      "Account_Site": "Headquarters",
      "Tag": [
        {
          "name": "Enterprise"
        }
      ]
    }
  ]
}
```

### `application/json` — DealsCreateExample

Create a new Deal record

```json
{
  "data": [
    {
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Deal_Name": "Bentley Systems - Annual License Renewal",
      "Amount": 85000,
      "Closing_Date": "2026-09-30",
      "Account_Name": {
        "name": "Bentley Systems",
        "id": "5725767000007908001"
      },
      "Stage": "Negotiation/Review",
      "Type": "Existing Business",
      "Expected_Revenue": 80000,
      "Next_Step": "Send revised contract",
      "Lead_Source": "Partner Referral",
      "Contact_Name": {
        "name": "Anna Kingsley",
        "id": "5725767000011356002"
      },
      "Description": "Renewal negotiation for enterprise licensing",
      "Pipeline": "Standard (Standard)",
      "Tag": [
        {
          "name": "Renewal"
        }
      ]
    }
  ]
}
```

### `application/json` — CampaignsCreateExample

Create a new Campaign record

```json
{
  "data": [
    {
      "Campaign_Name": "Fall Renewal Campaign",
      "Type": "Webinar",
      "Status": "In Progress",
      "Start_Date": "2026-09-01",
      "End_Date": "2026-09-30",
      "Expected_Revenue": 150000,
      "Budgeted_Cost": 20000,
      "Actual_Cost": 18500,
      "Expected_Response": 25,
      "Num_sent": 5000,
      "Description": "Renewal-focused email and webinar campaign",
      "Currency": "USD",
      "Parent_Campaign": {
        "name": "2026 Annual Marketing Plan",
        "id": "5725767000004498133"
      },
      "Tag": [
        {
          "name": "Q3"
        }
      ]
    }
  ]
}
```

### `application/json` — TasksCreateExample

Create a new Task record

```json
{
  "data": [
    {
      "Subject": "Follow up on renewal contract",
      "Due_Date": "2026-08-28",
      "Who_Id": {
        "name": "Anna Kingsley",
        "id": "5725767000011356002"
      },
      "Status": "In Progress",
      "Priority": "High",
      "Description": "Confirm terms before sending final contract",
      "Tag": [
        {
          "name": "Renewal"
        }
      ]
    }
  ]
}
```

### `application/json` — CasesCreateExample

Create a new Case record

```json
{
  "data": [
    {
      "Status": "In Progress",
      "Product_Name": {
        "name": "CRM Enterprise Suite",
        "id": "5725767000006754021"
      },
      "Priority": "High",
      "Type": "Question",
      "Case_Origin": "Email",
      "Subject": "Unable to export report as PDF",
      "Account_Name": {
        "name": "Bentley Systems",
        "id": "5725767000011373001"
      },
      "Deal_Name": {
        "name": "Bentley Systems - Annual License Renewal",
        "id": "5725767000011360004"
      },
      "Reported_By": "Anna Kingsley",
      "Email": "anna.kingsley@bentleysystems.com",
      "Phone": "555-3344556",
      "Description": "Customer reports PDF export fails with a timeout error",
      "Internal_Comments": "Escalated to engineering team",
      "Solution": "Restart the export service and retry",
      "Comments": "Awaiting customer confirmation",
      "Currency": "USD",
      "Case_Reason": "Product Defect",
      "Tag": [
        {
          "name": "Escalated"
        }
      ]
    }
  ]
}
```

### `application/json` — EventsCreateExample

Create a new Event record

```json
{
  "data": [
    {
      "Event_Title": "Renewal Contract Review",
      "Meeting_Venue__s": "Client location",
      "venue": "Zoho Conference Room",
      "Who_Id": {
        "name": "Anna Kingsley",
        "id": "5725767000011356002"
      },
      "All_day": false,
      "Start_DateTime": "2026-08-25T10:00:00-05:00",
      "End_DateTime": "2026-08-25T11:00:00-05:00",
      "Description": "Review the final renewal terms with Bentley Systems",
      "Participants": [
        {
          "Email": "alice@mail.com",
          "name": "Alice Brown",
          "type": "lead",
          "participant": "5725767000005425036"
        }
      ],
      "Remind_At": [
        {
          "unit": 15,
          "period": "minutes"
        }
      ],
      "Tag": [
        {
          "name": "Renewal"
        }
      ]
    }
  ]
}
```

### `application/json` — CallsCreateExample

Create a new Call record

```json
{
  "data": [
    {
      "Subject": "Discuss renewal pricing",
      "Call_Type": "Outbound",
      "Call_Purpose": "Prospecting",
      "Who_Id": {
        "name": "Anna Kingsley",
        "id": "5725767000011356002"
      },
      "Call_Start_Time": "2026-01-20T10:00:00-05:00",
      "Call_Duration": "00:20",
      "Description": "Discussed renewal pricing options and next steps",
      "Call_Result": "Interested",
      "Tag": [
        {
          "name": "Renewal"
        }
      ]
    }
  ]
}
```

### `application/json` — SolutionsCreateExample

Create a new Solution record

```json
{
  "data": [
    {
      "Solution_Title": "How to resolve PDF export timeout error",
      "Product_Name": {
        "name": "CRM Enterprise Suite",
        "id": "5725767000006754021"
      },
      "Question": "Why does the PDF export fail with a timeout error?",
      "Answer": "Restart the export service from Setup > System Settings and retry the export.",
      "Tag": [
        {
          "name": "Known Issue"
        }
      ]
    }
  ]
}
```

### `application/json` — ProductsCreateExample

Create a new Product record

```json
{
  "data": [
    {
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Product_Name": "CRM Enterprise Suite",
      "Product_Code": "PRD-2001",
      "Vendor_Name": {
        "name": "Zylker Hardwares",
        "id": "5725767000001693003"
      },
      "Product_Active": true,
      "Manufacturer": "Zylker Corp",
      "Product_Category": "Software",
      "Sales_Start_Date": "2026-01-01",
      "Sales_End_Date": "2027-12-31",
      "Support_Start_Date": "2026-01-01",
      "Support_Expiry_Date": "2027-12-31",
      "Unit_Price": 999,
      "Commission_Rate": 5,
      "Taxable": true,
      "Usage_Unit": "License",
      "Qty_Ordered": 100,
      "Qty_in_Stock": 50,
      "Reorder_Level": 10,
      "Qty_in_Demand": 20,
      "Description": "Enterprise-grade CRM licensing bundle",
      "Tag": [
        {
          "name": "Flagship"
        }
      ]
    }
  ]
}
```

### `application/json` — VendorsCreateExample

Create a new Vendor record

```json
{
  "data": [
    {
      "Vendor_Name": "Zylker Hardwares",
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Phone": "555-4455667",
      "Email": "sales@zylkerhardwares.com",
      "Website": "www.zylkerhardwares.com",
      "Category": "Hardware Supplier",
      "Street": "88 Industrial Ave",
      "City": "Trenton",
      "State": "New Jersey",
      "Zip_Code": "08608",
      "Country": "USA",
      "Description": "Primary hardware supplier",
      "Tag": [
        {
          "name": "Preferred Vendor"
        }
      ]
    }
  ]
}
```

### `application/json` — PurchaseOrdersCreateExample

Create a new Purchase Order record

```json
{
  "data": [
    {
      "PO_Number": "PO-88213",
      "Subject": "Purchase Order for CRM Enterprise Suite Stock",
      "Vendor_Name": {
        "name": "Zylker Hardwares",
        "id": "5725767000011346004"
      },
      "Contact_Name": {
        "name": "Anna Kingsley",
        "id": "5725767000011356002"
      },
      "PO_Date": "2026-08-15",
      "Due_Date": "2026-09-01",
      "Carrier": "UPS",
      "Excise_Duty": 0,
      "Sales_Commission": 0,
      "Status": "Approved",
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Sub_Total": 50000,
      "Discount": 0,
      "Tax": 0,
      "Adjustment": 0,
      "Grand_Total": 50000,
      "Billing_Street": "88 Industrial Ave",
      "Billing_City": "Trenton",
      "Billing_State": "New Jersey",
      "Billing_Code": "08608",
      "Billing_Country": "USA",
      "Shipping_Street": "1000 Commerce Drive",
      "Shipping_City": "Exton",
      "Shipping_State": "Pennsylvania",
      "Shipping_Code": "19341",
      "Shipping_Country": "USA",
      "Terms_and_Conditions": "Net 30",
      "Description": "Restocking order for enterprise licenses",
      "Tracking_Number": "1Z999AA10123456784",
      "Requisition_No": "REQ-4021",
      "Purchase_Items": [
        {
          "Product_Name": {
            "name": "CRM Enterprise Suite",
            "id": "5725767000011358006"
          },
          "quantity": 50,
          "list_price": 999,
          "discount": 0,
          "total": 49950
        }
      ]
    }
  ]
}
```

### `application/json` — PriceBooksCreateExample

Create a new Price Book record

```json
{
  "data": [
    {
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Price_Book_Name": "Standard Price Book 2026",
      "Active": true,
      "Pricing_Model": "Flat",
      "Pricing_Details": [
        {
          "from_range": 1,
          "to_range": 10,
          "discount": 0,
          "unit_price": 999
        },
        {
          "from_range": 11,
          "to_range": 50,
          "discount": 10,
          "unit_price": 899.1
        }
      ],
      "Tag": [
        {
          "name": "2026"
        }
      ]
    }
  ]
}
```

### `application/json` — QuotesCreateExample

Create a new Quote record

```json
{
  "data": [
    {
      "Quote_Number": "Q-00234",
      "Subject": "Quote for Bentley Systems Renewal",
      "Deal_Name": {
        "name": "Bentley Systems - Annual License Renewal",
        "id": "5725767000011360004"
      },
      "Quote_Stage": "Delivered",
      "Valid_Till": "2026-09-15",
      "Contact_Name": {
        "name": "Anna Kingsley",
        "id": "5725767000011356002"
      },
      "Account_Name": {
        "name": "Bentley Systems",
        "id": "5725767000011373001"
      },
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Carrier": "FedEx",
      "Sub_Total": 90000,
      "Discount": 5000,
      "Tax": 0,
      "Adjustment": 0,
      "Grand_Total": 85000,
      "Billing_Street": "1000 Commerce Drive",
      "Billing_City": "Exton",
      "Billing_State": "Pennsylvania",
      "Billing_Code": "19341",
      "Billing_Country": "USA",
      "Shipping_Street": "1000 Commerce Drive",
      "Shipping_City": "Exton",
      "Shipping_State": "Pennsylvania",
      "Shipping_Code": "19341",
      "Shipping_Country": "USA",
      "Terms_and_Conditions": "Payment due within 30 days",
      "Description": "Renewal quote for enterprise licensing",
      "Team": "Sales Team East",
      "Quoted_Items": [
        {
          "Product_Name": {
            "name": "CRM Enterprise Suite"
          }
        }
      ]
    }
  ]
}
```

### `application/json` — SalesOrdersCreateExample

Create a new Sales Order record

```json
{
  "data": [
    {
      "SO_Number": "SO-00567",
      "Subject": "Sales Order for Bentley Systems Renewal",
      "Deal_Name": {
        "name": "Bentley Systems - Annual License Renewal",
        "id": "5725767000011360004"
      },
      "Purchase_Order": "PO-88213",
      "Quote_Name": {
        "name": "Q-00234",
        "id": "5725767000011359014"
      },
      "Due_Date": "2026-09-20",
      "Pending": "0.00",
      "Contact_Name": {
        "name": "Anna Kingsley",
        "id": "5725767000011356002"
      },
      "Account_Name": {
        "name": "Bentley Systems",
        "id": "5725767000011373001"
      },
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Carrier": "FedEx",
      "Excise_Duty": 0,
      "Sales_Commission": 5,
      "Status": "Created",
      "Sub_Total": 90000,
      "Discount": 5000,
      "Tax": 0,
      "Adjustment": 0,
      "Grand_Total": 85000,
      "Billing_Street": "1000 Commerce Drive",
      "Billing_City": "Exton",
      "Billing_State": "Pennsylvania",
      "Billing_Code": "19341",
      "Billing_Country": "USA",
      "Shipping_Street": "1000 Commerce Drive",
      "Shipping_City": "Exton",
      "Shipping_State": "Pennsylvania",
      "Shipping_Code": "19341",
      "Shipping_Country": "USA",
      "Terms_and_Conditions": "Payment due within 30 days",
      "Description": "Renewal sales order",
      "Customer_No": "CUST-1042",
      "Ordered_Items": [
        {
          "Product_Name": {
            "Product_Code": "PRD-2001",
            "Qty_Ordered": 100,
            "name": "CRM Enterprise Suite",
            "Qty_in_Stock": 50,
            "Tax": [],
            "id": "5725767000011358006",
            "Taxable": true,
            "Unit_Price": 999
          }
        }
      ]
    }
  ]
}
```

### `application/json` — InvoicesCreateExample

Create a new Invoice record

```json
{
  "data": [
    {
      "Owner": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "Invoice_Number": "INV-3021",
      "Subject": "Invoice for Bentley Systems Renewal",
      "Sales_Order": {
        "name": "SO-00567",
        "id": "5725767000011355014"
      },
      "Invoice_Date": "2026-09-01",
      "Purchase_Order": "PO-88213",
      "Due_Date": "2026-09-30",
      "Account_Name": {
        "name": "Bentley Systems",
        "id": "5725767000011373001"
      },
      "Contact_Name": {
        "name": "Anna Kingsley",
        "id": "5725767000011356002"
      },
      "Grand_Total": 85000,
      "Billing_Street": "1000 Commerce Drive",
      "Billing_City": "Exton",
      "Billing_State": "Pennsylvania",
      "Billing_Code": "19341",
      "Billing_Country": "USA",
      "Shipping_Street": "1000 Commerce Drive",
      "Shipping_City": "Exton",
      "Shipping_State": "Pennsylvania",
      "Shipping_Code": "19341",
      "Shipping_Country": "USA",
      "Terms_and_Conditions": "Payment due within 30 days",
      "Description": "Renewal invoice",
      "Invoiced_Items": [
        {
          "Product_Name": {
            "name": "CRM Enterprise Suite",
            "id": "5725767000011358006"
          },
          "quantity": 90,
          "list_price": 999,
          "discount": 5,
          "total": 85414.5
        }
      ]
    }
  ]
}
```

### `application/json` — CustomModuleCreateExample

Create a record in a custom module

```json
{
  "data": [
    {
      "Name": "Extended Warranty - Bentley Systems",
      "Owner": {
        "name": "Patricia Boyle",
        "id": "554023000000235011"
      },
      "Email": "warranty-admin@zylker.com",
      "Secondary_Email": "warranty-admin2@zylker.com",
      "Email_Opt_Out": false,
      "Description": "Custom module records inherit these system fields (Owner, Name, Email, Currency, Tag, etc.) plus your own user-defined fields",
      "Currency": "USD",
      "Tag": [
        {
          "name": "Custom"
        }
      ]
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Success

Successfully created a single record

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2023-05-10T01:10:47-07:00",
        "Modified_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "Created_Time": "2023-05-10T01:10:47-07:00",
        "id": "5725767000000524157",
        "Created_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "$approval_state": "approved"
      },
      "message": "record added",
      "status": "success"
    }
  ]
}
```

### Status `207` — `application/json` — MixedResults

Mixed create results with one success and one validation error

```json
{
  "data": [
    {
      "code": "SUCCESS",
      "details": {
        "Modified_Time": "2023-05-10T01:10:47-07:00",
        "Modified_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "Created_Time": "2023-05-10T01:10:47-07:00",
        "id": "5725767000000524157",
        "Created_By": {
          "name": "Patricia Boyle",
          "id": "5725767000000411001"
        },
        "$approval_state": "approved"
      },
      "message": "record added",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "Last_Name",
        "json_path": "$.data[1].Last_Name"
      },
      "message": "the field api name given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidData

Invalid field value in the create request

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "message": "The field value given for Company is invalid",
      "status": "error",
      "details": {
        "api_name": "Company",
        "json_path": "$.data[0].Company"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataType

Field value has an incorrect data type

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "integer",
        "api_name": "Number_1",
        "json_path": "$.data[0].Number_1"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidSupportedValue

Unsupported value for a fixed-value field

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.apply_feature_execution[0].name",
        "supported_values": [
          "layout_rules",
          "range_validation",
          "assignment_rules",
          "function_validation_rule",
          "criteria_validation_rule",
          "global_map_dependency",
          "territory_subordinates"
        ]
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataLength

Field value exceeds the maximum allowed length

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 2,
        "api_name": "Number_1",
        "json_path": "$.data[0].Number_1"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module API name in the request URL

```json
{
  "data": [
    {
      "code": "INVALID_MODULE",
      "details": {
        "resource_path_index": 0
      },
      "message": "the module name given seems to be invalid",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MultipleErrors

Multiple validation errors in a single record

```json
{
  "data": [
    {
      "code": "MULTIPLE_OR_MULTI_ERRORS",
      "details": {
        "errors": [
          {
            "code": "DUPLICATE_DATA",
            "details": {
              "api_name": "Email",
              "duplicate_record": {
                "Owner": {
                  "name": "Prajesh Kumar S",
                  "id": "4881139000000307001",
                  "zuid": "736078909"
                },
                "module": {
                  "api_name": "Leads",
                  "id": "4881139000000002175"
                },
                "id": "4881139000000428295"
              },
              "json_path": "$.data[0].Email",
              "more_records": true
            },
            "message": "duplicate data",
            "status": "error"
          },
          {
            "code": "DUPLICATE_DATA",
            "details": {
              "api_name": "Mobile",
              "duplicate_record": {
                "Owner": {
                  "name": "Prajesh Kumar S",
                  "id": "4881139000000307001",
                  "zuid": "736078909"
                },
                "module": {
                  "api_name": "Leads",
                  "id": "4881139000000002175"
                },
                "id": "4881139000002432007"
              },
              "json_path": "$.data[0].Mobile",
              "more_records": true
            },
            "message": "duplicate data",
            "status": "error"
          }
        ]
      },
      "message": "Multiple errors in the request",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissing

Required dependent field missing from the request

```json
{
  "data": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "Product_Category",
          "json_path": "$.data[0].Product_Category"
        },
        "api_name": "Product_Subcategory",
        "json_path": "$.data[0].Product_Subcategory"
      },
      "message": "The field 'Product_Subcategory' is required when 'Product_Category' is provided",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentServiceError

Dependent service error during record creation

```json
{
  "data": [
    {
      "code": "DEPENDENT_SERVICE_ERROR",
      "details": {
        "dependency_error": "NO_PERMISSION"
      },
      "message": "The dependent service does not have permission to complete the operation",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFound

Required field missing from the create request

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "id",
        "json_path": "$.data.service.id"
      },
      "message": "Service Id Not Found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MandatoryNotFoundLayoutRule

Layout rule mandatory field absent from the request

```json
{
  "data": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "layout_rule": {
          "name": "Layout Rule",
          "id": "5410702000000761547"
        },
        "api_name": "Phone",
        "json_path": "$.data[0].Phone"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentMismatch

Dependent field value conflicts with controlling field

```json
{
  "data": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "Status",
          "json_path": "$.data[0].Status"
        },
        "api_name": "Unavailable_Till",
        "json_path": "$.data[0].Unavailable_Till"
      },
      "message": "Unavailable Till must be greater than current Time.",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidRequestMethod

Unsupported HTTP method for this endpoint

```json
{
  "data": [
    {
      "status": "error",
      "message": "The HTTP request method type is not a valid one.",
      "code": "INVALID_REQUEST_METHOD",
      "details": {
        "resource_path_index": 0
      }
    }
  ]
}
```

### Status `400` — `application/json` — AuthorizationFailed

Insufficient privileges to create a record

```json
{
  "data": [
    {
      "code": "AUTHORIZATION_FAILED",
      "details": {
        "resource_path_index": 0
      },
      "message": "User does not have sufficient privilege to perform this action",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateDataError

Duplicate field value matches an existing record

```json
{
  "data": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "Unique_1",
        "duplicate_record": {
          "Owner": {
            "name": "Pranav",
            "id": "2008662000000454001",
            "zuid": "75092197"
          },
          "id": "2008662000006256222"
        },
        "json_path": "$.data[0].Unique_1",
        "id": "2008662000006256222",
        "more_records": false
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — OauthScopeMismatch

OAuth access token missing the required create scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "Unauthorized",
  "status": "error",
  "details": {}
}
```

### Status `403` — `application/json` — NoPermission

User profile lacks module create permission

```json
{
  "code": "NO_PERMISSION",
  "message": "Permission denied",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_View_Leads"
    ]
  }
}
```

### Status `404` — `application/json` — InvalidUrlPattern

Invalid or unrecognized API endpoint URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "message": "Please check if the URL trying to access is a correct one",
  "status": "error",
  "details": {}
}
```

### Status `500` — `application/json` — InternalError

Unexpected internal server error during record creation

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "status": "error",
  "details": {}
}
```
