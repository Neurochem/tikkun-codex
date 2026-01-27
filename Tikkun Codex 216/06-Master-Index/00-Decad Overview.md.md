
```dataview
TABLE WITHOUT ID
  file.link AS "Chapter",
  "Ch. " + chapter AS "№",
  "Decad " + decad AS "Decad",
  title AS "Title"
FROM "01-Chapters"
SORT file.name ASC