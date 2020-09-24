Quiz site

This site uses Pandas in order to read an Excel file, extract results from it and interact with a website, so Pandas and Flask are requirements.

What the site does:
-By modifying the Quiz.xlsx file, you can have as many questions and character results as you like as long as the answer is True or False.
-The first line will define the character's name (and the image that should be used in the static/images folder. Current accepted format is .png
-The second line adds a description that can be customized for when you get the specified character's result (should be a description of the character or its attributes)
-From the third line to the last, everything is considered a question and characters should have "T" or "F" in their respective columns.