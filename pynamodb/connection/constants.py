"""
Pynamodb constants
"""

# Operations
BATCH_WRITE_ITEM = 'BatchWriteItem'
DESCRIBE_TABLE = 'DescribeTable'
BATCH_GET_ITEM = 'BatchGetItem'
CREATE_TABLE = 'CreateTable'
UPDATE_TABLE = 'UpdateTable'
DELETE_TABLE = 'DeleteTable'
LIST_TABLES = 'ListTables'
UPDATE_ITEM = 'UpdateItem'
DELETE_ITEM = 'DeleteItem'
GET_ITEM = 'GetItem'
PUT_ITEM = 'PutItem'
QUERY = 'Query'
SCAN = 'Scan'

# Request Parameters
RETURN_ITEM_COLL_METRICS = 'ReturnItemCollectionMetrics'
RETURN_CONSUMED_CAPACITY = 'ReturnConsumedCapacity'
EXCLUSIVE_START_KEY = 'ExclusiveStartKey'
COMPARISON_OPERATOR = 'ComparisonOperator'
SCAN_INDEX_FORWARD = 'ScanIndexForward'
ATTR_DEFINITIONS = 'AttributeDefinitions'
ATTR_VALUE_LIST = 'AttributeValueList'
CONSISTENT_READ = 'ConsistentRead'
DELETE_REQUEST = 'DeleteRequest'
RETURN_VALUES = 'ReturnValues'
REQUEST_ITEMS = 'RequestItems'
ATTRS_TO_GET = 'AttributesToGet'
ATTR_UPDATES = 'AttributeUpdates'
SCAN_FILTER = 'ScanFilter'
TABLE_NAME = 'TableName'
KEY_SCHEMA = 'KeySchema'
ATTR_NAME = 'AttributeName'
ATTR_TYPE = 'AttributeType'
PUT_REQUEST = 'PutRequest'
INDEX_NAME = 'IndexName'
TABLE_KEY = 'Table'
KEY_TYPE = 'KeyType'
ACTION = 'Action'
EXISTS = 'Exists'
SELECT = 'Select'
LIMIT = 'Limit'
RANGE = 'RANGE'
HASH = 'HASH'
ITEM = 'Item'
KEYS = 'Keys'
UTC = 'UTC'
KEY = 'Key'

# Defaults
DEFAULT_REGION = 'us-east-1'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f%z'
SERVICE_NAME = 'dynamodb'
HTTP_OK = 200

# Create Table arguments
PROVISIONED_THROUGHPUT = 'ProvisionedThroughput'
READ_CAPACITY_UNITS = 'ReadCapacityUnits'
WRITE_CAPACITY_UNITS = 'WriteCapacityUnits'
STRING = 'String'
NUMBER = 'Number'
BINARY = 'Binary'

# Constants needed for creating indexes
LOCAL_SECONDARY_INDEXES = 'LocalSecondaryIndexes'
GLOBAL_SECONDARY_INDEXES = 'GlobalSecondaryIndexes'
PROJECTION = 'Projection'
PROJECTION_TYPE = 'ProjectionType'
NON_KEY_ATTRIBUTES = 'NonKeyAttributes'


# These are constants used in the KeyConditions parameter
# See: http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html#DDB-Query-request-KeyConditions
BEGINS_WITH = 'BEGINS_WITH'
BETWEEN = 'BETWEEN'
EQ = 'EQ'
NE = 'NE'
LE = 'LE'
LT = 'LT'
GE = 'GE'
GT = 'GT'
IN = 'IN'
KEY_CONDITIONS = 'KeyConditions'
COMPARISON_OPERATOR_VALUES = [EQ, LE, LT, GE, GT, BEGINS_WITH, BETWEEN]

# These are the valid select values for the Scan operation
# See: http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html#DDB-Scan-request-Select
NOT_NULL = 'NOT_NULL'
NULL = 'NULL'
CONTAINS = 'CONTAINS'
NOT_CONTAINS = 'NOT_CONTAINS'
ALL_ATTRIBUTES = 'ALL_ATTRIBUTES'
ALL_PROJECTED_ATTRIBUTES = 'ALL_PROJECTED_ATTRIBUTES'
SPECIFIC_ATTRIBUTES = 'SPECIFIC_ATTRIBUTES'
COUNT = 'COUNT'
SELECT_VALUES = [ALL_ATTRIBUTES, ALL_PROJECTED_ATTRIBUTES, SPECIFIC_ATTRIBUTES, COUNT]

# These are the valid comparison operators for the Scan operation
# See: http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html#DDB-Scan-request-ScanFilter
SEGMENT = 'Segment'
TOTAL_SEGMENTS = 'TotalSegments'
SCAN_FILTER_VALUES = [EQ, NE, LE, LT, GE, GT, NOT_NULL, NULL, CONTAINS, NOT_CONTAINS, BEGINS_WITH, IN, BETWEEN]

# These are constants used in the expected condition for PutItem
# See: http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html#DDB-PutItem-request-Expected
VALUE = 'Value'
EXPECTED = 'Expected'

# These are the valid ReturnConsumedCapacity values used in multiple operations
# See: http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchGetItem.html#DDB-BatchGetItem-request-ReturnConsumedCapacity
INDEXES = 'INDEXES'
TOTAL = 'TOTAL'
NONE = 'NONE'
RETURN_CONSUMED_CAPACITY_VALUES = [INDEXES, TOTAL, NONE]

# These are the valid ReturnItemCollectionMetrics values used in multiple operations
# See: http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html#DDB-BatchWriteItem-request-ReturnItemCollectionMetrics
SIZE = 'SIZE'
RETURN_ITEM_COLL_METRICS_VALUES = [SIZE, NONE]

# These are the valid ReturnValues values used in the PutItem operation
# See: http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html#DDB-PutItem-request-ReturnValues
ALL_OLD = 'ALL_OLD'
UPDATED_OLD = 'UPDATED_OLD'
ALL_NEW = 'ALL_NEW'
UPDATED_NEW = 'UPDATED_NEW'
RETURN_VALUES_VALUES = [NONE, ALL_OLD, UPDATED_OLD, ALL_NEW, UPDATED_NEW]

# These are constants used in the AttributeUpdates parameter for UpdateItem
# See: http://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html#DDB-UpdateItem-request-AttributeUpdates
PUT = 'PUT'
DELETE = 'DELETE'
ADD = 'ADD'
ATTR_UPDATE_ACTIONS = [PUT, DELETE, ADD]
