H2 Database Journey from SQL String to Execution
---

# Contents  
- [H2 Database Journey from SQL String to Execution](#h2-database-journey-from-sql-string-to-execution)  
  - [H2 Code Structure](#h2-code-structure)  
    - [Command](#1-command)  
    - [Query](#2-query)  
    - [Select](#3-select)  
    - [Prepared](#4-prepared)  
    - [CommandContainer](#5-commandcontainer)  
    - [Relationships](#relationships)  
    - [Execution Flow](#execution-flow)  
    - [Quick Reference TLDR](#quick-reference-tldr)  
- [Tokenization and Parsing](#tokenization-and-parsing)  
- [Query Planning](#query-planning)  
- [Optimization](#optimization)  
- [Execution](#execution)  
- [Planning vs. Optimization: Difference](#planning-vs-optimization-difference)  
- [High Level Flow TLDR](#tldr)  
- [Relational Algebra Implementation in H2](#relational-algebra-implementation-in-h2)  
  - [Key RelOp Operations in H2](#key-relop-operations-in-h2)  
    - [Table Scan](#1-table-scan)  
    - [Index Scan](#2-index-scan)  
    - [Predicate Evaluation (Filter)](#3-predicate-evaluation-filter)  
    - [Projection](#4-projection)  
    - [Join](#5-join)  
    - [Aggregation](#6-aggregation)  
    - [Sorting](#7-sorting)  
    - [Union](#8-union)  
    - [Difference](#9-difference)  
    - [Intersection](#10-intersection)  
  - [Relationship Between RelOp and Relational Algebra](#relationship-between-relop-and-relational-algebra)  
  - [How RelOp Operations Work Together](#how-relop-operations-work-together)  
- [Walking the RELOP Tree](#walking-the-relop-tree)  
  - [Code Locations](#code-locations)  
  - [Key Observations](#key-observations)  

---

# H2 Database Journey from SQL String to Execution  

## H2 Code Structure  

In the H2 database codebase, **Command**, **Query**, **Select**, **Prepared**, and **CommandContainer** are key components involved in the lifecycle of a SQL query. These classes are part of the pipeline that processes SQL commands from parsing to execution. To see the code flow in your debugger run H2 in server mode and set a breakpoint in  `process()`  method in `TcpServerThread.java`.

--- 
### **1. Command**
- **Purpose**: Represents a high-level SQL command.
- **Role**: The entry point for SQL queries after parsing.
- **Features**:
  - Acts as an abstract class with specific implementations for different SQL statements (e.g., `Select`, `Update`, `Insert`).
  - Each SQL command corresponds to a subclass of `Command`
  - Manages metadata, execution lifecycle, and connection context.

- **Key Code**:
  - Located in `Command.java`.
  - Subclasses include `CommandConatiner`, `CommandConatinerList`, `CreateTable`, `ListTable`

---

### **2. Query**
- **Purpose**: Represents SQL queries (e.g., SELECT statements).
- **Role**: A specific type of `Prepared` statement focused on reading data.
- **Features**:
  - Implements logic to handle SELECT statements and some types of subqueries.
  - Serves as a base for handling complex SELECT queries.
  - Optimized for read-heavy operations.
  - Operates on `ResultSet` objects to return results.

- **Key Code**:
  - Located in `Query.java`.
  - Implements the `executeQuery()` method to return rows from the database.

---

### **3. Select**
- **Purpose**: Represents the AST for a SELECT statement.
- **Role**: A subcomponent of the `Query` class, responsible for managing the structure of SELECT operations.
- **Features**:
  - Contains the logic for SELECT clauses, including projections (columns), WHERE clauses, GROUP BY, and HAVING.
  - Implements relational operations like filtering and grouping.
  - Works with `TableFilter` to handle table scans and joins.

- **Key Code**:
  - Located in `Select.java`.
  - Core methods like `addCondition()` and `addGroupBy()` build the relational structure.

---

### **4. Prepared**
- **Purpose**: Represents a prepared SQL statement.
- **Role**: The bridge between the parsed SQL command and its execution plan.
- **Features**:
  - Abstracts query planning and validation.
  - Acts as a parent class for specific commands (like `Query`).
  - Includes logic to optimize and execute the query.

- **Key Code**:
  - Located in `Prepared.java`.
  - Common base class for executable SQL statements, like `Insert`, `Update`, `Delete`, and `Query`.

---

### **5. CommandContainer**
- **Purpose**: Wraps a `Prepared` statement for execution.
- **Role**: Provides an interface to execute the SQL commands.
- **Features**:
  - Serves as a wrapper to handle the lifecycle of `Prepared` statements.
  - Manages execution state, caching, and resource cleanup.

- **Key Code**:
  - Located in `CommandContainer.java`.
  - Acts as a bridge between client-facing SQL execution and the backend logic.

---

### **Relationships**
1. **Command**:
   - High-level representation of SQL commands.

2. **Prepared**:
   - Represents the parsed and validated query, ready for planning and execution.
   - Base class for executable statements like `Query`.

3. **Query**:
   - Subclass of `Prepared` specifically for SELECT queries.
   - Handles read operations and result set generation.

4. **Select**:
   - Represents the SELECT-specific AST and logic.
   - Operates within a `Query` to implement SELECT-related functionality.

5. **CommandContainer**:
   - Wraps the `Prepared` object for execution.
   - Manages caching and lifecycle for `Prepared` statements.

---

### **Execution Flow**
1. A SQL string is parsed in the SessionLocal (each connection has a session), via `PrepareLocal()`
2. The `Command` object is created by `prepareLocal()` owned by `Parser`
3. `Parser` parses to get an "unprepared" `Prepared` object, that it then "prepares" this is where it will conver to Relop Tree and do optimizations. By leveraging the overridden methods the opmtiomizations can be found in each specific Prepared Concrete Class like `Select`, ans `SelectUnion`
4. The `CommandContainer` wraps the `Prepared` statement for execution, managing caching and cleanup.
5. Execution occurs, and the result is returned to the client.

---

### **Quick Reference TLDR**
- **Command**: High-level SQL command interface.
- **Query**: Specialized class for SELECT statements, subclass of `Prepared`.
- **Select**: Encapsulates the SELECT-specific AST and relational logic.
- **Prepared**: Base class for all parsed, validated, and executable statements.
- **CommandContainer**: Wrapper for `Prepared` to manage execution and caching.

______


## Query Planning
Query planning involves converting the parsed AST into an intermediate representation, such as a **Relational Operation (RelOp) Tree**. The RelOp tree mirrors the structure of relational algebra, which allows the database engine to reason about the query's execution.

### Key Processes:
- **AST Transformation**: The `Command` object is transformed into a tree of `Query` and `TableFilter` nodes.
- **Access Path Selection**: Determines which indexes or table scans to use for retrieving data.
- **Binding and Validation**: Ensures all columns, tables, and functions referenced in the query exist and are correctly typed.

### Relevant Code:
- **Transformation**: `Query.java` and `Select.java`
  - These classes are responsible for interpreting the AST and creating an execution plan structure.
- **Table Filtering**: `TableFilter.java`
  - Represents a node in the execution plan tree and manages table access logic.

### Output:
- The output is an initial **execution plan**, represented as a RelOp tree.

---

## **Optimization**

Optimization refines the initial execution plan to improve performance by applying various techniques like predicate pushdown, join reordering, and index selection.

### Key Processes:
- **Predicate Pushdown**: Moves filter conditions (WHERE clauses) closer to the data source to minimize intermediate results.
- **Join Reordering**: Changes the order of table joins to reduce the cost of intermediate computations.
- **Index Selection**: Chooses appropriate indexes for efficient data access.
- **Cost-Based Analysis**: Estimates the cost of different execution strategies and selects the most efficient one.

### Relevant Code:
- **Optimization**: `Optimizer.java`
  - This class performs the bulk of optimization by analyzing the query structure and applying transformations.
- **Cost Evaluation**: `TableFilter.java` (methods like `getBestPlanItem()`)
  - Evaluates the cost of accessing data using different indexes or table scans.

### Output:
- The optimized **execution plan**, which is ready for execution.

---

## **Execution**
The execution stage traverses the optimized execution plan and executes it against the underlying storage engine. It retrieves results by evaluating the relational operations specified in the plan.

### Key Processes:
- **Relational Operations**: Each node in the RelOp tree corresponds to a relational algebra operation (e.g., SELECT, JOIN).
- **Row Iteration**: Executes the operations and streams rows back to the client.

---

## **Planning vs. Optimization: Differenece**

- **Planning**:
  - Transforms the parsed query into an **initial execution plan** (RelOp tree).
  - Focuses on correctness, ensuring that the plan accurately reflects the query semantics.

- **Optimization**:
  - Refines the initial execution plan to improve performance.
  - Applies cost-based analysis and heuristics to choose the most efficient strategy for executing the query.

### Relationship:
- **Planning** creates the baseline representation of the query.
- **Optimization** improves upon this baseline by considering performance factors.

---

## **TLDR**
1. **Parsing**: Converts SQL into an AST (`Command` object).  
2. **Planning**: Builds an initial execution plan (RelOp tree).  
3. **Optimization**: Refines the execution plan for efficiency.  
4. **Execution**: Executes the optimized plan and returns results.

___________________

## Relational Algebra Implementation in H2

In the H2 database, the **RelOp operations** (relational operators) represent logical and physical operations used in query execution. These operations are derived from **relational algebra** and are implemented in the codebase to execute SQL queries efficiently.

---

### **Relationship Between RelOp and Relational Algebra**
H2's RelOp tree is based on the concepts of relational algebra, and these operations map closely to algebraic counterparts. For example:
- **Selection (σ)**: Implemented as filters (`TableFilter`).
- **Projection (π)**: Handled by column selection in `Select` + `TableFilter`.
- **Join (⨝)**: Represented explicitly in the `Join` class.
- **Set Operations (∪, −, ∩)**: Managed by `SelectUnion`.

---

### **How RelOp Operations Work Together**
1. **Parsing Stage**: SQL is parsed into an AST.
2. **Planning Stage**: The AST is transformed into a RelOp tree, where each node represents one of these operations.
3. **Execution Stage**: The RelOp tree is traversed, and operations are executed in sequence or parallel where applicable.

---

### **Relevant Code in H2**
- **`TableFilter`**: Handles table scans and index scans.
- **`Select`**: Manages SELECT queries, including projection, filtering, and sorting.
- **`TableFilter + Parser`**: Implements join logic and optimization.
- **`SelectUnion`**: Implements union, intersection, and difference operations.
- **`Optimizer`**: Refines the RelOp tree to make execution more efficient.

---

### **Summary**
The RelOp operations in H2 implement key relational algebra concepts like selection, projection, join, and set operations. These are fundamental to the query execution pipeline and ensure that SQL queries can be executed efficiently while adhering to the relational model.

______________________________________________

## Walking the RELOP Tree

In the H2 database, the RelOp tree is traversed during query optimization and execution phases. This traversal is performed to plan and execute the query efficiently. The code components that walk the RelOp tree include:

### **Walking the RelOp Tree for Execution**

#### **Component**: `ResultInterface` and Iterators  
- **Purpose**: Executes the query by traversing the RelOp tree nodes and fetching data iteratively.
- **Key Classes**:
  - **`TableFilter`**:
    - Represents a table or index scan operation.
    - Has methods like `next()` to fetch the next row during execution.
  - **`Query` and `Select`**:
    - Execute the relational operations by calling iterators like `getIterator()` on child nodes (e.g., filters or joins).
  - **`Join`**:
    - Handles join operations by iterating over child nodes (left and right tables) and combining rows.

#### **Execution Workflow**:
1. **`Command.executeQuery()`**:
   - Initiates the query execution.
2. **`Query.query()`**:
   - Walks the relational tree to execute operations in the correct sequence.
3. **Node Traversal**:
   - Iterators like `TableFilter.next()` are used to fetch rows and combine results.


---

### **Code Locations**
**Execution**:
   - `Query.execute()` in `Query.java`
   - `TableFilter.next()` in `TableFilter.java`

---

### **Key Observations**
- The RelOp tree traversal is split into **optimization** and **execution** stages.
- **Optimization** modifies the tree for efficiency, while **execution** walks the tree iteratively to fetch and process data.
- Classes like `Select`, and `TableFilter` handle traversal specific to their relational roles.