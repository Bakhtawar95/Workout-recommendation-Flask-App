from flask import Flask, render_template, request,redirect, url_for, session
import random
import pandas as pd


# Read exercise data from Excel file
exercise_data = pd.read_excel('Book1.xlsx')
# Create dictionaries and lists to store exercises for each level
exercise_lists = {}
completed_exercises1_3 = []
completed_exercises3_4 = []
completed_exercises4_5 = []
recommended_exercises1_3b = []
recommended_exercises3_4b=[]
recommended_exercises4_5b=[]
recommended_exercises1_3i = []
recommended_exercises3_4i=[]
recommended_exercises4_5i=[]
recommended_exercises1_3a = []
recommended_exercises3_4a=[]
recommended_exercises4_5a=[]

# Loop through the exercise data and append exercises to the appropriate exercise list
for index, row in exercise_data.iterrows():
    level = row['Level']
    exercise = row['Exercise']
    if level not in exercise_lists:
        exercise_lists[level] = []
    exercise_lists[level].append(exercise)



# Create separate lists for each level
level_1_exercises = exercise_lists.get(1, [])
level_2_exercises = exercise_lists.get(2, [])
level_3_exercises = exercise_lists.get(3, [])
level_4_exercises = exercise_lists.get(4, [])
level_5_exercises = exercise_lists.get(5, [])

level1_3_exercises = level_1_exercises + level_3_exercises
level3_4_exercises = level_3_exercises + level_4_exercises
level4_5_exercises = level_4_exercises + level_5_exercises

first_list="recommended_exercises1_3"
second_list="recommended_exercises3_4"
third_list="recommended_exercises4_5"

# Loops to recommend exercises
previous_exercise = None

for i in range(1, 76):
    if (i % 5 == 0 and i != 1):
        recommended_exercises1_3b.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level1_3_exercises)
        if exercise != previous_exercise:
            recommended_exercises1_3b.append(exercise)
            previous_exercise = exercise
        else:
            # If the current exercise is the same as the previous one,
            # choose another exercise until a different one is found
            while exercise == previous_exercise:
                exercise = random.choice(level1_3_exercises)
            recommended_exercises1_3b.append(exercise)
            previous_exercise = exercise

previous_exercise = None
for i in range(1, 151):
    if (i % 5 == 0 and i != 1):
        recommended_exercises3_4b.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level3_4_exercises)
        if exercise != previous_exercise:
            recommended_exercises3_4b.append(exercise)
            previous_exercise = exercise
        else:
            while exercise == previous_exercise:
                exercise = random.choice(level3_4_exercises)
            recommended_exercises3_4b.append(exercise)
            previous_exercise = exercise

previous_exercise = None

for i in range(1, 226):
    if (i % 5 == 0 and i != 1):
        recommended_exercises4_5b.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level4_5_exercises)
        if exercise != previous_exercise:
            recommended_exercises4_5b.append(exercise)
            previous_exercise = exercise
        else:
            while exercise == previous_exercise:
                exercise = random.choice(level4_5_exercises)
            recommended_exercises4_5b.append(exercise)
            previous_exercise = exercise
#loops for Intermediate type
for i in range(1, 121):
    if (i % 5 == 0 and i != 1):
        recommended_exercises1_3i.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level1_3_exercises)
        if exercise != previous_exercise:
            recommended_exercises1_3i.append(exercise)
            previous_exercise = exercise
        else:
            # If the current exercise is the same as the previous one,
            # choose another exercise until a different one is found
            while exercise == previous_exercise:
                exercise = random.choice(level1_3_exercises)
            recommended_exercises1_3i.append(exercise)
            previous_exercise = exercise

previous_exercise = None
for i in range(1, 241):
    if (i % 5 == 0 and i != 1):
        recommended_exercises3_4i.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level3_4_exercises)
        if exercise != previous_exercise:
            recommended_exercises3_4i.append(exercise)
            previous_exercise = exercise
        else:
            while exercise == previous_exercise:
                exercise = random.choice(level3_4_exercises)
            recommended_exercises3_4i.append(exercise)
            previous_exercise = exercise

previous_exercise = None

for i in range(1, 361):
    if (i % 5 == 0 and i != 1):
        recommended_exercises4_5i.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level4_5_exercises)
        if exercise != previous_exercise:
            recommended_exercises4_5i.append(exercise)
            previous_exercise = exercise
        else:
            while exercise == previous_exercise:
                exercise = random.choice(level4_5_exercises)
            recommended_exercises4_5i.append(exercise)
            previous_exercise = exercise
#loops for Advanced type

for i in range(1, 151):
    if (i % 5 == 0 and i != 1):
        recommended_exercises1_3a.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level1_3_exercises)
        if exercise != previous_exercise:
            recommended_exercises1_3a.append(exercise)
            previous_exercise = exercise
        else:
            # If the current exercise is the same as the previous one,
            # choose another exercise until a different one is found
            while exercise == previous_exercise:
                exercise = random.choice(level1_3_exercises)
            recommended_exercises1_3a.append(exercise)
            previous_exercise = exercise

previous_exercise = None
for i in range(1, 301):
    if (i % 5 == 0 and i != 1):
        recommended_exercises3_4a.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level3_4_exercises)
        if exercise != previous_exercise:
            recommended_exercises3_4a.append(exercise)
            previous_exercise = exercise
        else:
            while exercise == previous_exercise:
                exercise = random.choice(level3_4_exercises)
            recommended_exercises3_4a.append(exercise)
            previous_exercise = exercise

previous_exercise = None

for i in range(1, 451):
    if (i % 5 == 0 and i != 1):
        recommended_exercises4_5a.append(random.choice(level_2_exercises))
        previous_exercise = None
    else:
        exercise = random.choice(level4_5_exercises)
        if exercise != previous_exercise:
            recommended_exercises4_5a.append(exercise)
            previous_exercise = exercise
        else:
            while exercise == previous_exercise:
                exercise = random.choice(level4_5_exercises)
            recommended_exercises4_5a.append(exercise)
            previous_exercise = exercise



def recommender(criterion, programs,state,list_name, recommended_exercise_group):
    prog = ""
    count = 0
    prog = session.get('prog', 0)
    no_check = session.get('no_check', 0)
    if no_check==1:
        state=state+1
        session['no_check'] = 0
    session['list'] = list_name
    session['rec'] = recommended_exercise_group
    session['current_state'] = state
    exercise = recommended_exercise_group[state]
    #print(f"rec ex: {recommended_exercises1_3b}")
    print(f"state:{state}")
    if (state+1) % criterion == 1 and count < programs :
        progr = (state) // criterion + 1
        prog= f"{progr} / {programs}"
        session['prog'] = prog

        count += 1

    variable = exercise
    session['suggested'] = variable
    search_column = "Exercise"
        # Use boolean indexing to filter rows where the search column matches the variable
    filtered_df = exercise_data[exercise_data[search_column] == variable]

            # Fetch the corresponding value from the fetch column
    if not filtered_df["Desc"].isnull().any():
        fetched_value = filtered_df.iloc[0, 1]
    else:
        fetched_value="No description available."

            # Fetch the corresponding value from the fetch column
    if not filtered_df["Picture"].isnull().any():
        pic_url = filtered_df.iloc[0, 4]
    else:
        pic_url="No preview available."
            
    ques="Were you able to do the exercise?"
    return state,prog,variable, fetched_value,pic_url,ques

app = Flask(__name__)
app.secret_key = 'hani'

# Create a variable to store the sensor data
sensor_data = {
    'temperature': None,
    'angle': None,
    'stability': None
}

# Create a variable to store the sensor data

@app.route("/")
def home():
    session['state1'] = 0
    session['state2'] = 0
    session['state3'] = 0
    session['prog'] = ''
    session['list'] = ''
    session['rec'] = ''
    session['suggested'] = ''
    session['level'] = 1
    session['current_state'] = 0
    session['checkbox'] = 0
    session['no_check'] = 0
    session['no_pressed']=0

    return render_template('index.html')


@app.route("/Login")
def Login():
    return render_template("Login.html")

@app.route("/Profil")
def Profil():
    return render_template("Profil.html")

@app.route("/Support")
def Support():
    return render_template("Support.html")

@app.route("/Verktyg")
def Verktyg():
    return render_template("Verktyg.html")

@app.route("/Skada")
def Skada():
    return render_template("Skada.html")

@app.route("/Kontakt")
def Kontakt():
    return render_template("Kontakt.html")

@app.route('/ready', methods=['GET', 'POST'])
def ready():
    if request.method == 'POST':
        # Redirect the user to the desired page
        return redirect(url_for('target_page'))
    else:
        # Render the form for the user to submit
        return render_template('ready.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    checkbox_value = request.form.get('training') 
    session['checkbox'] = checkbox_value
    
    if checkbox_value=="1":
        st,prog,variable, fetched_value,pic_url,ques = recommender(5, 15,0,first_list, recommended_exercises1_3b)        
        st=st+1
        return render_template('rec.html', selected_level="Beginner", st=st, prog=prog, variable=variable, fetched_value=fetched_value , filename=pic_url,ques=ques)  
    
    elif checkbox_value=="2":
        st,prog,variable, fetched_value,pic_url,ques = recommender(8, 15,0,first_list, recommended_exercises1_3i)        
        st=st+1
        return render_template('rec.html', selected_level="Intermediate", st=st,prog=prog, variable=variable, fetched_value=fetched_value , filename=pic_url,ques=ques)  
   
    elif checkbox_value=="3":
        st,prog,variable, fetched_value,pic_url,ques = recommender(10, 15,0,first_list, recommended_exercises1_3i)        
        st=st+1
        return render_template('rec.html', selected_level="Advanced", st=st,prog=prog, variable=variable, fetched_value=fetched_value , filename=pic_url,ques=ques)  
    else:
        return "No training level selected"
    

@app.route('/submit-ques-form', methods=['POST'])
def submit_ques_form():
    pic_url = None        
    if request.form.get('answer') == "YES":
        #no_pressed = session.get('no_pressed', 0) 
    
        session['no_pressed'] = 0
        checkbox = session.get('checkbox', 0) 
        if checkbox == "1":
            level= session.get('level', 0)
            if level==1:
                state1 = session.get('state1', 0)
                if state1==74:
                    state1+=1
                    session['state1'] = state1
                    level=2
                    session['level'] = level
                    exc="You have successfully completed level 1. Now you are on Second level! "
                
                    st,prog,variable, fetched_value,pic_url,ques = recommender(5, 30,0,second_list, recommended_exercises3_4b)
                elif state1 < 74 :   
                    state1 += 1
                    session['state1'] = state1
                    exc="That's Great"
                    st,prog,variable, fetched_value,pic_url,ques = recommender(5, 15,state1,first_list, recommended_exercises1_3b)
            elif level==2: 
                state2 = session.get('state2', 0) 
                if state2==149:
                    state2 += 1
                    session['state2'] = state2
                    level=3
                    session['level'] = level
                    exc="You have successfully completed level 2. Now you are on Third level! "
                    st,prog,variable, fetched_value,pic_url,ques = recommender(5, 45,0,third_list, recommended_exercises4_5b)
                elif state2 < 149 :   
                    state2 += 1
                    session['state2'] = state2

                    exc="That's Great!"
        
                    st,prog,variable, fetched_value,pic_url,ques = recommender(5, 30,state2,second_list,recommended_exercises3_4b)
        

        
            elif level==3: 
                state3 = session.get('state3', 0) 
                if state3==224:
                    state3 += 1
                    session['state3'] = state3
                    exc="You have successfully completed level 3. Training Finished! "
                    return exc
                elif state3 < 224 :   
                    state3 += 1
                    session['state3'] = state3
                    exc="That's Great!"
                    st,prog,variable, fetched_value,pic_url,ques = recommender(5, 45,state3,third_list,recommended_exercises4_5b)
            st=st+1
            return render_template('rec.html', response="yes",exc=exc,st=st, prog=prog, variable=variable, fetched_value=fetched_value , filename=pic_url, ques=ques)
        



        elif checkbox == "2":
            level= session.get('level', 0)
            if level==1:
                state1 = session.get('state1', 0)
                if state1==119:
                    state1+=1
                    session['state1'] = state1
                    level=2
                    session['level'] = level
                    exc="You have successfully completed level 1. Now you are on Second level! "
                
                    st,prog,variable, fetched_value,pic_url,ques = recommender(8, 30,0,second_list, recommended_exercises3_4i)
                elif state1 < 119 :   
                    state1 += 1
                    session['state1'] = state1
                    exc="That's Great"
                    st,prog,variable, fetched_value,pic_url,ques = recommender(8, 15,state1,first_list, recommended_exercises1_3i)
            elif level==2: 
                state2 = session.get('state2', 0) 
                if state2==239:
                    state2 += 1
                    session['state2'] = state2
                    level=3
                    session['level'] = level
                    exc="You have successfully completed level 2. Now you are on Third level! "
                    st,prog,variable, fetched_value,pic_url,ques = recommender(8, 45,0,third_list, recommended_exercises4_5i)
                elif state2 < 239 :   
                    state2 += 1
                    session['state2'] = state2

                    exc="That's Great!"
        
                    st,prog,variable, fetched_value,pic_url,ques = recommender(8, 30,state2,second_list,recommended_exercises3_4i)
        
            elif level==3: 
                state3 = session.get('state3', 0) 
                if state3==359:
                    state3 += 1
                    session['state3'] = state3
                    exc="You have successfully completed level 3. Training Finished! "
                    return exc
                elif state3 < 359 :   
                    state3 += 1
                    session['state3'] = state3
                    exc="That's Great!"
                    st,prog,variable, fetched_value,pic_url,ques = recommender(8, 45,state3,third_list,recommended_exercises4_5i)
            st=st+1
            return render_template('rec.html', response="yes",exc=exc, st=st,prog=prog, variable=variable, fetched_value=fetched_value , filename=pic_url, ques=ques)
        elif checkbox == "3":
            level= session.get('level', 0)
            if level==1:
                state1 = session.get('state1', 0)
                if state1==149:
                    state1+=1
                    session['state1'] = state1
                    level=2
                    session['level'] = level
                    exc="You have successfully completed level 1. Now you are on Second level! "
                
                    st,prog,variable, fetched_value,pic_url,ques = recommender(10, 30,0,second_list, recommended_exercises3_4a)
                elif state1 < 149 :   
                    state1 += 1
                    session['state1'] = state1
                    exc="That's Great"
                    st,prog,variable, fetched_value,pic_url,ques = recommender(10, 15,state1,first_list, recommended_exercises1_3a)
            elif level==2: 
                state2 = session.get('state2', 0) 
                if state2==299:
                    state2 += 1
                    session['state2'] = state2
                    level=3
                    session['level'] = level
                    exc="You have successfully completed level 2. Now you are on Third level! "
                    st,prog,variable, fetched_value,pic_url,ques = recommender(10, 45,0,third_list, recommended_exercises4_5a)
                elif state2 < 299 :   
                    state2 += 1
                    session['state2'] = state2

                    exc="That's Great!"
        
                    st,prog,variable, fetched_value,pic_url,ques = recommender(10, 30,state2,second_list,recommended_exercises3_4a)
        
            elif level==3: 
                state3 = session.get('state3', 0) 
                if state3==449:
                    state3 += 1
                    session['state3'] = state3
                    exc="You have successfully completed level 3. Training Finished! "
                    return exc
                elif state3 < 449 :   
                    state3 += 1
                    session['state3'] = state3
                    exc="That's Great!"
                    st,prog,variable, fetched_value,pic_url,ques = recommender(10, 45,state3,third_list,recommended_exercises4_5a)
            st=st+1
            return render_template('rec.html', response="yes",exc=exc, st=st, prog=prog, variable=variable, fetched_value=fetched_value , filename=pic_url, ques=ques)        
    if request.form.get('answer') == "NO":
        return render_template('rec.html', response="nope")

    
    



@app.route('/no-form', methods=['POST'])
def submit_feedback_form():

    exc="Thank you for your feedback! Here's another recommendation for you:"
    rec = session.get('rec', 0)
    list= session.get('list', 0)
    current_state=session.get('current_state', 0)
    current_state+=1
    session['current_state'] = current_state
    session['no_check'] = 1
    
    no_pressed=session.get('no_pressed', 0)
    no_pressed+=1
    session['no_pressed']=no_pressed


    st,prog,variable, fetched_value,pic_url,ques = recommender(5, 15,current_state,list,rec)
    st=st-1
    noo=session.get('no_pressed', 0)
    if noo>1:
        st=""

    return render_template('rec.html', response="no",exc=exc,st=st, prog=prog, variable=variable, fetched_value=fetched_value , filename=pic_url, ques=ques)










@app.route('/target-page')
def target_page():
    return render_template('rec.html')

@app.route("/Varden", methods=["GET", "POST"])
def varden():
    return 'Send data using a POST request', 400

@app.route("/data")
def data():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080")