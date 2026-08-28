# GET /settings/territories
**Operation:** `getTerritories` — Get all territories
> To retrieve the list of territories enabled for your Zoho CRM organization.

**Tags:** Territories

**Parameters:**
- `include` (query, string, optional) [maxLen=100, enum=[7 values]]: Include account_rule_criteria, lead_rule_criteria (or) deal_rule_criteria.
- `ids` (query, array, optional) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: List of Territory Ids
- `page` (query, integer/int32, optional) [min=1]: Page Numeber
- `per_page` (query, integer/int32, optional) [min=1, max=2000]: Per Page Number
- `filters` (query, object, optional): Filter Out the Territories based on Given Criteria
- `include_inner_details` (query, string, optional) [enum=['manager.zuid,manager.status', 'manager.zuid', 'manager.status']]: Include manager status & zuid

**Schemas:**
`BetweenFilterCriterionResponse`:
  > Represents the response for a filter criterion using the between and not_between comparators. The value is an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator returned for the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field was evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the between filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`EqualFilterCriterionResponse`:
  > Represents the response for a filter criterion using the equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime; SimpleFilterCriterionValueNumber for integer, currency, or double; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup, ownerlookup, or userlookup; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator returned for the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value returned for the equal comparator. Contains a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'value', 'pre_defined', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the equal filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`EqualityFilterCriterionResponse`:
  oneOf:
    - `EqualFilterCriterionResponse` — Represents the response for a filter criterion using the equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime; SimpleFilterCriterionValueNumber for integer, currency, or double; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup, ownerlookup, or userlookup; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
    - `NotEqualFilterCriterionResponse` — Represents the response for a filter criterion using the not_equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text-based types; SimpleFilterCriterionValueNumber for numeric types; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup types; and SimpleFilterCriterionValueObjectPredefined for predefined user or role placeholders.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GroupedFilterCriterionResponse`:
  > Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
      - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
  - `$disrupted` (boolean) — Indicates whether the grouped filter criterion is in a disrupted state, typically due to an invalid or unresolvable condition within the group.
`MultiSelectLookupFilterCriterionResponse`:
  > Represents the response for a filter criterion using the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion was applied. The field has a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator returned for the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectResponse`) [minItems=1, maxItems=500] **REQ** — Contains an array of lookup object references returned for the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the multi-select lookup filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`NotEqualFilterCriterionResponse`:
  > Represents the response for a filter criterion using the not_equal comparator. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for text-based types; SimpleFilterCriterionValueNumber for numeric types; SimpleFilterCriterionValueBoolean for Boolean; SimpleFilterCriterionValueObjectResponse for lookup types; and SimpleFilterCriterionValueObjectPredefined for predefined user or role placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator returned for the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value returned for the not_equal comparator. Contains a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectResponse` — Represents a lookup object filter criterion value for response bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. Both the ID and name properties are included.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'value', 'pre_defined', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the not-equal filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`OrderingFilterCriterionResponse`:
  > Represents the response for a filter criterion using the less_than, less_equal, greater_than, and greater_equal comparators. The value is a scalar; arrays and objects are not valid.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator returned for the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value returned for the ordering comparator.
    anyOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the ordering filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`SetFilterCriterionResponse`:
  > Represents the response for a filter criterion using the in and not_in comparators. The value is an array of primitive values.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator returned for the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values returned for the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the set filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.
`SimpleFilterCriterionResponse`:
  oneOf:
    - `EqualityFilterCriterionResponse` — Represents the response for an equality filter criterion that dispatches to either the EqualFilterCriterionResponse or NotEqualFilterCriterionResponse schema based on the comparator value.
    - `TextFilterCriterionResponse` — Represents the response for a filter criterion using the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value is a string scalar or array; SimpleFilterCriterionValueString applies to text-based field types.
    - `OrderingFilterCriterionResponse` — Represents the response for a filter criterion using the less_than, less_equal, greater_than, and greater_equal comparators. The value is a scalar; arrays and objects are not valid.
    - `BetweenFilterCriterionResponse` — Represents the response for a filter criterion using the between and not_between comparators. The value is an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `SetFilterCriterionResponse` — Represents the response for a filter criterion using the in and not_in comparators. The value is an array of primitive values.
    - `MultiSelectLookupFilterCriterionResponse` — Represents the response for a filter criterion using the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
`SimpleFilterCriterionValueObjectBase`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (string/int64) — Represents the unique ID of the lookup module record.
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`SimpleFilterCriterionValueObjectPredefined`:
  oneOf:
      - `name` (string) **REQ** [enum=['${CURRENTUSER}']] — Represents the predefined placeholder for the currently logged-in user.
Possible values:
${CURRENTUSER} - Represents the currently logged-in user.
      - `id` (string) **REQ** [enum=['${CURRENTUSERROLE}']] — Represents the predefined placeholder for the logged-in user's role record ID.
Possible values:
${CURRENTUSERROLE} - Represents the role of the currently logged-in user.
      - `name` (string) [maxLen=255] — Represents an optional display label for the predefined role, such as Logged in User Role.
      additionalProperties: any
`SimpleFilterCriterionValueObjectResponse`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (object) **REQ**
  additionalProperties: any
`TerritoryGETSchema`:
  > Individual territory object containing detailed information about the territory.
  - `created_time` (string/date-time) **REQ** — Represents the date and time the territory record took effect, in ISO 8601 format.
  - `modified_time` (string/date-time) **REQ** — Represents the date and time when the territory was last modified, in ISO 8601 format.
  - `manager` (object) **REQ**
    oneOf:
        - `name` (string) **REQ** [maxLen=100] — Represents the display name of the territory manager.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the territory manager.
        - `zuid` (string/int32) — Represents the Zoho User ID (ZUID) of the territory manager.
        - `status` (string) [enum=['deleted', 'rejected', 'active', 'closed', 'disabled']] — Represents the current status of the territory manager. Possible values: **deleted**, **rejected**, **active**, **closed**, **disabled**.
        type: null [const=None] — Represents the absence of a territory manager.
  - `reporting_to` (object) **REQ**
    oneOf:
        - `name` (string) **REQ** [maxLen=100] — Represents the display name of the parent territory.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the parent territory.
        type: null [const=None] — Represents the absence of a parent territory for this territory.
  - `permission_type` (string) **REQ** [enum=['read_write_delete', 'read_only']] — Represents the access permission for users in this territory. Possible values: **read_write_delete**, **read_only**.
  - `modified_by` (object) **REQ** — Represents the user who last modified the territory.
    - `name` (string) **REQ** [maxLen=100] — Represents the display name of the user who last modified the territory.
    - `id` (string/int64) **REQ** — Represents the unique identifier of the user who last modified the territory.
  - `description` (object) **REQ**
    oneOf:
        type: null [const=None] — Represents the absence of a description for the territory.
        type: string [maxLen=250] — Represents the description of the territory.
  - `id` (string/int64) **REQ** — Represents the unique identifier of the territory.
  - `created_by` (object) **REQ** — Represents the user who created the territory.
    - `name` (string) **REQ** [maxLen=100] — Represents the display name of the user who created the territory.
    - `id` (string/int64) **REQ** — Represents the unique identifier of the user who created the territory.
  - `account_rule_criteria` (object) — Represents the criteria used to auto-assign accounts to the territory.
    oneOf:
      - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
      - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
        type: null [const=None] — Represents the absence of an account rule criteria for the territory.
  - `deal_rule_criteria` (object) — Represents the criteria used to auto-assign deals to the territory.
    oneOf:
      - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
      - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
        type: null [const=None] — Represents the absence of a deal rule criteria for the territory.
  - `lead_rule_criteria` (object) — Represents the criteria used to auto-assign leads to the territory.
    oneOf:
      - `SimpleFilterCriterionResponse` — Represents the response for a simple field-based filter criterion, dispatching to the appropriate comparator-specific response schema.
      - `GroupedFilterCriterionResponse` — Represents the grouped filter criterion returned in the response, containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
        type: null [const=None] — Represents the absence of a lead rule criteria for the territory.
  - `name` (string) **REQ** [maxLen=50] — Represents the display name of the territory.
  - `api_name` (string) **REQ** [maxLen=100] — Represents the unique API name of the territory used in API requests.
`TextFilterCriterionResponse`:
  > Represents the response for a filter criterion using the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value is a string scalar or array; SimpleFilterCriterionValueString applies to text-based field types.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion was applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator returned for the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value returned for the text comparator. Contains a scalar string or an array of string values.
    oneOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
  - `$disrupted` (boolean) — Indicates whether the text filter criterion is in a disrupted state, typically due to an invalid or unresolvable field or value reference.

**Responses:**

- **200**: Returns the list of territories enabled for the Zoho CRM organization. Use the **info** object to navigate through paginated results. — Schema: `TerritoryListResponse` [application/json]
    > Represents the response for the GET /settings/territories endpoint. Returns either a paginated list of territories with an info object, or a filtered list of territories when the ids parameter is provided.
    oneOf:
        - `territories` (array of object `TerritoryGETSchema`) [minItems=1, maxItems=200] **REQ** — Represents the list of territory objects returned in the paginated response.
        - `info` (object `InfoSchema`) **REQ** — Pagination metadata for the response.
          schema: `InfoSchema`
          - `per_page` (integer/int32) **REQ** [min=1, max=2000] — Represents the number of records returned per page.
          - `count` (integer/int32) **REQ** [min=0] — Represents the total number of records returned in the current page.
          - `page` (integer/int32) **REQ** [min=1] — Represents the current page number of the paginated results.
          - `more_records` (boolean) **REQ** — Indicates whether more records are available in subsequent pages.
        - `territories` (array of object `TerritoryGETSchema`) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects filtered by the specified IDs.

- **204**: No territories found for the given query parameters.

- **400**: The request contains an invalid filter parameter.\n**Resolution:** The **filters** query parameter must use a supported field name. [application/json]
    > Represents the error response for the GET /settings/territories request. Contains either an unsupported filter field error or a territory feature not enabled error.
    oneOf:
      - `NotSupportedFieldsInFilters` — Represents the error response when unsupported fields are used in filter parameters.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request. Possible values: **INVALID_DATA**.
        - `details` (object) **REQ** — Represents additional details about the error, including the name of the unsupported filter parameter.
          - `param_name` (string) **REQ** [enum=['filters']] — Represents the name of the unsupported filter parameter. Possible values: **filters**.
        - `message` (string) **REQ** [enum=[4 values]] — Represents the error message returned when an unsupported field is used in filters. Possible values: **The given api_name(description) is not supported**, **The given api_name(reporting_to) is not supported**, **The given api_name(manager) is not supported**, **Specify Atleast one field**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `FilterNotSupportedApiName` — Represents an error response returned when a filter criterion references a field API name that is not supported for filtering. The details object identifies the unsupported field and its location within the filter parameter.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Indicates the error classification assigned to this response.
Possible values:
**NOT_SUPPORTED** - The referenced field API name is not permitted for use in filter criteria.
        - `details` (object) **REQ** — Contains the contextual details identifying the unsupported field that caused the error, including its API name, its location within the filter expression, and the name of the filter parameter involved.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the field that is not supported for use in filter criteria and triggered this error.
          - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSONPath location of the unsupported field within the filter expression.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the name of the filter request parameter that carried the unsupported field API name.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive message summarizing the nature of the error returned by the API.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the API response.
Possible values:
**error** - The request failed because an unsupported field API name was used in the filter criteria.
      - `FilterEmptyFilterObject` — Represents the error response returned when a filter object is submitted without any recognized fields — such as group or criteria — where at least one is required for the expression to be valid. The error code is EXPECTED_FIELD_MISSING.
        - `code` (string) **REQ** [enum=['EXPECTED_FIELD_MISSING']] — Indicates the error classification for this failure.
Possible values:
**EXPECTED_FIELD_MISSING** - None of the expected filter fields were present in the submitted filter object.
        - `details` (object) **REQ** — Contains structured diagnostic detail about the empty filter object, including the parameter name and the list of fields that were expected but entirely absent from the filter expression.
          - `expected_fields` (array of object) [minItems=1, maxItems=100, uniqueItems] **REQ** — Contains the collection of fields that the filter object was expected to include, of which at least one must be present for the request to be valid. Each entry identifies the field by its API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of a field expected to be present in the filter object.
            - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSON path at which the expected field should be present within the filter object.
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the filter parameter associated with the empty filter object error. This field is a filter-specific extension to the standard error detail structure.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive message summarizing the empty filter object error.
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome status of the API response.
Possible values:
**error** - The request failed because the filter object did not contain any of the expected fields.
      - `FilterMandatoryNotFound` — Represents an error response returned when a mandatory field required by the filter criteria is absent from the request. Includes a filter-specific param_name field that extends the standard MANDATORY_NOT_FOUND error structure.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Indicates the error code identifying the category of failure.
Possible values:
**MANDATORY_NOT_FOUND** - A mandatory field was absent from the filter criteria.
        - `details` (object) **REQ** — Contains detailed information identifying the mandatory field that is absent from the request, including its API name, JSON path location, and, as a filter-specific extension, its parameter name.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the mandatory field that was not found in the filter criteria.
          - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the mandatory field that is missing from the filter criteria.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the parameter name associated with the missing mandatory field, as a filter-specific extension to the standard error detail.
        - `message` (string) **REQ** [maxLen=512] — Contains a brief error message describing which mandatory field was not found in the filter criteria.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the response.
Possible values:
**error** - The request failed because a mandatory field was absent from the filter criteria.
      - `FilterInvalidComparator` — Represents an error response returned when a filter field is provided with a comparator operator that is not supported for that field. The error code is INVALID_DATA.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Indicates the category of error associated with this response.
Possible values:
**INVALID_DATA** - An unsupported comparator operator was provided for the filter field.
        - `details` (object) **REQ** — Contains structured details identifying the filter field that received an unsupported comparator, including its location, parameter name, and the list of valid comparator values accepted for that field.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the filter field to which an unsupported comparator operator was applied.
          - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the specific filter field within the request payload that carries the unsupported comparator operator.
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the filter parameter whose comparator was rejected, scoped as a filter-specific extension to the standard error detail.
          - `supported_values` (array of string) [minItems=1, maxItems=100, uniqueItems] **REQ** — Contains the list of comparator values that are valid for the offending filter field.
            items: [maxLen=256]
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive summary of the invalid-comparator error, identifying the rejected operator and the affected filter parameter.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall outcome of the request.
Possible values:
**error** - The request failed due to an invalid filter comparator.
      - `FilterFieldComparatorValueMissing` — Represents an error response returned when a filter field that requires a comparator value is submitted without one, typically because a required upstream dependee field is absent from the filter expression.
        - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Indicates the error classification assigned to this response.
Possible values:
**DEPENDENT_FIELD_MISSING** - A filter field's required comparator value is absent because its upstream dependee field was not supplied in the filter criteria.
        - `details` (object) **REQ** — Contains structured details about the missing comparator value error, identifying the field in error, the upstream dependee field that constrains it, and the filter parameter context in which the violation occurred.
          - `dependee` (object) **REQ** — Represents the upstream field whose value constrains the comparator requirements of the field currently in error. Contains the API name and JSONPath location of that upstream dependee field within the filter expression.
            - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the upstream dependee field whose value constrains the comparator requirements of the field currently in error.
            - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSONPath location of the upstream dependee field within the filter expression.
          - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the filter field whose comparator value is absent, identifying which field in the filter expression triggered the error.
          - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSONPath location of the field in error within the filter expression, pinpointing where the missing comparator value was detected.
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the filter parameter that carries the filter criteria in which the missing comparator value was detected.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive message summarizing the missing comparator value error.
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome status of the response.
Possible values:
**error** - The request failed because a required comparator value was absent from the filter criteria.
      - `FilterFieldComparatorMismatch` — Represents an error response returned when a filter field's comparator value does not match any of the values permitted by the upstream dependee field's value. Contains the offending field's API name and JSONPath location, the dependee field's identity, the filter parameter context, and the list of supported comparator values.
        - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Indicates the error type for this response.
Possible values:
**DEPENDENT_MISMATCH** - The comparator supplied for the field does not match the set of comparators permitted given the current value of the dependee field.
        - `details` (object) **REQ** — Contains structured details about the comparator mismatch, identifying the field in error, the upstream dependee field whose value constrains valid comparators, and the set of comparator values that are permitted.
          - `dependee` (object) **REQ** — Represents the upstream field whose current value determines which comparators are valid for the field identified in `api_name`. Contains the upstream field's API name and its location within the filter expression.
            - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the upstream dependee field whose value constrains the set of comparators permitted for the field currently in error.
            - `json_path` (string) **REQ** [maxLen=512] — Contains the JSONPath expression locating the dependee field within the filter expression submitted in the request.
          - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the field whose supplied comparator value does not match the comparators permitted given the current value of the dependee field.
          - `json_path` (string) **REQ** [maxLen=512] — Contains the JSONPath expression locating the field in error within the filter expression submitted in the request.
          - `supported_values` (array of string) [minItems=1, maxItems=100, uniqueItems] **REQ** — Contains the complete set of comparator values that are permitted for the field in error, as determined by the current value of the dependee field.
            items: [maxLen=256]
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the filter query parameter that carries the filter expression containing the comparator mismatch.
        - `message` (string) **REQ** [maxLen=512] — Represents a short, descriptive summary of the comparator-field dependency violation.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request.
Possible values:
**error** - The request failed due to a comparator value mismatch in the filter criteria.
      - `FilterFieldValueMismatch` — Represents the error response returned when a filter field's value carries a data type that does not satisfy the requirement imposed by its dependee field's current value.
        - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Indicates the category of error associated with this response.
Possible values:
**DEPENDENT_MISMATCH** - A filter field's value has a data type that conflicts with the requirement set by the dependee field.
        - `details` (object) **REQ** — Contains diagnostic details identifying the offending filter field, its expected data type, the dependee field that governs that expectation, and the filter parameter in which the mismatch was detected.
          - `dependee` (object) **REQ** — Represents the field whose current value dictates the required data type for the offending filter field.
            - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the dependee field whose value drives the data type requirement for the offending filter field.
            - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSON path locating the dependee field within the request payload.
          - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the filter field whose supplied value does not match the data type required by the dependee field.
          - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSON path locating the filter field whose value carries the data type mismatch within the request payload.
          - `expected_data_type` (string) **REQ** [maxLen=256] — Indicates the data type expected by the dependee field against which the submitted filter value was validated.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the filter-specific query parameter name associated with the field that failed value validation.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive explanation of the filter field value mismatch error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the response.
Possible values:
**error** - The request failed because a filter field value did not match the type required by the dependee field.
      - `FilterComparatorValueMismatch` — Represents an error returned when a value associated with a filter comparator fails validation due to constraints imposed by a dependee field. This error targets the value driven by the comparator rather than the comparator operator selection itself.
        - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Indicates the classification of the error.
Possible values:
**DEPENDENT_MISMATCH** - The comparator-driven value failed validation due to constraints imposed by the dependee field.
        - `details` (object) **REQ** — Contains structured diagnostic details identifying the filter field whose comparator-driven value failed dependency validation, including the controlling dependee field reference.
          - `dependee` (object) **REQ** — Represents the dependee field whose state or constraints govern the validation rules applied to the comparator value of the current filter field.
            - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the dependee field whose constraints triggered the comparator value validation failure.
            - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the dependee field within the request structure whose constraints govern the comparator value validation.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the filter field whose supplied value does not match the requirements of the comparator operator in use.
          - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the specific filter field whose value is incompatible with the comparator operator applied to it.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the filter-specific parameter name identifying the request parameter associated with the comparator value mismatch.
        - `message` (string) **REQ** [maxLen=512] — Contains a descriptive error message summarizing the comparator-value mismatch encountered in the filter request.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the response.
Possible values:
**error** - The request failed because the comparator-driven value did not satisfy dependency validation rules.
      - `FilterInvalidParamDataType` — Represents an error response returned when a filter parameter is supplied with an incorrect data type. Contains the error code, a descriptive message, and details identifying the offending parameter along with its expected data type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error classification code for this response.
Possible values:
**INVALID_DATA** - The filter parameter was supplied with an incorrect data type.
        - `details` (object) **REQ** — Contains structured details about the data type mismatch, including the name of the offending filter parameter and the data type it is expected to carry.
          - `expected_data_type` (string) **REQ** [maxLen=256] — Represents the data type that the filter parameter is required to carry for the request to be valid.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the name of the query or body parameter — such as `filters` — that carries the filter criteria and was supplied with an invalid data type.
        - `message` (string) **REQ** [maxLen=512] — Represents a descriptive message explaining the data type error encountered for the filter parameter.
        - `status` (string) **REQ** [enum=['error']] — Represents the outcome of the request.
Possible values:
**error** - The request failed due to an invalid filter parameter data type.
      - `FilterInvalidFieldDataType` — Represents the error response returned when a field within the filter criteria contains a value of an incorrect data type. Includes the API name of the offending field, its JSONPath location within the filter expression, and the data type the field expects.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Indicates the category of error returned.
Possible values:
**INVALID_DATA** - A field in the filter criteria was supplied with an incorrect data type.
        - `details` (object) **REQ** — Contains diagnostic details identifying the specific filter field whose value failed the data type check, including its API name, its location in the filter expression, the expected data type, and the name of the filter parameter that carried the criteria.
          - `api_name` (string) **REQ** [maxLen=256] — Indicates the API name of the filter field whose supplied value does not match the field's required data type.
          - `json_path` (string) **REQ** [maxLen=512] — Indicates the JSONPath location within the filter criteria expression where the data type mismatch was detected.
          - `expected_data_type` (string) **REQ** [maxLen=256] — Indicates the data type that the identified filter field requires, against which the submitted value was evaluated and found incompatible.
          - `param_name` (string) **REQ** [maxLen=256] — Indicates the name of the query or body parameter that carried the filter criteria containing the invalid field value.
        - `message` (string) **REQ** [maxLen=512] — Represents a brief description of the data type error encountered for the filter field.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request.
Possible values:
**error** - The request failed due to an invalid data type in the filter criteria.
      - `FilterFieldNotSupportedInCriteria` — Represents an error response returned when a filter criteria field references a field type that is not supported for filtering, such as file upload or image upload fields.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Indicates the error code identifying the category of failure.
Possible values:
**INVALID_DATA** - The field referenced in the filter criteria is not supported for filtering.
        - `details` (object) **REQ** — Contains details identifying the specific field that is not supported in filter criteria, including its API name, JSON path, and associated parameter name.
          - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the field that is not supported within the filter criteria expression.
          - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the unsupported field within the filter criteria structure.
          - `param_name` (string) **REQ** [maxLen=256] — Represents the parameter name associated with the unsupported field, as a filter-specific extension to the standard error detail.
        - `message` (string) **REQ** [maxLen=512] — Contains a brief error message describing why the specified field is not supported in the filter criteria.
        - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the response.
Possible values:
**error** - The request failed because a field type not supported in filter criteria was referenced.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failure due to missing, expired, or invalid OAuth token.\n**Resolution:** A new access token must be generated with the required scope for this API. — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.READ
