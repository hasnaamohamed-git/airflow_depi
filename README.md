# Airflow_Depi

## Description
This Airflow DAG contains three simple tasks to demonstrate basic operator usage and task dependencies.

## Tasks
1. **Print Current Date** – Uses `BashOperator` to print the current system date.  
2. **Print Welcome Message** – Uses `PythonOperator` to print a welcome message with the author’s name.  
3. **Generate Random Number** – Uses `PythonOperator` to generate a random number and save it to `/tmp/random.txt`.

## Task Flow
print_date → print_welcome → generate_random_number
<img width="1366" height="768" alt="Screenshot (551)" src="https://github.com/user-attachments/assets/a6fb7f72-004e-47f1-a41b-940a75f5407e" />
