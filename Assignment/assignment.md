#### Query Based questions:

1. Insert the given data ( data is present inside data.json file ), to **"details"** collection, inside
   your **"Employees"** database. Make sure you are using python to insert the data. Do commit this python
   file in your repository.

2. After inserting all the documents -> display all the documents.
   2.1 Using find()
   2.2 Using aggregate()

3. Display the fields --> name, salary, marital status and company of all the documents. ( Make sure no 
   other fields should be displayed apart from the above mentioned fields. )

4. Display **only** the **name** field of all the documents which are from Norway.

5. Display all the documents in descending order which have salary greater than equal to 3500.

6. Find all the documents which are from New Zealand and are married.

7. Display the names and salary of top 10 documents with least amount of salary.

8. Find all the documents whihc have "Inc" in their company's name. ( Make sure that your query is not 
   not taking much time to run. ) 

9. Count the total number of documents living in each country.

10. Find a document whose name is "Kirsten Jensen", and update his name to "CoreStack".

11. Delete the document with then name "CoreStack".

12. Display countries in ascending order, according to the earnings of each country. 
    For eg: People of China might earn $10000 and People of India might earn $20000 -- (sum of the salaries of all the people living in China and India respectively. So, the output should be -
    China $10000
    India $20000 )

#### Theory Based questions:

13. What do you understand by profiling. What is the command for setting up level 2 profile.

14. If your query is running slow, then how can you improve it's performance. How will you find
    whether your query is running slow or not.

15. What do you understand by aggregation pipeline. Why is [] (empty array) needed in aggregate() 
    function.