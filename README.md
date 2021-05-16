# Τεχνική Αναφορά | Περιγραφή Εκτέλεσης Κώδικα
Τμήμα Ψηφιακών Συστημάτων | Πληροφοριακά Συστήματα : Ναταλία Κολιού, Ε18073

> # Εισαγωγή
> Στην τρέχουσα τεχνική αναφορά, θα περιγράψουμε αναλυτικά τα στάδιο εκτέλεσης του αρχείου app.py. Για τον σκοπό αυτό, θα χρησιμοποιήσουμε τον τερματικό του Linux και την εφαρμογή Postman. Με την εκκίνηση της εικονικής μας μηχανής, θα εκτελέσουμε στον terminal τις ακόλουθες δύο εντολές για να ενεργοποιήσουμε το docker και την βάση mongodb: sudo systemctl enable docker --now και sudo docker start mongodb. Στη συνέχεια, θα γράψουμε την εντολή python3 app.py για να ενεργοποιήσουμε τον debugger και να εκτελέσουμε το python αρχείο μας στον http://0.0.0.0:5000/. Προτείνεται η κατασκευή και των 9 JSON αρχείων που θα εισάγετε στο Postman προς δική σας διευκόλυνση ...
> 
>  ... ανατρέξτε στο αρχείο Indicative_JSON_files.txt της εργασίας στο GitHub.
> # Υλοποίηση του 1ου Endpoint | Δημιουργία Χρήστη
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την POST request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/createUser. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint1.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
>
> Ερμηνεία του Κώδικα: το σύστημα ελέγχει αν υπάρχουν ήδη χρήστες στην συλλαγή των Users αξιοποιώντας την συνάρτηση count_documents(). Αν αυτή επιστρέψει 0, τότε αποθηκεύεται στο λεξικό user το username και το password που εισάγεται στο data μέσω της εντολής data = json.loads(request.data). Το λεξικό αυτό user μπαίνει στην συλλογή Users και εν τέλει αποστέλλεται μήνυμα επιτυχίας στον χρήστη. Ειδάλλως αν το username και το password που θέλουμε να εισάγουμε, υπάρχει ήδη στην συλλογή Users, επιστρέφεται το ανάλογο μήνυμα αποτυχίας.
> # Υλοποίηση του 2ου Endpoint | Login στο σύστημα
> Στο πεδίο HTTP Request του Postman, επιλέγουμε την POST request μέθοδο και στο πεδίο Request URL βάζουμε την διεύθυνση: http://0.0.0.0:5000/login. Στο κυρίως μέρος (Body) επιλέγουμε το πεδίο raw για να δηλώσουμε ότι ο τύπος αρχείου που θα εισάγουμε θα είναι JSON. Έπειτα πατάμε binary και στη συνέχεια Select File. Εκεί καλούμαστε να εισάγουμε το endpoint2.json αρχείο μας στο σύστημα. Όταν φορτωθεί επιτυχώς, πατάμε Send για να μας εκτυπωθεί η ζητούμενη απάντηση.
> 
> Ερμηνεία του Κώδικα: το σύστημα ελέγχει αν υπάρχουν χρήστες στην συλλαγή των Users με το username και password που εισάγουμε στο Body του Postman. Αν βρεθεί ένας τέτοιος χρήστης τότε καλείται η συνάρτηση create_session() προκειμένου να αυθεντικοποιηθεί ο χρήστης. Έτσι επιστρέφεται στον χρήστη ένα λεξικό με keys το user unique identifier (uuid) και το username του χρήστη. Σε περίπτωση που δεν βρεθεί ο ζητούμενος χρήστης επιστρέφεται το ανάλογο μήνυμα αποτυχίας.
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
