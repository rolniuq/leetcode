select eni.unique_id, e.name
from  Employees e
left join EmployeeUNI eni on e.id = eni.id
