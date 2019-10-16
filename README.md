# flask_db_gui
Resuming project once I get a better understanding of Flask and browser based applications. I am learning more about browser extensions and multiple pages and links. The database as it stands now does not update "added students" to the website on Ubuntu, but it does on Windows. Will debugg when more knowledge of flask is attained.

This program is a browser based app that adds students to a database. The app builds a database and allows 
manipulation of the students Objects.
To this point the app runs, adds a student, but I have to trouble shoot some bugs with the additional 
database implementation features.

A student class is created and stored in its own file 

![student_class](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_student_def.png)


A flask app is created to execute the brower when the program is run.

![flask_def](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_flask_file.png)


![flask_exec](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_main.png)


A Html template with CSS features is used to add asthetics to the browser site. Not all code is shown to save space.

![html_template_directory](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_template_directory.png)

![html_screenshots](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_htlm0.png)

![html_screenshot2](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_html1.png)

Another file intergrates the front end to the student class.

![write_toFile0](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_write_toFile0.png)

This portion is responsible for taking in fields from the browser and using the input to create a student object. The object parameters are written to a txt file.

![write_toFile1](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_write_toFile2.png)

The text file is used to retrieve previously created objects and displaying them on the browser.

![write_toFile2](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_write_toFile.png)

The front page of the website looks like this. The different tabs are implemented to add extended functionality that I intend down the road.

![website_main](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_website_main.png)

This is how the student fileds are presented and filled in.

![fields_empty](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_website_student_fieldsEmpty.png)

![fields_filled](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_student_fields.png)

Finally the student will be added(currently debugging).

![student_added](https://github.com/r0meroh/flask_db_gui/blob/master/images/flask_db_website_student_added.png)




