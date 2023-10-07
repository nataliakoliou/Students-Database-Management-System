# Students Database Management System
This project aims to build a Students Database Management System, which provides various endpoints for managing student data effectively. The system is implemented using Python with Flask for the backend and MongoDB as the database. 

## Introduction
In this report, we will provide a detailed walkthrough of the steps involved in running the `students-app.py` file. To accomplish this, we will use the Linux terminal and the Postman application. Our process will begin with the setup of a virtual machine, followed by the activation of Docker and the MongoDB database using the following commands:

```bash
sudo systemctl enable docker --now
sudo docker start mongodb
```
We will then execute the Python file, students-app.py, along with a debugger, accessible at http://0.0.0.0:5000/. For your convenience, we recommend creating nine JSON files that can be imported into Postman. You can find a list of these JSON files in the [json-endpoints.txt](https://github.com/nataliakoliou/Students-Database-Management-System/blob/main/json-endpoints.txt) file in this repository. Copy and paste the endpoints from the file to quickly set up your requests in Postman.

## 1st Endpoint | User Creation
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/createUser](http://0.0.0.0:5000/createUser).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the `endpoint1.json` file to the system.
5. Once the file is uploaded, click "Send" to get the response.

**Code Explanation:**
The system checks if there are any existing users in the Users collection using the `count_documents()` function. If it returns 0, the username and password entered in the data using `data = json.loads(request.data)` are stored in the user dictionary. This user dictionary is then added to the Users collection, and a success message is sent to the user. If the username and password you're trying to add already exist in the Users collection, you'll receive a corresponding failure message.

## 2nd Endpoint | System Login
1. Open Postman and select the POST request method.
2. Enter the following URL: [http://0.0.0.0:5000/createUser](http://0.0.0.0:5000/login).
3. In the request Body, choose the "raw" option to specify that you are importing a JSON file.
4. Select "binary" and click "Select File" to upload the `endpoint2.json` file to the system.
5. Once the file is uploaded, click "Send" to get the response.

**Code Explanation:**
The system checks if there are users in the Users collection with the username and password you provided in the Postman request Body. If it finds a matching user, it triggers the `create_session()` function to authenticate the user. You'll receive a dictionary containing the user's unique identifier (UUID) and username. If the requested user isn't found, you'll get an error message.

## 3rd Endpoint | Retrieve Student by Email

1. Open Postman and select the HTTP GET request method.
2. Enter the following URL: [http://0.0.0.0:5000/getStudent](http://0.0.0.0:5000/getStudent).
3. In the request body section, choose the "raw" option to specify that you're sending JSON data.
4. Select the "binary" option and click "Select File" to upload the `endpoint3.json` file to the system.
5. In the Headers section, add a new header named "Authorization."
6. After successfully logging in as a user, copy the UUID (user unique identifier) and paste it into the Authorization field.
7. Click the "Send" button to initiate the request and receive the response.

**Code Explanation:**
The system checks if the UUID in the Authorization field exists in the `users_sessions` by calling the `is_session_valid()` function. If it gets a positive response, it proceeds to check if there's a user in the Students collection with the email provided through Postman. If such a user is found, their details are returned through the `student_d1` dictionary. Since the `Students.json` file may contain users who have declared their home address and those who haven't, the `student_d1` dictionary can take two forms: one including the "address" field and one without it. In case the UUID is invalid or the email doesn't correspond to a student, an error message is returned.





> # Υλοποίηση του 3ου Endpoint | Επιστροφή φοιτητή βάσει email
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/getStudent. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint3.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει χρήστης στην συλλογή Students με το email που έλαβε μέσω Postman. Αν πράγματι βρεθεί ένας τέτοιος χρήστης, τότε επιστρέφονται τα στοιχεία του μέσω του λεξικού student_d1. Επειδή το Students.json αρχείο μας περιέχει χρήστες που έχουν δηλώσει τα στοιχεία κατοικίας τους, αλλά και χρήστες που έχουν κενό αυτό το πεδίο, πρέπει το λεξικό student_d1 να λαμβάνει δύο μορφές: η πρώτη θα περιλαμβάνει το πεδίο address ενώ η δεύτερη δε θα το περιλαμβάνει. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον μαθητή, επιστρέφεται μήνυμα λάθους.



> # Υλοποίηση του 4ου Endpoint | Επιστροφή όλων των φοιτητών που είναι 30 ετών
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/getStudents/thirties. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Προσοχή: δεν εισάγουμε τίποτα στο πεδίο Body. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχουν μαθητές που είναι 30 ετών το τρέχον έτος. Υπολογίζει στην ουσία την τιμή date.today().year-30 και την αποθηκεύει στην μεταβλητή yearMinus30. Πρόκειται απλώς για ένα νούμερο που δηλώνει το έτος γέννησης των 30χρονων μαθητών του τρέχοντας έτους (το 2021 λόγου χάρη, η τιμή year ισούται με 1991). Έπειτα ελέγχει αν υπάρχουν μαθητές που είναι 30 ετών στην συλλογή Students. Αν πράγματι εντοπιστεί το ζητούμενο σύνολο των μαθητών αυτών, τότε το σύστημα εκτυπώνει τα στοιχεία τους μέσω της λίστας student_l1. Για την δημιουργία αυτής της λίστας χρησιμοποιούμε μια δομή επανάληψης for, ώστε να έχουμε πρόσβαση σε κάθε 30χρονο μαθητή και να αποθηκεύσουμε τα στοιχεία του σε ένα λεξικό με το όνομα student_d2. Έτσι με την εντολή students_l1.append(student_d2) δημιουργείται η ζητούμενη λίστα των μαθητών που μας εκτυπώνεται ως μήνυμα επιτυχίας. Επειδή όμως το Students.json αρχείο μας περιέχει χρήστες που έχουν δηλώσει τα στοιχεία κατοικίας τους, αλλά και χρήστες που έχουν κενό αυτό το πεδίο, πρέπει το λεξικό student_d2 να λαμβάνει δύο μορφές: η πρώτη θα περιλαμβάνει το πεδίο address ενώ η δεύτερη δε θα το περιλαμβάνει. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον 30χρονο μαθητή, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 5ου Endpoint | Επιστροφή όλων των φοιτητών που είναι τουλάχιστον 30 ετών
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/getStudents/oldies. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Προσοχή: δεν εισάγουμε τίποτα στο πεδίο Body. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχουν μαθητές που είναι τουλάχιστον 30 ετών το τρέχον έτος. Υπολογίζει στην ουσία την τιμή date.today().year-30 και την αποθηκεύει στην μεταβλητή yearMinus30. Πρόκειται απλώς για ένα νούμερο που δηλώνει το έτος γέννησης των 30χρονων μαθητών του τρέχοντας έτους (το 2021 λόγου χάρη, η τιμή year ισούται με 1991). Έπειτα ελέγχει αν υπάρχουν μαθητές που είναι άνω των 30 ετών στην συλλογή Students. Αν πράγματι εντοπιστεί το ζητούμενο σύνολο των μαθητών αυτών, τότε το σύστημα εκτυπώνει τα στοιχεία τους μέσω της λίστας student_l2. Για την δημιουργία αυτής της λίστας χρησιμοποιούμε μια δομή επανάληψης for, ώστε να έχουμε πρόσβαση σε κάθε τέτοιο μαθητή και να αποθηκεύσουμε τα στοιχεία του σε ένα λεξικό με το όνομα student_d3. Έτσι με την εντολή students_l2.append(student_d3) δημιουργείται η ζητούμενη λίστα των μαθητών που μας εκτυπώνεται ως μήνυμα επιτυχίας. Επειδή το Students.json αρχείο μας περιέχει χρήστες που έχουν δηλώσει τα στοιχεία κατοικίας τους, αλλά και χρήστες που έχουν κενό αυτό το πεδίο, πρέπει το λεξικό student_d3 να λαμβάνει δύο μορφές: η πρώτη θα περιλαμβάνει το πεδίο address ενώ η δεύτερη δε θα το περιλαμβάνει. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον μαθητή άνω των 30, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 6ου Endpoint | Επιστροφή φοιτητή που έχει δηλώσει κατοικία βάσει email
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/getStudentAddress. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint6.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει χρήστης στην συλλογή Students με το email που έλαβε μέσω Postman, που να έχει συγχρόνως δηλώσει τα στοιχεία κατοικίας του. Αν πράγματι βρεθεί ένας τέτοιος χρήστης, τότε επιστρέφεται το όνομά του, η οδός και ο ταχυδρομικός κώδικας της πόλης που διαμένει, μέσω του λεξικού student_d4. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον μαθητή, ή ακόμα και αν το email υπάρχει στην συλλογή των Students αλλά αντιστοιχεί σε μαθητή που δεν δήλωσε το πεδίο address, τότε επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 7ου Endpoint | Διαγραφή φοιτητή βάσει email
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την DELETE request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/deleteStudent. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint7.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει χρήστης στην συλλογή Students με το email που έλαβε μέσω Postman. Αν πράγματι βρεθεί ένας τέτοιος χρήστης, τότε διαγράφεται εντελώς από την συλλογή Students, μέσω της εντολής students.delete_one({"email":data["email"]}). Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον μαθητή, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 8ου Endpoint | Εισαγωγή μαθημάτων σε φοιτητή βάσει email
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την PATCH request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/addCourses. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint8.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει χρήστης στην συλλογή Students με το email που έλαβε μέσω Postman. Αν πράγματι βρεθεί ένας τέτοιος χρήστης, τότε εισάγεται στα στοιχεία του το πεδίο courses με τα μαθήματα που λαμβάνει το σύστημα μέσω της εντολής json.loads(request.data). Σκοπός μας είναι να εκτυπωθούν με τρόπο ευδιάκριτο, γι' αυτό και τα αποθηκεύουμε ένα ένα μέσα σε μια λίστα που ονομάζουμε courses_l. Τα δεδομένα αυτής της λίστας περνάνε έπειτα στην μεταβλητή student με την εντολή student.update({"courses":courses_l}) σε μορφή dictionary (ακριβώς όπως υπάρχουν στο JSON αρχείο). Έτσι το σύστημα εκτυπώνει τα στοιχεία του μαθητή με το τρέχον email, αφού πρώτα τα εισάγει στο λεξικό student_d5. Επειδή το Students.json αρχείο μας περιέχει χρήστες που έχουν δηλώσει τα στοιχεία κατοικίας τους, αλλά και χρήστες που έχουν κενό αυτό το πεδίο, πρέπει το λεξικό student_d5 να λαμβάνει δύο μορφές: η πρώτη θα περιλαμβάνει το πεδίο address ενώ η δεύτερη δε θα το περιλαμβάνει. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον μαθητή, επιστρέφεται μήνυμα λάθους.
> # Υλοποίηση του 9ου Endpoint | Επιστροφή περασμένων μαθημάτων φοιτητή βάσει email
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την GET request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/getPassedCourses. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint9.json αρχείο μας στο σύστημα. Έπειτα πηγαίνουμε στο πεδίο Headers και εισάγουμε έναν νέο header με το όνομα Authorization και κάνουμε κλικ στο τετράγωνο πλαίσιο στα αριστερά. Έχοντας κάνει επιτυχώς το login ως χρήστες, λαμβάνουμε (copy) το αναγνωριστικό uuid και το βάζουμε στο πλαίσιο του Authorization. Τώρα είμαστε έτοιμοι να πατήσουμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: Το σύστημα εξετάζει αν το uuid στο πεδίο Authorization υπάρχει στην users_session, καλώντας την συνάρτηση is_session_valid(). Αν λάβει θετική απάντηση, ελέγχει αν υπάρχει χρήστης στην συλλογή Students με το email που έλαβε μέσω Postman, που να έχει συμπληρωμένο το πεδίο courses στην συλλογή Students. Αν πράγματι βρεθεί ένας τέτοιος χρήστης, τότε εξάγονται ως λεξικό τα μαθήματα στα οποία εξετάστηκε και αξιολογήθηκε με προβιβάσιμο βαθμό (βαθμός μεγαλύτερος ή και ίσως του 5). Το λεξικό αυτό ονομάζεται passed και δημιουργείται μέσω της εντολής passed.update(course_d) | το course_d το κάθε ζεύγος course-grade που θέλουμε να εισαχθεί στο λεξικό. Στο τέλος, το σύστημα εκτυπώνει το όνομα του μαθητή και τα μαθήματα που έχει περάσει, μέσω ενός λεξικού που ονομάζουμε student_d6. Σε περίπτωση που το uuid είναι μη έγκυρο, ή το email δεν αντιστοιχεί σε κάποιον μαθητή, ή ο μαθητής δεν έχει εξεταστεί σε κανένα μάθημα επιστρέφεται μήνυμα λάθους. Αντίστοιχα αν ο μαθητής εξετάστηκε αλλά κόπηκε σε όλα τα μαθήματα, εμφανίζεται το ανάλογο ενημερωτικό μήνυμα.
