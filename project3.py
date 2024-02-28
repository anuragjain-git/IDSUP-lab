salaries_and_tenures = [(83000, 8), (88000, 8),(48000, 1), (76000, 6),(69000, 6), 
                        (76000, 7), (60000, 2), (83000, 10),(48000, 2), (63000, 4), 
                        (52000,1),(85000,8),(71000,5),(80000,7)]


from collections import defaultdict

salary_by_tenure=defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
    
print(salary_by_tenure)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenures, salaries in salary_by_tenure.items()}
print(average_salary_by_tenure)

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif  tenure < 5:
        return "between two and five"
    else:
        return"More than five"
    
for salary, tenure in salaries_and_tenures:
    bucket =tenure_bucket(tenure)
    salary_by_tenure[bucket].append(salary)
    
