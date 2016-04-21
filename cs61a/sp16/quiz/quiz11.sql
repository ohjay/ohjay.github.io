CREATE TABLE tblA AS
  SELECT 1 AS col1, "A" AS col2 UNION
  SELECT 2, "B";

CREATE TABLE tblB AS
  SELECT 1 AS col1, "Z" AS col2 UNION
  SELECT 2, "Y" UNION
  SELECT 3, "Y";

-- Q1(a)
SELECT "Q1(a) ---";
SELECT col2 FROM tblB;

-- Q1(b)
SELECT "";
SELECT "Q1(b) ---";
SELECT col1 FROM tblA, tblB;

-- Q1(c)
SELECT "";
SELECT "Q1(c) ---";
SELECT tblA.col1, tblA.col2, tblB.col1, tblB.col2
  FROM tblA, tblB;

-- Q1(d)
SELECT "";
SELECT "Q1(d) ---";
SELECT tblA.col1, tblA.col2, tblB.col2
  FROM tblA, tblB
  WHERE tblA.col1 = tblB.col1;
