# Chapter 2 Data Models and Query

- Data models shape how we break down our thinking for building an application.


## Relational
- The relational model was a theoretical proposal, and many people at the time doubted whether it could be implemented efficiently. However, by the mid-1980s, relational database management systems (RDBMSes) and SQL had become the tools of choice for most people who needed to store and query data with some kind of regular structure. The dominance of relational databases has lasted around 25‒30 years—an eternity in computing history.

- The roots of relational databases lie in business data processing, which was performed on mainframe computers in the 1960s and ’70s. The use cases appear mundane from today’s perspective: typically transaction processing (entering sales or banking transactions, airline reservations, stock-keeping in warehouses) and batch processing (customer invoicing, payroll, reporting).
Other databases at that time forced application developers to think a lot about the internal representation of the data in the database. The goal of the relational model was to hide that implementation detail behind a cleaner interface.

- Often optimizing on how much memory is being used, versus documents are often sacrificing more space for more straightforward retrieval paths.

## Document Model
- Oversimplification alert -> We can say document model is just key value with the value being a hierarchial format (json for comsosdb, bson for mongo, xml for IBM's IMS, etc).

## Nosql isnt really one thing...

- it was originally intended simply as a catchy Twitter hashtag for a meetup on open source, distributed, nonrelational databases in 2009. A number of interesting database systems are now associated with the #NoSQL hashtag, and it has been retroactively reinterpreted as Not Only SQL.
- Key val stores, document databases, funny enough depending on who you ask Graphs may or may not fall in Nosql

## Mismatch between OOP and The Relational Model
- Most application development today is done in object-oriented programming languages, which leads to a common criticism of the SQL data model: if data is stored in relational tables, an awkward translation layer is required between the objects in the application code and the database model of tables, rows, and columns. The disconnect between the models is sometimes called an impedance mismatch.
- Object-relational mapping (ORM) frameworks like ActiveRecord and Hibernate reduce the amount of boilerplate code required for this translation layer, but they can’t completely hide the differences between the two models.

## Normalizing and Denormalizing
- data normalization is the process of organizing data to reduce redundancy and improve data integrity. The goal is to minimize duplicate data by dividing data into tables based on relationships and ensuring each table serves a specific purpose. Normalization typically follows a series of "normal forms," such as First Normal Form (1NF), Second Normal Form (2NF), and Third Normal Form (3NF), each addressing specific types of redundancy or anomalies. For example, 1NF eliminates repeating groups, while 3NF ensures that all columns depend only on the primary key.
- Denormalization, on the other hand, is the process of merging tables and intentionally introducing redundancy for performance benefits. This can improve read performance by reducing the need for complex joins at the expense of additional storage and potential update anomalies. Denormalization is often used in read-heavy systems or where performance is critical, such as in analytical databases or specific use cases in NoSQL systems.

### Above definition tailors the situation to a relational model. 
- normalizing this data requires many-to-one relationships (many people live in one particular region, many people work in one particular industry), which don’t fit nicely into the document model. In relational databases, it’s normal to refer to rows in other tables by ID, because joins are easy. In document databases, joins are not needed for one-to-many tree structures, and support for joins is often weak.

If the database itself does not support joins, you have to emulate a join in application code by making multiple queries to the database. (In this case, the lists of regions and industries are probably small and slow-changing enough that the application can simply keep them in memory. But nevertheless, the work of making the join is shifted from the database to the application code.)

Moreover, even if the initial version of an application fits well in a join-free document model, data has a tendency of becoming more interconnected as features are added to applications.

## Importance and role of Query Optimizers in Relational Model
- Declartive syntaxes let someone more aware of disk layout and costs of operations perform the imperative steps for you. That someone is the query optimizer.
- the relational model lays out all the data in the open: a relation (table) is simply a collection of tuples (rows), and that’s it. There are no labyrinthine nested structures, no complicated access paths to follow if you want to look at the data. You can read any or all of the rows in a table, selecting those that match an arbitrary condition. You can read a particular row by designating some columns as a key and matching on those. You can insert a new row into any table without worrying about foreign key relationships to and from other tables.iv
In a relational database, the query optimizer automatically decides which parts of the query to execute in which order, and which indexes to use. Those choices are effectively the “access path,” but the big difference is that they are made automatically by the query optimizer, not by the application developer, so we rarely need to think about them.
If you want to query your data in new ways, you can just declare a new index, and queries will automatically use whichever indexes are most appropriate. You don’t need to change your queries to take advantage of a new index. (See also “Query Languages for Data”.) The relational model thus made it much easier to add new features to applications.
Query optimizers for relational databases are complicated beasts, and they have consumed many years of research and development effort [18]. But a key insight of the relational model was this: you only need to build a query optimizer once, and then all applications that use the database can benefit from it. If you don’t have a query optimizer, it’s easier to handcode the access paths for a particular query than to write a general-purpose optimizer—but the general-purpose solution wins in the long run.

## Relational to Document translation
- One to many -> use embedding. Put data in an array in your document or Create reference fields and have application code do the extra fetches. (pros and cons -> discuss doc size limitation, extra network and disk IO costs).
- Many to many -> use denormalization (pros and cons *updates becoming harder to maintain), join table by hand (application code complexity).

## Data locality
- Fetching document if you need most of the fields means lesser disk IO, versus multiple (often random) disk seeks in relational databases to different tables.
- Underlying data structure dictates locality: Write heavy nosql systems popular DS is LSM tree (mem table (commonly a binary tree)is kept in mem and then flushed as sstables on disk when past a certain threshold, and does compactions, dels are tombstoned, and writes are faster because we write to disk sequential).
Relational databases commonly use BTree or B+trees with pages on disk which involves alot of pointer based lookup, not sequential in nature. faster reads, slower writes is a common occurrence.
- Everyone tries to keep disk IO sequenetial regardless, but LSM trees by nature end up keeping IO sequential even when the structures keep changing.

## Schema and Flexibility (why we want it, and why we hate it)
- Schema on READ vs Schema on Write
- A more accurate term is schema-on-read (the structure of the data is implicit, and only interpreted when the data is read), in contrast with schema-on-write (the traditional approach of relational databases, where the schema is explicit and the database ensures all written data conforms to it) [21].
Schema-on-read is similar to dynamic (runtime) type checking in programming languages, whereas schema-on-write is similar to static (compile-time) type checking. Just as the advocates of static and dynamic type checking have big debates about their relative merits [22], enforcement of schemas in database is a contentious topic, and in general there’s no right or wrong answer.
- In a document database, you would just start writing new documents with the new fields and have code in the application that handles the case when old documents are read
- On the other hand, in a “statically typed” database schema, you would typically perform a migration. Schema changes have a bad reputation of being slow and requiring downtime. This reputation is not entirely deserved: most relational database systems execute the ALTER TABLE statement in a few milliseconds. MySQL is a notable exception—it copies the entire table on ALTER TABLE, which can mean minutes or even hours of downtime when altering a large table—although various tools exist to work around this limitation. Running the UPDATE statement on a large table is likely to be slow on any database, since every row needs to be rewritten. If that is not acceptable, the application can leave first_name set to its default of NULL and fill it in at read time, like it would with a document database.
- The schema-on-read approach is advantageous if the items in the collection don’t all have the same structure for some reason (i.e., the data is heterogeneous)—for example, because:
There are many different types of objects, and it is not practicable to put each type of object in its own table.
The structure of the data is determined by external systems over which you have no control and which may change at any time.
In situations like these, a schema may hurt more than it helps, and schemaless documents can be a much more natural data model. But in cases where all records are expected to have the same structure


## Convergence
- Both models are picking each others strengths
- Example mongodb provides a layer that lets the db driver resolve external collections's references for you, as well as add constraints to document's schemas.
- Postgresql lets you make a field json
- Mongodb has 