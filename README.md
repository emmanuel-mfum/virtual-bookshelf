# virtual-bookshelf
Full-stack app that allows the user to save book titles and their ratings on a database.

Despite the minimal front-end, this app allows the user to save titles with a SQLite database.

SQLite allows us to treat entries in the database as objects, where the table kept in the database is like a class and
the columns of the table (fields) are the properties of objects (entries).

We use this paradigm to create a Model for our database, just like we would create a class in Python.

![image](https://user-images.githubusercontent.com/55893421/116580226-29f59380-a8e1-11eb-889c-e08770e2f4a6.png)

In this app, we provide multiple routes:

1.Home Route  
2.Add Route  
3.Edit Route
4.Delete Route

Each of these routes can be tied to the basic operations performed on database (aka CRUD).

The home route will read all the Book entries inside our database and will send them to be rendered in the "index.html" file.
The add route  (which leads to an HTML form) will use the data sent by this form via a POST request to create a new entry in 
the database. The user is then redirected to the home route, which will display this new entry. 
This route can be reach vis a button on the home page.

The edit route can be reached via a button on the homepage. It leads also to a form, and the data from that form will be used to
update an already exisiting entry in the database. We know which entry to update as the id of the Book entry is passed to the server
as a query parameter.

Finally, the delete route is reached via a button on the homepage. Clicking on this button will simply send the id of the current Book entry
to our server and there using that id, we will delete the entry with the corresponding id in the database.

We also have to take note that ids are automatically generated for entries when we create them in the database.

Essential for the completion of this project was the use of CRUD operations with SQLite. Examples for learning can be found in the comments of 
the "main.py" file.

In the comments can also be found some code I wrote just to be famliar with SQLite, the code that is tied to the "books-collection.db"

Home page
![image](https://user-images.githubusercontent.com/55893421/116583694-a047c500-a8e4-11eb-882e-4c92c93923ae.png)

Edit page
![image](https://user-images.githubusercontent.com/55893421/116583743-ac338700-a8e4-11eb-9581-2e4a69c02172.png)

Add page
![image](https://user-images.githubusercontent.com/55893421/116583777-b5245880-a8e4-11eb-96fa-efcce7c921f5.png)



