-- Discussion 10 Quiz
-- To run (Ubuntu / OS X Yosemite +): sqlite3 < quiz10.sql
-- Windows / OS X Mavericks -: ./sqlite3 < quiz10.sql

-- Example table for Q1
create table numbers as
  select 0 as idx, 5 as n union
  select 1, 9 union
  select 2, 1 union
  select 3, -2 union
  select 4, 6 union
  select 5, -5 union
  select 6, 1 union
  select 7, 5 union
  select 8, -8 union
  select 9, 5 union
  select 10, 14 union
  select 11, 3 union
  select 12, -30 union
  select 13, -2 union
  select 14, 83 union
  select 15, 17;

-- Q1 solution
-- Expected output: 3 6 9 14 17 83
select 'Q1'; select '---';
select n from numbers
  group by n having n > 0 and count(n) = 1;

-- Q2 solution
-- Expected output: 233 89 55 21 13 5 3 1 1
select ''; select 'Q2'; select '---';
with
  fibonacci (prev, curr) as (
    select 0, 1 union
    select curr, prev + curr from fibonacci where prev + curr < 333
  )
select curr from fibonacci where curr % 2 != 0 order by -curr;

-- Example table for Q3
-- There are many more songs I could have added to this
create table good_songs as
  select 'Drops of Jupiter' as song, 'Train' as artist, 'Drops of Jupiter' as album, 2001 as year_released union
  select 'The Great Pumpkin Waltz', 'Vince Guaraldi', 'A Charlie Brown Christmas', 1965 union
  select 'Satisfied', 'Renée Elise Goldsberry', 'Hamilton', 2015 union
  select 'Cmon Talk', 'Bernhoft', 'Solidarity Breaks', 2011 union
  select 'dummy_song1', 'Bernhoft', 'dummy_album1', 2011 union
  select 'Man in the Mirror', 'Michael Jackson', 'Bad', 1987 union
  select 'Eight Days a Week', 'The Beatles', 'Beatles for Sale', 1964 union
  select 'dummy_song1', 'The Beatles', 'dummy_album1', 1964 union
  select 'dummy_song2', 'The Beatles', 'dummy_album2', 1964 union
  select 'dummy_song3', 'The Beatles', 'dummy_album3', 1964 union -- this should count
  select 'My Stupid Mouth', 'John Mayer', 'Room for Squares', 2001 union
  select 'Breakable', 'Ingrid Michaelson', 'Girls and Boys', 2006 union
  select 'Mr. Jones', 'Counting Crows', 'August and Everything After', 1993 union
  select 'Kame Sennin / Peace Gangster Stardust', 'Vagabond Maurice', 'Stray Sessions', 2015 union
  select 'dummy_song1', 'Vagabond Maurice', 'dummy_album1', 2015 union
  select 'dummy_song2', 'Vagabond Maurice', 'dummy_album2', 2015 union -- this should count
  select 'Drive', 'Incubus', 'Make Yourself', 1999 union
  select 'Beautiful Pain', 'Eminem', 'The Marshall Mathers LP 2', 2013 union
  select 'Already Home', 'A Great Big World', 'Is There Anybody Out There?', 2014 union
  select 'Saturdays', 'Holly Brook', 'Like Blood Like Honey', 2006 union
  select 'No Role Modelz', 'J. Cole', '2014 Forest Hills Drive', 2014 union
  select 'dummy_song1', 'J. Cole', 'dummy_album1', 1 union
  select 'dummy_song2', 'J. Cole', 'dummy_album2', 2 union
  select 'Daylight', 'Matt and Kim', 'Grand', 2009 union
  select 'dummy_song1', 'Matt and Kim', 'dummy_album1', 2009 union
  select 'dummy_song2', 'Matt and Kim', 'dummy_album2', 2 union
  select 'Remember the Name', 'Fort Minor', 'The Rising Tied', 2005;

-- Q3 solution
-- Expected output: The Beatles and Vagabond Maurice
-- By SO: "group by X, Y means put all those with the same values for both X and Y in one group"
select ''; select 'Q3'; select '---';
select artist from good_songs group by artist, year_released having count(*) > 2;
