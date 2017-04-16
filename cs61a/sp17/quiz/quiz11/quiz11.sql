-- Discussion 11 Quiz
-- To run (Ubuntu / macOS Yosemite+): sqlite3 < quiz11.sql
-- Windows / macOS Mavericks-: ./sqlite3 < quiz11.sql

-- Q1 solution
-- Expected output: 1 3 9 27 81 243 729 2187 6561
select 'Q1'; select '---';
with threes(pwr) as (
  select 1 union
  select pwr * 3 from threes where pwr <= 2187
)
select pwr from threes;

-- Q2 solution
-- Expected output: acst acts asct astc ...
-- Do try to figure this one out on your own! It's very cool.
select ''; select 'Q2'; select '---';
with given(char, weight) as (
  select 'c',    1 union
  select 'a',   10 union
  select 't',  100 union
  select 's', 1000
) 
select a.char || b.char || c.char || d.char
from given as a, given as b, given as c, given as d
where a.weight + b.weight + c.weight + d.weight = 1111;
