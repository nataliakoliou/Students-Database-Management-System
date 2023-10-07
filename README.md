# Students Database Management System
This project aims to build a Students Database Management System, which provides various endpoints for managing student data effectively. The system is implemented using Python with Flask for the backend and MongoDB as the database. 

## Introduction
In this report, we will provide a detailed walkthrough of the steps involved in running the `students-app.py` file. To accomplish this, we will use the Linux terminal and the Postman application. Our process will begin with the setup of a virtual machine, followed by the activation of Docker and the MongoDB database using the following commands:

```bash
sudo systemctl enable docker --now
sudo docker start mongodb
```
We will then execute the Python file, students-app.py, along with a debugger, accessible at http://0.0.0.0:5000/. For your convenience, we recommend creating nine JSON files that can be imported into Postman. You can find a list of these JSON files in the [json-endpoints.txt](https://github.com/nataliakoliou/Students-Database-Management-System/blob/main/json-endpoints.txt) file in this repository. Copy and paste the endpoints from the file to quickly set up your requests in Postman.

## 1st Endpoint | User creation
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/createUser](http://0.0.0.0:5000/createUser).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the `endpoint1.json` file to the system.
5. Once the file is uploaded, click "Send" to get the response.

**Code Explanation:**
The system checks if there are any existing users in the Users collection using the `count_documents()` function. If it returns 0, the username and password entered in the data using `data = json.loads(request.data)` are stored in the user dictionary. This user dictionary is then added to the Users collection, and a success message is sent to the user. If the username and password you're trying to add already exist in the Users collection, you'll receive a corresponding failure message.

## 2nd Endpoint | System login
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/createUser](http://0.0.0.0:5000/login).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the `endpoint2.json` file to the system.
5. Once the file is uploaded, click "Send" to get the response.

**Code Explanation:**
The system checks if there are users in the Users collection with the username and password you provided in the Postman request Body. If it finds a matching user, it triggers the `create_session()` function to authenticate the user. You'll receive a dictionary containing the user's unique identifier (UUID) and username. If the requested user isn't found, you'll get an error message.

## 3rd Endpoint | Get student by email

1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/getStudent](http://0.0.0.0:5000/getStudent).
3. In the request body section, choose the "raw" option to specify that you're sending JSON data.
4. Select "binary" and click "Select File" to upload the `endpoint3.json` file to the system.
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy the UUID (user unique identifier) and paste it into the Authorization field.
7. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `users_sessions` by calling the `is_session_valid()` function. If it gets a positive response, it proceeds to check if there's a user in the Students collection with the email provided through Postman. If such a user is found, their details are returned through the `student_d1` dictionary. Since the `Students.json` file may contain users who have declared their home address and those who haven't, the `student_d1` dictionary can take two forms: one including the "address" field and one without it. In case the UUID is invalid or the email doesn't correspond to a student, an error message is returned.

## 4th Endpoint | Get all students who are exactly 30 years old
1. Open Postman and select the GET request method.
2. 2. Enter the following URL: [http://0.0.0.0:5000/getStudents/thirties](http://0.0.0.0:5000/getStudents/thirties).
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy the UUID (user unique identifier) and paste it into the Authorization field.
4. Leave the Body field empty.
7. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system checks if your UUID in the Authorization field is valid by calling the is_session_valid() function. If it's valid, it looks for students aged 30 in the current year. It calculates their birth year (e.g., 1991 for 2021) and stores it as yearMinus30. Then, it checks the Students collection for students in this age group. If any are found, their details are printed using the student_l1 list. To create this list, it goes through each 30-year-old student, stores their information in a dictionary called student_d2, and adds it to the students_l1 list. It's important to note that because the Students.json file may have users with or without address information, the student_d2 dictionary can have two forms – one with the address field and one without. If the UUID is invalid or the email doesn't belong to a 30-year-old student, it returns an error message.

## 5th Endpoint | Get all students who are at least 30 years old
1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/getStudents/oldies](http://0.0.0.0:5000/getStudents/oldies).
3. In the Headers section, add a new header named "Authorization."
4. After successfully logging in as a user, copy your UUID (user unique identifier) and paste it into the Authorization field.
5. Leave the Body field empty.
6. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system first checks if the UUID in the Authorization field exists in the users_session by using the is_session_valid() function. If it's valid, it proceeds to find students who are at least 30 years old in the current year. To do this, it calculates their birth year (e.g., 1991 for 2021) and stores it as yearMinus30. Then, it searches the Students collection for students in this age group. If any are found, their details are printed using the student_l2 list. To create this list, the system iterates through each student who is 30 years old or older, stores their information in a dictionary named student_d3, and adds it to the students_l2 list. It's important to note that because the Students.json file may contain users with or without address information, the student_d3 dictionary can take two forms – one with the address field and one without. If the UUID is invalid or the email doesn't belong to a student who is at least 30 years old, it returns an error message.

## 6th Endpoint | Get students who have declared residence based on email
1. Open Postman and select the GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/getStudentAddress](http://0.0.0.0:5000/getStudentAddress).
3. In the Body section, choose "raw" to specify that the input type will be JSON.
4. Click "Binary" and then "Select File" to upload the endpoint6.json file.
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy the UUID (User Unique Identifier) and paste it into the Authorization field.
7. Leave the Body field empty.
8. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system first checks if the UUID in the Authorization field exists in the users_session by calling the is_session_valid() function. If it gets a positive response, it proceeds to check if there is a user in the Students collection with the email received via Postman. Additionally, it ensures that this user has also provided their address information. If such a user is found, the system returns their name, street, and postal code as per the student_d4 dictionary.

## 7th Endpoint | Delete student by email
1. Open Postman and select the DELETE request method.
2. Enter the following URL: [http://0.0.0.0:5000/deleteStudent](http://0.0.0.0:5000/deleteStudent).
3. In the Body section, select the "raw" input type and specify JSON.
4. Click "binary," then "Select File" to upload the endpoint7.json file.
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy your UUID (Unique User Identifier) and paste it into the Authorization field.
7. Click the "Send" button to execute the request.

**Code Explanation:**
The system first checks the validity of your UUID in the Authorization field by calling the is_session_valid() function. If it's valid, the system proceeds to check if there is a user in the Students collection with the email provided in Postman. If such a user is found, they are completely removed from the Students collection using the students.delete_one({"email": data["email"]}) command. If the UUID is invalid, the email doesn't correspond to a student, or the email exists in the Students collection but belongs to a student who hasn't provided an address, an error message is returned.



> # Υλοποίηση του 8ου Endpoint | Εισαγωγή μαθημάτων σε φοιτητή βάσει email
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την PATCH request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/addCourses. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint8.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει χρήστης στην συλλογή Students με το email που έλαβε μέσω Postman. Αν πράγματι βρεθεί ένας τέτοιος χρήστης, τότε εισάγεται στα στοιχεία του το πεδίο courses με τα μαθήματα που λαμβάνει το σύστημα μέσω της εντολής json.loads(request.data). Σκοπός μας είναι να εκτυπωθούν με τρόπο ευδιάκριτο, γι' αυτό και τα αποθηκεύουμε ένα ένα μέσα σε μια λίστα που ονομάζουμε courses_l. Τα δεδομένα αυτής της λίστας περνάνε έπειτα στην μεταβλητή student με την εντολή student.update({"courses":courses_l}) σε μορφή dictionary (ακριβώς όπως υπάρχουν στο JSON αρχείο). Έτσι το σύστημα εκτυπώνει τα στοιχεία του μαθητή με το τρέχον email, αφού πρώτα τα εισάγει στο λεξικό student_d5. Επειδή το Students.json αρχείο μας περιέχει χρήστες που έχουν δηλώσει τα στοιχεία κατοικίας τους, αλλά και χρήστες που έχουν κενό αυτό το πεδίο, πρέπει το λεξικό student_d5 να λαμβάνει δύο μορφές: η πρώτη θα περιλαμβάνει το πεδίο address ενώ η δεύτερη δε θα το περιλαμβάνει. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον μαθητή, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 9ου Endpoint | Επιστροφή περασμένων μαθημάτων φοιτητή βάσει email
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/getPassedCourses. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint9.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει χρήστης στην συλλογή Students με το email που έλαβε μέσω Postman, που να έχει συμπληρωμένο το πεδίο courses στην συλλογή Students. Αν πράγματι βρεθεί ένας τέτοιος χρήστης, τότε εξάγονται ως λεξικό τα μαθήματα στα οποία εξετάστηκε και αξιολογήθηκε με προβιβάσιμο βαθμό (βαθμός μεγαλύτερος ή και ίσως του 5). Το λεξικό αυτό ονομάζεται passed και δημιουργείται μέσω της εντολής passed.update(course_d) | το course_d το κάθε ζεύγος course-grade που θέλουμε να εισαχθεί στο λεξικό. Στο τέλος, το σύστημα εκτυπώνει το όνομα του μαθητή και τα μαθήματα που έχει περάσει, μέσω ενός λεξικού που ονομάζουμε student_d6. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον μαθητή, ή ο μαθητής δεν έχει εξεταστεί σε κανένα μάθημα επιστρέφεται μήνυμα λάθους. Αντίστοιχα αν ο μαθητής εξετάστηκε αλλά κόπηκε σε όλα τα μαθήματα, εμφανίζεται το ανάλογο ενημερωτικό μήνυμα.
