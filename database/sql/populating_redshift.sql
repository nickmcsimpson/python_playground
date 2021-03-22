-- POPULATING REDSHIFT:

--  Learning the Copy Command
copy dimproduct
--optional column list, ordinal by default
from 's3://pimpsonsbucket/dimproduct.csv' -- specify a data source
iam_role 'arn:aws:iam::227967283010:role/RedshiftS3' -- authorization, several ways
region 'us-west-2'
-- format, and additional options
;

select * from dimproduct;