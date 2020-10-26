# Photo Storage Documentation

Photos are stored in their own database table. This table contains a user column
to indicate which user it belongs to.

## Photo Table

Defined in [`src/ledger/LedgerHeaderUtils.cpp`](/src/ledger/LedgerHeaderUtils.cpp)

Equivalent to _LedgerHeader_

Field | Type | Description
------|------|---------------
id | CHARACTER(64) PRIMARY KEY | Unique Id, primary Key
uid | CHARACTER(64) NOT NULL | User Id, foreign Key from users table
s3 | CHARACTER(64) NOT NULL | Path to file on Amazon S3
date | TEXT NOT NULL | Upload Date
