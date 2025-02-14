# Write your MySQL query statement below

select r.customer_id, COUNT(customer_id) AS count_no_trans 
from (
    select transaction_id, customer_id
    from visits v
    left join Transactions t on t.visit_id = v.visit_id
) r
where r.transaction_id is null
group by r.customer_id

