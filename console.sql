
select * from schedule where doc_id = 4;


select time(time) from schedule where date='2021-03-06' and doc_id = 4;


select cast(time AS date),cast(time AS Time) from schedule;

select schedule_id, doc_id, date, time, status from schedule where doc_id = 4 and date = '2021-03-06'