---
category: stealth
title: Lab 12&#58; SQL
---

## SQL
### Big Ideas (stolen from Eric Pai)
- **SQL** is a query language for databases. The idea is that queries (filtering, ordering, parsing information, getting aggregate statistics, etc...) are similar, so people have written query engines and a Stuctured Query Language (SQL) for actually making queries.
- SQL allows us to store data and write queries to **describe what kind of data we want** rather than _code to implement the computation._
- In SQL, we represent data in _tables_, where each object of the table is stored as a _row_ that may have multiple _columns_ representing data.
  - `select` creates a new table
  - anatomy of a `select`: `SELECT [columns] FROM [tables] WHERE [condition] ORDER BY [criteria] LIMIT [limit] ...;`
    - `SELECT [columns]`: which columns to include in your new table
    - `FROM [tables]`: which tables to pull data from
    - `WHERE [condition]`: filter rows that satisfy a condition
    - `ORDER BY [criteria]`: order the rows in the output by a certain criteria
    - `LIMIT [limit]`: limit the number of rows in the output
  - using `*` as `columns` will select all columns in the table
  - specifying multiple tables to pull from will create a **join**: every possible combination of rows from the two tables
  - order is `ASCENDING` by default
  - whitespace and capitalization of keywords doesn't matter (e.g. `select` and `SELECT` mean the same thing)
