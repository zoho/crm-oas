# PUT /settings/territories
**Operation:** `updateTerritories` — Update territories

> To update the details of one or more territories in your Zoho CRM organization.


**Tags:** Territories

**Schemas:**
`BetweenFilterCriterionRequest`:
  > Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `field` (object) **REQ** — Represents the target field definition to which the range filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['between', 'not_between']] — Represents the range comparison operator applied to the criterion, indicating whether the field value falls within or outside the specified bounds.
Possible values:
between - Matches records where the field value falls within the specified range.
not_between - Matches records where the field value falls outside the specified range.
  - `value` (array of object) [minItems=2, maxItems=2] **REQ** — Contains the two boundary values — [lower_bound, upper_bound] — against which the field is evaluated for the between or not_between comparator.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`EqualFilterCriterionRequest`:
  > Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['equal']] — Represents the equal comparison operator applied to the criterion.
Possible values:
equal - Matches records where the field value equals the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueGeneralPredefined` (string) [enum=['${EMPTY}', '${NOTEMPTY}']] — Represents a predefined placeholder value applicable to any field data_type with the equal comparator.
Possible values:
${EMPTY} - Matches records where the field has no value.
${NOTEMPTY} - Matches records where the field has any non-empty value.
      - `SimpleFilterCriterionValueDateTimePredefined` (string) [enum=[22 values]] — Represents a predefined placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator.
      - `SimpleFilterCriterionValueNDaysPredefined` (string) [maxLen=255, pattern=^\$\{(LAST_N_|NEXT_N_)(DAYS|WEEKS|MONTHS|YEARS):([0-9]+)\}$] — Represents a predefined N-period range placeholder value applicable only when the field's data_type is date or datetime, with the equal comparator. Follows the pattern ${NEXT_N_<PERIOD>:<n>} or ${LAST_N_<PERIOD>:<n>}, where PERIOD is DAYS, WEEKS, MONTHS, or YEARS and n is a positive integer. The current period is always excluded from the range.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`EqualityFilterCriterionRequest`:
  oneOf:
    - `EqualFilterCriterionRequest` — Represents a filter criterion for the equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders. Accepts scalar or array values. Resolve the data_type from the field's FieldSchema.
    - `NotEqualFilterCriterionRequest` — Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
`FilterFieldBase`:
  > Represents the base field reference used in filter operations, containing minimal required properties. The field's data_type is not part of this object; resolve it from the corresponding FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
  - `id` (string/int64) — Represents the unique ID of the field used for filter operations.
  - `api_name` (string) **REQ** — Represents the API name of the field used for filter application. Supports relationship notation, for example, Deals__r.Stage.
  additionalProperties: any
`GroupedFilterCriterionRequest`:
  > Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group` (array of object) [minItems=2, maxItems=25] **REQ** — Contains an array of filter conditions grouped together and evaluated with the specified logical operator.
    oneOf:
      - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
      - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
  - `group_operator` (string) **REQ** [enum=['AND', 'OR', 'and', 'or']] — Represents the logical operator applied between the filter conditions in the group.
Possible values:
AND - All conditions in the group must be satisfied.
OR - At least one condition in the group must be satisfied.
and - Equivalent to AND; all conditions in the group must be satisfied.
or - Equivalent to OR; at least one condition in the group must be satisfied.
`MultiSelectLookupFilterCriterionRequest`:
  > Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
  - `field` (object) **REQ** — Represents the target field definition to which the multi-select lookup filter criterion is applied. The field must have a data_type of multiuserlookup or multiselectlookup.
  - `comparator` (string) **REQ** [enum=['include_all', 'include_any', 'exclude_all', 'exclude_any']] — Represents the multi-select lookup comparison operator applied to the criterion. Applicable only when the field's data_type is multiuserlookup or multiselectlookup.
Possible values:
include_all - Matches records that include all specified lookup values.
include_any - Matches records that include at least one of the specified lookup values.
exclude_all - Matches records that exclude all specified lookup values.
exclude_any - Matches records that exclude at least one of the specified lookup values.
  - `value` (array of object `SimpleFilterCriterionValueObjectRequest`) [minItems=1, maxItems=5] **REQ** — Contains an array of lookup object references used in the multi-select comparison.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`NotEqualFilterCriterionRequest`:
  > Represents a filter criterion for the not_equal comparator. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime fields; SimpleFilterCriterionValueNumber for integer, currency, or double fields; SimpleFilterCriterionValueBoolean for Boolean fields; SimpleFilterCriterionValueObjectRequest for lookup, ownerlookup, or userlookup fields; and SimpleFilterCriterionValueObjectPredefined for predefined user or role object placeholders.
  - `field` (object) **REQ** — Represents the target field definition to which the not-equal filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['not_equal']] — Represents the not-equal comparison operator applied to the criterion.
Possible values:
not_equal - Matches records where the field value does not equal the specified filter value.
  - `value` (object) **REQ** — Represents the filter value used in the not_equal comparator. Accepts a scalar or an array of values, depending on the field's data_type.
    anyOf:
        type: array of object [minItems=1, maxItems=500]
          oneOf:
            - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
            - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
              anyOf:
                - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
                - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
      - `SimpleFilterCriterionValueBoolean` (boolean) — Represents a Boolean filter criterion value. Applicable only when the field has a Boolean data type (checkbox field).
      - `SimpleFilterCriterionValueObjectRequest` — Represents a lookup object filter criterion value for request bodies, applicable when the field's data_type is lookup, ownerlookup, or userlookup. The ID property is required.
      - `SimpleFilterCriterionValueObjectPredefined` — Represents a predefined placeholder object filter criterion value for lookup fields, applicable with equal or not_equal comparators when the field's data_type is ownerlookup or userlookup. Two forms are supported: (1) the currently logged-in user, represented by passing only the name property with the predefined value ${CURRENTUSER} and no ID property; and (2) the logged-in user's role, represented by passing the ID property with the predefined value ${CURRENTUSERROLE} and an optional display label in the name property. For specific real users or roles that are not predefined, use SimpleFilterCriterionValueObjectRequest, which requires the ID property.
      - `SimpleFilterCriterionValueAgeDuePredefined` (string) [maxLen=255, pattern=^\$\{(AGEINDAYS|DUEINDAYS)\}\+[0-9]+$] — Represents a predefined age or due-in-days placeholder value applicable only when the field's data_type is date or datetime. Follows the pattern ${AGEINDAYS}+<n> for records where the date field was exactly n days in the past, or ${DUEINDAYS}+<n> for records where the date field is exactly n days in the future. Supported comparators are equal, not_equal, less_than, greater_than, less_equal, and greater_equal.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`OrderingFilterCriterionRequest`:
  > Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the ordering filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['less_than', 'less_equal', 'greater_than', 'greater_equal']] — Represents the ordering comparison operator applied to the criterion.
Possible values:
less_than - Matches records where the field value is less than the specified filter value.
less_equal - Matches records where the field value is less than or equal to the specified filter value.
greater_than - Matches records where the field value is greater than the specified filter value.
greater_equal - Matches records where the field value is greater than or equal to the specified filter value.
  - `value` (object) **REQ** — Represents the scalar filter value used in the ordering comparator. Arrays and objects are not supported for ordering comparators.
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
`SetFilterCriterionRequest`:
  > Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
  - `field` (object) **REQ** — Represents the target field definition to which the set filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['in', 'not_in']] — Represents the set membership comparison operator applied to the criterion.
Possible values:
in - Matches records where the field value is in the specified set of values.
not_in - Matches records where the field value is not in the specified set of values.
  - `value` (array of object) [minItems=1, maxItems=500] **REQ** — Contains an array of primitive filter values used in the set comparison.
    oneOf:
      - `SimpleFilterCriterionValueString` (string) [maxLen=255] — Represents a string filter criterion value applicable to fields with a data_type of text, textarea, email, phone, website, autonumber, picklist, multiselectpicklist, date, or datetime, as well as any data_type not explicitly covered by SimpleFilterCriterionValueNumber, SimpleFilterCriterionValueBoolean, SimpleFilterCriterionValueObjectRequest, SimpleFilterCriterionValueObjectResponse, or the multiselect lookup value schemas.
      - `SimpleFilterCriterionValueNumber` (number) — Represents a numeric filter criterion value applicable to fields with a data_type of integer, currency, or double.
  - `type` (string) [enum=['merge_field', 'pre_defined', 'value', 'field'], default=value] — Indicates the value resolution mode of the criterion, distinguishing whether the filter value is a literal value, a merge field reference, a predefined system variable, or another field reference.
Possible values:
value - The value is a direct literal.
merge_field - The value is a merge field reference.
pre_defined - The value is a predefined system variable placeholder.
field - The value references another field.
`SimpleFilterCriterionRequest`:
  oneOf:
    - `EqualityFilterCriterionRequest` — Represents an equality filter criterion that dispatches to either the EqualFilterCriterionRequest or NotEqualFilterCriterionRequest schema based on the comparator value.
    - `TextFilterCriterionRequest` — Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
    - `OrderingFilterCriterionRequest` — Represents a filter criterion for the less_than, less_equal, greater_than, and greater_equal comparators. The value must be a scalar; arrays and objects are not supported. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `BetweenFilterCriterionRequest` — Represents a filter criterion for the between and not_between comparators. The value must be an array of exactly two elements — [lower_bound, upper_bound]. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for date or datetime fields, and SimpleFilterCriterionValueNumber for integer, currency, or double fields. Resolve the data_type from the field's FieldSchema. For formula fields, use formula.return_type as the effective data_type; for rollup_summary fields, use rollup_summary.return_type.
    - `SetFilterCriterionRequest` — Represents a filter criterion for the in and not_in comparators. The value must be an array of primitive values. The value type is determined by the field's data_type: use SimpleFilterCriterionValueString for text-based types, and SimpleFilterCriterionValueNumber for integer, currency, or double fields.
    - `MultiSelectLookupFilterCriterionRequest` — Represents a filter criterion for the include_all, include_any, exclude_all, and exclude_any comparators. Applicable only when the field's data_type is multiuserlookup or multiselectlookup. The value must be an array of SimpleFilterCriterionValueObjectRequest lookup objects.
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
`SimpleFilterCriterionValueObjectRequest`:
  > Represents the base minified record structure of a lookup module, containing the record's unique identifier and display name.
  - `id` (object) **REQ**
  - `name` (string) [maxLen=255] — Represents the display name of the lookup module record.
  additionalProperties: any
`TextFilterCriterionRequest`:
  > Represents a filter criterion for the like, not_like, starts_with, ends_with, contains, and not_contains comparators. The value must be a string scalar or array; use SimpleFilterCriterionValueString for text-based field types. Object and Boolean values are not supported. Resolve the data_type from the field's FieldSchema.
  - `field` (object) **REQ** — Represents the target field definition to which the text filter criterion is applied, conforming to the base field structure.
  - `comparator` (string) **REQ** [enum=['like', 'not_like', 'starts_with', 'ends_with', 'contains', 'not_contains']] — Represents the text comparison operator applied to the criterion.
Possible values:
like - Matches records where the field value contains the specified pattern.
not_like - Matches records where the field value does not contain the specified pattern.
starts_with - Matches records where the field value begins with the specified string.
ends_with - Matches records where the field value ends with the specified string.
contains - Matches records where the field value contains the specified string.
not_contains - Matches records where the field value does not contain the specified string.
  - `value` (object) **REQ** — Represents the string filter value used in the text comparator. Accepts a scalar string or an array of string values.
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

**Request Body** (required) — application/json
> The request body must contain a **territories** array. You can include a maximum of 100 territory objects per request.

  > Specify the territories to update.

  - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Specify the list of territories to update.

    - `manager` (object)
      oneOf:
          - `id` (string) **REQ** [maxLen=19] — Specify the unique ID of the user to assign as the manager of this territory.

          type: null [const=None] — Specify **null** to remove the manager from this territory.

    - `reporting_to` (object)
      oneOf:
          - `id` (string/int64) **REQ** — Specify the unique ID of the parent territory.

          type: null [const=None] — Specify **null** when this territory has no parent territory.

    - `permission_type` (string) [enum=['read_write_delete', 'read_only']] — Specify the permission type for the territory.
Possible values:
read_write_delete - Grants full access to the territory, including read, write, and delete operations.
read_only - Restricts users to read-only access for the territory.

    - `description` (string) [maxLen=250, nullable] — Specify the description of the territory.

    - `id` (string/int64) **REQ** — Specify the unique ID of the territory to update.

    - `name` (string) [maxLen=50] — Specify the name of the territory.

    - `account_rule_criteria` (object) — Specify the account rule criteria for the territory. Use a criteria object or a group criteria object to define the conditions. Set to **null** to remove the existing criteria.

      oneOf:
        - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
        - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
          type: null [const=None] — Represents a null value that removes the account rule criteria from the territory.

    - `deal_rule_criteria` (object) — Specify the deal rule criteria for the territory. Use a criteria object or a group criteria object to define the conditions. Set to **null** to remove the existing criteria.

      oneOf:
        - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
        - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
          type: null [const=None] — Represents a null value that removes the deal rule criteria from the territory.

    - `lead_rule_criteria` (object) — Specify the lead rule criteria for the territory. Use a criteria object or a group criteria object to define the conditions. Set to **null** to remove the existing criteria.

      oneOf:
        - `SimpleFilterCriterionRequest` — Represents a simple field-based filter criterion that dispatches to the appropriate comparator-specific schema. The equal and not_equal comparators support scalar or array values; text comparators support scalar or array strings; ordering comparators require a scalar; between and not_between comparators require a two-element array; in and not_in comparators require an array of primitives; and include_all, include_any, exclude_all, and exclude_any comparators require an array of lookup objects and apply only when the field's data_type is multiuserlookup or multiselectlookup.
        - `GroupedFilterCriterionRequest` — Represents a grouped filter criterion containing multiple filter conditions evaluated with a logical operator. Supports recursive nesting for complex filtering logic.
          type: null [const=None] — Represents a null value that removes the lead rule criteria from the territory.


**Responses:**

- **200**: Returns the result of the territory update for each territory in the **territories** array. The **code** field indicates **SUCCESS** for updated territories and **ERROR** for failures.
 — Schema: `TerritoryUpdateSuccessResponse` [application/json]
    > Represents the response returned when one or more territories are successfully updated.
    schema: `TerritoryUpdateSuccessResponse`
    - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects updated by the request.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the territory update. Possible values: **SUCCESS**.
      - `details` (object) **REQ** — Represents additional details about the updated territory, including its unique identifier.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the updated territory.
      - `message` (string) **REQ** [maxLen=100, enum=['Territory Updated Successfully']] — Represents the success message returned for the territory update. Possible values: **Territory Updated Successfully**.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the territory update operation. Possible values: **success**.

- **400**: The territory update request contains invalid or missing data.
**Resolution:** The territory IDs, required fields, and field values in the request body must be valid.
 [application/json]
    > Represents the error response for an invalid or failed territory update request.

    oneOf:
      - `InvalidData` — Represents the error response when a territory request contains invalid field data.
        - `territories` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of territory objects with their error details.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the territory error.
          - `details` (object) **REQ** — Represents additional details about the error.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that contains invalid data.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that contains invalid data.
          - `message` (string) **REQ** [enum=[15 values]] — Represents the error message describing the reason for this failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `InvalidDataWithSupportedValues` — Represents the error response when a field value is not valid, including the list of accepted values.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the territory error. Possible values: **INVALID_DATA**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field name, JSON path, and list of accepted values.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that contains an unsupported value.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field in the request body that contains an invalid value.
            - `supported_values` (array of string) [minItems=1, maxItems=10] **REQ** — Represents the list of accepted values for the field.
              items: [maxLen=100]
          - `message` (string) **REQ** [enum=['the given value is invalid', 'Given Permission_type value is invalid']] — Represents the error message returned when a field value is not among the accepted values. Possible values: **the given value is invalid**, **Given Permission_type value is invalid**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `DuplicateDataError` — Represents the error response when the request contains duplicate data for a territory field.
        - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects with their error details.
          - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code indicating the type of error for the territory operation.
          - `details` (object) **REQ** — Represents additional details about the error.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field that contains duplicate data.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field that contains duplicate data.
          - `message` (string) **REQ** [enum=['Given Territory name already exists', 'Duplicate Territory Name Found']] — Represents the error message describing the reason for this failure.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryParentNoPermission` — Represents the error response when the user does not have permission to use the specified territory as a parent.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with permission error details.
          - `code` (string) **REQ** [enum=['PERMISSION_DENIED']] — Represents the error code for the request. Possible values: **PERMISSION_DENIED**.
          - `details` (object) **REQ** — Represents additional details about the permission error.
          - `message` (string) **REQ** [enum=["Doesn't have a permission to choose that territory as a Parent Id"]] — Represents the error message returned when the user lacks permission to use the selected parent territory. Possible values: **Doesn't have a permission to choose that territory as a Parent Id**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `MandatoryNotFoundError` — Represents the error response when a mandatory field is missing from the territory request.
        - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the territory error. Possible values: **MANDATORY_NOT_FOUND**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field name and JSON path of the missing mandatory field.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the mandatory field that is missing from the request.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the mandatory field that is missing from the request body.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message returned when a required field is absent. Possible values: **required field not found**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `MandatoryNotFoundTerritoriesError` — Represents the error response when the mandatory territories field is missing from the request body.
        - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the territory error. Possible values: **MANDATORY_NOT_FOUND**.
        - `details` (object) **REQ** — Represents additional details about the error, including the field name and JSON path of the missing mandatory field.
          - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the mandatory field that is missing from the request.
          - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the mandatory field that is missing from the request body.
        - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message returned when a required field is absent. Possible values: **required field not found**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryMaxLimitExceededErrorSchemaForCriteria` — Represents the error response when the number of criteria conditions in the request exceeds the allowed maximum.
        - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects with criteria limit error details.
          - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code for the request. Possible values: **LIMIT_EXCEEDED**.
          - `details` (object) **REQ** — Represents additional details about the error, including the maximum criteria limit and the fields that exceeded it.
            - `limit` (integer/int32) **REQ** [min=1] — Represents the maximum number of criteria conditions allowed.
            - `limit_due_to` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of criteria fields that caused the limit to be exceeded.
              - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the criteria field that caused the limit to be exceeded.
              - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the criteria field that caused the limit to be exceeded.
          - `message` (string) **REQ** [maxLen=100, enum=['Maximum Territory Criteria Limit reached']] — Represents the error message returned when the territory criteria limit is exceeded. Possible values: **Maximum Territory Criteria Limit reached**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `InvalidDataWithMaximumLength` — Represents the error response when a field value exceeds the maximum allowed length.
        - `territories` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the territory error. Possible values: **INVALID_DATA**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field name, JSON path, and maximum allowed length.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field whose value exceeds the maximum allowed length.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field in the request body whose value exceeds the maximum allowed length.
            - `maximum_length` (integer/int32) **REQ** [min=1] — Represents the maximum number of characters allowed for the field.
          - `message` (string) **REQ** [enum=['invalid data', 'the value of the field exceeds the maximum allowed length']] — Represents the error message returned when a field value exceeds the maximum allowed length. Possible values: **invalid data**, **the value of the field exceeds the maximum allowed length**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `NotSupportedForCriteriaOnModuleDisable` — Represents the error response when a criteria field references a module that is disabled.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the territory error. Possible values: **NOT_ALLOWED**.
          - `details` (object) **REQ** — Represents additional details about the error, including the field name and JSON path associated with the disabled module.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field whose criteria cannot be set because the module is disabled.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path of the field in the request body that references the disabled module.
          - `message` (string) **REQ** [enum=[6 values]] — Represents the error message returned when criteria cannot be set for a disabled module. Possible values: **Unable to set rules criteria for disabled module**, **Lead Rule Disabled**, **Deal Rule Disabled**, **Territory Deal Rule Disabled**, **Territory Lead Rule Disabled**, **Inactive User**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryParentNoPermissionDetailed` — Represents the error response when the user does not have permission to use the specified territory as a parent, with detailed field-level context.
        - `territories` (array of object) [minItems=1, maxItems=10] **REQ** — Represents the list of territory objects with detailed permission error information.
          - `code` (string) **REQ** [enum=['PERMISSION_DENIED']] — Represents the error code for the request. Possible values: **PERMISSION_DENIED**.
          - `details` (object) **REQ** — Represents additional details about the permission error, including the field API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that caused the permission error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path pointing to the field that caused the permission error.
          - `message` (string) **REQ** [enum=[3 values]] — Represents the error message returned when the user lacks permission for the territory. Possible values: **Doesn't have a permission to choose that territory as a Parent Id**, **User does not have update/delete permission for the territory**, **User does not have permission to view/access the Territory**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `NotAllowedOrgTerritoryUpdate` — Represents the error response when updating the root organization territory is not permitted.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with error details.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the territory error. Possible values: **NOT_ALLOWED**.
          - `details` (object) **REQ** — Represents additional details about the error.
          - `message` (string) **REQ** [enum=[2 values]] — Represents the error message returned when the organization territory cannot be updated. Possible values: **Organization territory can only be updated**, **Cannot update the Org Territory except Name**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryReportingToChildError` — Represents the error response when the reporting_to territory ID is a child of the territory being updated, which would create a circular hierarchy.
        - `territories` (array of object) [minItems=1, maxItems=1] **REQ** — Represents the list of territory objects with child hierarchy error details.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the request. Possible values: **NOT_ALLOWED**.
          - `details` (object) **REQ** — Represents additional details about the hierarchy error, including the field API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=100, minLen=1] — Represents the API name of the field associated with the hierarchy validation error.
            - `json_path` (string) **REQ** [maxLen=250, minLen=1] — Represents the JSON path pointing to the field that caused the hierarchy error.
          - `message` (string) **REQ** [enum=[3 values]] — Represents the error message returned when the reporting_to territory is a child of the territory being updated. Possible values: **Reporting_to id should not be the child of given territory. Chosse another territory as Reporing_to**, **Org Territory cannot be deleted.**, **Territory can't be deleted as it's having child**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryUpdateDeleteNoPermission` — Represents the error response when the user does not have update or delete permission for the specified territory.
        - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects with update or delete permission error details.
          - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the request. Possible values: **NO_PERMISSION**.
          - `details` (object) **REQ** — Represents additional details about the permission error, including the field API name and JSON path.
            - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that caused the permission error.
            - `json_path` (string) **REQ** [maxLen=250] — Represents the JSON path pointing to the field that caused the permission error.
          - `message` (string) **REQ** [maxLen=100, enum=['User does not have update/delete permission for the territory']] — Represents the error message returned when the user lacks update or delete permission for the territory. Possible values: **User does not have update/delete permission for the territory**.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.
      - `TerritoryCriteriaError` — Represents the error response for criteria validation errors in territory operations, containing a territories array with criteria error items.
        - `territories` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the list of territory objects with criteria validation error details.
          oneOf:
            - `InvalidDataType` — Represents the error response returned when a criterion field value is provided with an incorrect data type. Contains the error code, a descriptive message, the response status, and details identifying the offending field and its expected data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code that identifies the category of validation failure.
Possible values:
INVALID_DATA - Indicates that the value provided for a criterion field does not match the expected data type.
              - `details` (object) **REQ** — Contains the details of the invalid data type error, including the API name of the offending criterion field, its JSON path within the request body, and the data type that was expected.
                - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the criterion field whose value was supplied with an invalid data type.
                - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path that locates the specific field within the request body where the invalid data type was detected.
                - `expected_data_type` (string) **REQ** [maxLen=256] — Represents the data type that the API expected for the criterion field identified by the API name, against which the supplied value was validated.
              - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the invalid data type failure in a form suitable for display or logging.
              - `status` (string) **REQ** [enum=['error']] — Represents the response status for this error response.
Possible values:
error - Indicates that the request failed due to an invalid data type on a criterion field.
            - `FieldComparatorValueMissing` — Represents the error response returned when a criterion comparator cannot be applied because the comparator value supplied by the dependee field is absent. Carries error code DEPENDENT_FIELD_MISSING along with details identifying both the field in error and the dependee field whose value is missing.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code that identifies the category of failure for this error response.
Possible values:
DEPENDENT_FIELD_MISSING - Indicates that the comparator value required from the dependee criterion field is absent, preventing the comparator from being evaluated.
              - `details` (object) **REQ** — Contains detailed information about the criterion field that caused the error and the dependee field whose comparator value is missing, including the API name and JSON path for each.
                - `dependee` (object) **REQ** — Represents the dependee criterion field — that is, the field whose value determines what the current comparator accepts — and whose missing comparator value triggered this error. Contains the API name and JSON path of that dependee field.
                  - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the dependee criterion field whose comparator value is absent and caused the evaluation failure.
                  - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path that locates the dependee criterion field within the request body, identifying where the missing comparator value was expected.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field that triggered the DEPENDENT_FIELD_MISSING error.
                - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field in error within the request body.
              - `message` (string) **REQ** [maxLen=512] — Error message describing the DEPENDENT_FIELD_MISSING condition returned in the response envelope.
              - `status` (string) **REQ** [enum=['error']] — Status of the response. Possible values: error.
            - `FieldComparatorMismatch` — Error schema returned when the comparator value supplied for a criterion field does not match the valid comparator values determined by its dependee field. Contains the error code DEPENDENT_MISMATCH and a details object identifying the criterion field, its dependee field, and the list of supported comparator values.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code identifying the type of field comparator mismatch condition. Possible values: DEPENDENT_MISMATCH.
              - `details` (object) **REQ** — Detailed information about the field comparator mismatch, including the API name and JSON path of the criterion field in error, the dependee field that governs valid comparator values, and the array of supported comparator values.
                - `dependee` (object) **REQ** — The dependee field whose value determines which comparator values are valid for the criterion field that raised the DEPENDENT_MISMATCH error. Contains the API name and JSON path of the dependee field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field that determines the valid comparator values for the criterion field in error.
                  - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the criterion field whose comparator value does not match any of the supported values determined by the dependee field.
                - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path locating the criterion field whose comparator value does not match any of the supported values determined by the dependee field.
                - `supported_values` (array of string) [minItems=1, maxItems=100] **REQ** — Contains the comparator values that are valid for the criterion field, as determined by the dependee field.
                  items: [maxLen=256]
              - `message` (string) **REQ** [maxLen=512] — Represents the error message describing the comparator mismatch condition for the criterion field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: error.
            - `FieldValueMismatch` — Represents the error response returned when the data type of the value supplied for a criterion field does not match the expected data type determined by the dependee field. Returned with error code DEPENDENT_MISMATCH. Contains details identifying the mismatched criterion field, its dependee field, and the expected data type.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code identifying the type of error condition encountered. Possible values: DEPENDENT_MISMATCH.
              - `details` (object) **REQ** — Contains detailed information about the data type mismatch, including the criterion field that raised the error, the dependee field whose value determines the expected data type, and the expected data type itself.
                - `dependee` (object) **REQ** — Represents the dependee field whose value determines the expected data type for the criterion field that raised the mismatch error. Contains the API name and JSON path of the dependee field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field that determines the expected data type for the criterion field in error.
                  - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field whose value does not match the expected data type.
                - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field whose value contains the data type mismatch.
                - `expected_data_type` (string) **REQ** [maxLen=256] — Data type expected for the criterion field value, as determined by the dependee field.
              - `message` (string) **REQ** [maxLen=512] — Descriptive message providing details about the field value mismatch error.
              - `status` (string) **REQ** [enum=['error']] — Status of the response. Possible values: error.
            - `ComparatorValueMismatch` — Error schema returned when the comparator value itself does not satisfy the dependency validation rules imposed by the dependee field. Carries error code DEPENDENT_MISMATCH and includes details identifying the criterion field with the invalid comparator value, its dependee field (api_name, json_path), and the criterion field own api_name and json_path.
              - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Error code identifying the comparator dependency mismatch condition. Possible values: DEPENDENT_MISMATCH.
              - `details` (object) **REQ** — Object containing diagnostic detail about the dependency mismatch, including the criterion field with the invalid comparator value (api_name, json_path) and the dependee field that imposed the violated validation rule (dependee.api_name, dependee.json_path).
                - `dependee` (object) **REQ** — Identifies the dependee field whose value determines the validation rules applied to the comparator of the criterion field in error. Contains the API name and JSON path of the dependee field.
                  - `api_name` (string) **REQ** [maxLen=256] — API name of the dependee field whose value imposed the violated validation rule on the criterion field comparator.
                  - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the dependee field within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field whose comparator value does not satisfy the dependency rule imposed by the dependee field.
                - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field with the invalid comparator value within the request body.
              - `message` (string) **REQ** [maxLen=512] — Descriptive message providing details about the comparator value mismatch error.
              - `status` (string) **REQ** [enum=['error']] — Status of the response indicating the outcome of the request. Possible values: error.
            - `InvalidComparator` — Error schema returned when the comparator specified in a criterion field is not one of the allowed comparator values for the given field type. Returned with error code INVALID_DATA. The details object identifies the offending field by API name and JSON path, and enumerates the supported comparator values.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code identifying the category of error. Possible values: INVALID_DATA.
              - `details` (object) **REQ** — Contains structured information about the invalid comparator error. Identifies the offending criterion field by API name and JSON path, and provides the list of supported comparator values valid for the given field type.
                - `api_name` (string) **REQ** [maxLen=256] — API name of the criterion field for which an invalid comparator was specified.
                - `json_path` (string) **REQ** [maxLen=512] — JSON path locating the criterion field with the invalid comparator within the request body.
                - `supported_values` (array of string) [minItems=1, maxItems=100] **REQ** — Contains the comparator values that are valid for the criterion field type.
                  items: [maxLen=256]
              - `message` (string) **REQ** [maxLen=512] — Descriptive error message conveying the nature of the invalid comparator condition to the caller.
              - `status` (string) **REQ** [enum=['error']] — Status of the response indicating the outcome of the request. Possible values: error.
            - `LookupLimitExceeded` — Represents the error response returned when the count of lookup fields used in criterion expressions exceeds the allowed limit. The error code is LOOKUP_LIMIT_EXCEEDED. The details object contains a used_in array (minItems: 1, maxItems: 10) in which each entry identifies an affected location by name and provides the relevant lookup fields and the applicable lookup limit.
              - `code` (string) **REQ** [enum=['LOOKUP_LIMIT_EXCEEDED']] — Identifies the error code that signals the lookup field limit has been exceeded. Possible values: LOOKUP_LIMIT_EXCEEDED.
              - `details` (object) **REQ** — Provides structured information about the locations where the lookup field count exceeded the allowed limit. The required used_in array contains objects that each specify a location name (such as "criteria" or "cross_filters"), the lookup fields in use, and the applicable lookup limit.
                - `used_in` (array of object) [minItems=1, maxItems=10] **REQ** — Lists the locations (for example, "criteria" or "cross_filters") where lookup field usage exceeded the allowed limit. Each entry in the array contains a location name, the lookup fields involved, and the applicable lookup limit. The array contains between 1 and 10 items.
                  - `name` (string) **REQ** [maxLen=256] — Identifies the location — such as criteria or cross_filters — where the lookup field count exceeded the allowed limit.
                  - `lookup_fields` (array of object) [minItems=1, maxItems=100] **REQ** — Lists the lookup fields present in the specified location that contributed to exceeding the allowed lookup field limit. Contains between 1 and 100 entries, each identifying a single lookup field by its API name.
                    - `api_name` (string) **REQ** [maxLen=256] — Specifies the API name of a lookup field that was counted against the lookup field limit for the specified location.
                  - `lookup_limit` (integer/int32) **REQ** — Specifies the maximum number of lookup fields permitted in the associated location, such as criteria or cross_filters.
              - `message` (string) **REQ** [maxLen=512] — Contains a descriptive error message explaining why the lookup field limit was exceeded.
              - `status` (string) **REQ** [enum=['error']] — Indicates the outcome of the request. Possible values: error.
            - `NotSupportedApiName` — Represents the error response returned when the API name specified in a criterion field is not supported by the target module. Contains the error code, a descriptive message, the response status, and details identifying the unsupported field and its location in the request body.
              - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Represents the error code that identifies the category of validation failure.
Possible values:
NOT_SUPPORTED - Indicates that the API name specified for the criterion field is not supported by the target module.
              - `details` (object) **REQ** — Contains detailed information identifying the criterion field whose API name is not supported by the target module, including the field API name and its location within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the criterion field that is not supported by the target module.
                - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path that locates the unsupported criterion field within the request body.
              - `message` (string) **REQ** [maxLen=512] — Represents the error message describing why the criterion field API name is not supported by the target module.
              - `status` (string) **REQ** [enum=['error']] — Represents the outcome status of the response for this error condition.
Possible values:
error - Indicates the request failed because the specified criterion field API name is not supported by the target module.
              - `code` (string) **REQ** [const=INVALID_DATA] — Represents the error code for the request.
              - `details` (object) **REQ** — Represents additional details about the error, including the field API name, JSON path, and supported values.
                - `api_name` (string) **REQ** [maxLen=256] — Represents the API name of the field with invalid data.
                - `json_path` (string) **REQ** [maxLen=512] — Represents the JSON path pointing to the field with invalid data.
                - `supported_values` (array of string) [minItems=1, maxItems=10] — Represents the list of valid values supported for the field.
                  items: [maxLen=100]
              - `message` (string) **REQ** [enum=[6 values]] — Represents the error message returned when the criteria data is invalid. Possible values: **the given value is invalid**, **the given filter value is invalid**, **invalid data**, **The given api_name seems to be invalid**, **The given comparator seems to be invalid**, **Please give a valid comparator**.
              - `status` (string) **REQ** [const=error] — Represents the status of the operation. Possible values: **error**.
            - `FieldNotSupportedInCriteria` — Represents the error response returned when a criterion field type is not supported in filter criteria. Field types such as file upload and image upload cannot be used as filter criteria fields. The error code is INVALID_DATA. The details object identifies the unsupported field via its api_name and json_path.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Indicates the classification of the error returned by the API.

Possible values:
INVALID_DATA - The request contains a criterion field whose type is not supported in filter criteria.
              - `details` (object) **REQ** — Contains detailed information identifying the unsupported criterion field. The api_name property specifies the API name of the offending field, and the json_path property locates it within the request body.
                - `api_name` (string) **REQ** [maxLen=256] — Specifies the API name of the criterion field whose type is not supported in filter criteria.
                - `json_path` (string) **REQ** [maxLen=512] — Specifies the JSON path that locates the unsupported criterion field within the request body.
              - `message` (string) **REQ** [enum=['The given field api_name is not supported in criteria']] — Provides a fixed descriptive message identifying the unsupported criterion field.

Possible values:
"The given field api_name is not supported in criteria" - Indicates that the field identified by api_name cannot be used in filter criteria.
              - `status` (string) **REQ** [enum=['error']] — Indicates the outcome status of the API response.

Possible values:
error - The request failed because the specified criterion field type is not supported in filter criteria.
      - `TerritoryFeatureNotEnabledError` — Represents the error response when the territory feature is not enabled for the organization.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED']] — Represents the error code for the request. Possible values: **FEATURE_NOT_ENABLED**.
        - `details` (object) **REQ** — Represents additional details about the error.
        - `message` (string) **REQ** [maxLen=100, enum=[5 values]] — Represents the error message returned when the territory feature is not enabled for the organization. Possible values: **Territory Management is disabled**, **Territory Management is not enabled**, **Territory Management Disabled**, **the territory feature is not enabled for Leads Module**, **Territory Management is not enabled for Leads Module**.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

- **401**: Authentication failure due to missing, expired, or invalid OAuth token.
**Resolution:** A new access token must be generated with the required scope for this API.
 — Schema: `UnauthorizedError` [application/json]
    > Represents the error response when authentication fails for the request.
    schema: `UnauthorizedError`
    - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the request. Possible values: **AUTHENTICATION_FAILURE**.
    - `details` (object) **REQ** — Represents additional details about the authentication error.
    - `message` (string) **REQ** [maxLen=100, enum=['Authentication failed']] — Represents the error message returned when authentication fails. Possible values: **Authentication failed**.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the operation. Possible values: **error**.

**Scopes:** ZohoCRM.settings.territories.UPDATE
