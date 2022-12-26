====================================
------------INTRODUCTION------------
====================================
In this project I built a website for librarians.
The website is divided into pages.
On the home page(index.html) they will be able to see pictures of the books that exist in the library.
On the books page, they will be able to see the following details about each book: the name of the book, ID, author, year of publication and the type of book
In addition, they will be able to search for a book, add a book, update a book and delete a book.
On the customers page, they will be able to see the following details about each customer: the customer's name, their ID, age, and their city.
In addition, they will be able to search for a customer, add a customer, update a customer and delete a customer.
On the page of the loans, they will be able to see the following details about the whole question: the name of the customer, the name of the book, the date of the loan and the expected return date.
In addition, they will be able to see the questions from others, update the question, delete the question and return the question.

====================================
---------------PYTHON---------------
====================================
I imported the necessary packages to build the project in Flask.
I connected my server with the database.
I defined a class for each table and connected the tables using an P.key.
Then, I created a 'CRUD' for each of the tables.
Finally, I created an entry point that will run the program.

====================================
----------------HTML----------------
====================================
I created an index page which is my homepage, and another 3 HTML pages for each of the topics: books, customers and loans. 
Each page has a design that I imported from an external Siasas file, each page has a regular bar that I imported from Botstrap. 
In addition to each of the pages there is the same title and favicon that leads back to the site's homepage.

====================================
-------------JAVASCRIPT-------------
====================================
I created all my functions, to each category I created a functions page separately and imported the file into the HTML page.
I connect my server and then created the following functions according to the CRUD methods: 
1.function that shows the data,
2.function that adds data,
3.function updating data,
4.function that delete data.
In addition, for each category I have created a few more functions that are specially suitable for it.

ENJOY!