import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import math
from randomforest import saved_model

from flask import Flask, render_template, request, url_for
app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/index')
def item():
   return render_template('index.html')


@app.route('/graph')
def item2():
   return render_template('graph.html')
   
   
   
@app.route('/results',methods = ['POST', 'GET'])
def results():
    if request.method == 'POST':
        a1=request.form['attendanceRadio']
        a2=request.form['studyHoursRadio']
        a3=request.form.getlist("Sem")
        a4=request.form['regularLastMinRadio']
        a5=request.form['councilRadio']	
        a6=request.form['groupProjects']
        a7=request.form['soloProjects']
        a8=request.form['higherStudiesRadio']
        a9=request.form['medicalConditionRadio']
        a10=request.form['noOfNonTech']
        a11=request.form['noOfTech']
        a12=request.form['kt']
        a13=request.form['socialHoursRadio']
        a14=request.form['entertainmentHoursRadio']
        a15=request.form['outdoorHoursRadio']
        a16=request.form['collegeTimeRadio']
        a17=request.form['siblingRadio']
        a18=request.form['depressionRadio']
        a19=request.form['familyCrisisRadio']
        a20=request.form['interestedRadio']
        a21=request.form['noOfFriends']
        a22=request.form['hosteliteRadio']	
        a=[a1,a2,'0',a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22]
        X = pd.DataFrame(a)
        X = X.transpose()
        #Encoding categorical data
        from sklearn.preprocessing import LabelEncoder, OneHotEncoder
        LabelEncoder_X = LabelEncoder()
        #X[:, 2] = LabelEncoder_X.fit_transform(X[:, 2])
        X.values[:, 2] = LabelEncoder_X.fit_transform(X.values[:, 2])	
        reg= pickle.loads(saved_model)	
        y_pred=reg.predict(X)
        y_pred1=round(y_pred[0],2)
        if y_pred<=6.5:
            s1="Your report shows you often struggle to focus in class, which harms your ability to engage well with class activities and assignments.Be sure to ask for assistance. You need to listen to directions more attentively during lessons. Working on these problem areas every night would help improve your learning outcomes."
        if y_pred>6.5 and y_pred<=7.0:
            s1="You need to improve your cooperation in group settings. Ensure to accept a share of the work when participating in a group assignment. You would benefit from showing a greater desire to contribute ideas in class. Work on voicing feelings and emotions and listening to others."
        if y_pred>7.0 and y_pred<=7.7:
            s1="Your report shows you require ongoing support to develop an understanding of note taking from lectures and readings in preparation for tests. Give yourself extra time. You need to work very hard if you are pursuing higher studies and need to get a CGPA above 8.5 to get a good university and also avail scholarships."
        if y_pred>7.7 and y_pred<=8.2:
            s1="Good. Appreciative of different perspectives and experiences.” You can improve more if you work hard on your skills. You can be shortlisted for almost all companies. The companies on higher end demand a CGPA of 8.5 and above. Keep working hard and try pulling your CGPA above 8.5. If you are pursuing higher studies for getting a good university you need a minimum of 8.5 CGPA along with other factors."
        if y_pred>8.2 and y_pred<=8.8:
            s1="Very Good. You are encouraged to demonstrate a more responsible attitude and behavior in the classroom. You are determined and with some motivation, you can easily grow your numbers. Most of the people fall under the same category so you have a lot of competition to beat.Your developmental skills are strong but your analytical skills still needs to be up to the mark. Companies to look for: JPMC, MAQ, KPMG, Reliance Industries, BNP Paribas. "
        if y_pred>8.8 and y_pred<=9.2:
            s1="Excellent. Your report shows a conscientious effort to learn. Please continue to nurture and encourage this behavior. You are in the higher 2% of the population in this college. Still you need to put in more effort to absolute ensure your position in the big leagues. The last step from here is not far away. Focus more on training your brain to think analytically, increase your IQ and that could seal your place among the best. Companies to look for: Carwale, Morgan Stanley, Indus Valley Partners, Interactive Brokers, Quantiphi.”"    
        if y_pred>9.2 and y_pred<=9.5:
            s1="Keep it up! Your report demonstrates a willing and conscientious effort in your daily work.”Your CGPA is among the highest and very few students are able to achieve this feat. Now you need to emphasize your projects and have some real life technical experience by doing some internships. You can also try to improve your social interaction and make connections.Companies to look for - JPMC, Carwale, Indus Valley Partners, Deutsche Bank"

        if y_pred>9.5:
            s1="Congratulations! Your predict CGPA is off the charts! You have a very high Cgpa this will definitely help you in your future, whether it be higher studies or securing good job opportunities. Make sure to follow your passion. Try participating on competitive coding contests and get hands on experience by doing internships. All the best for your future endeavors!Companies to look for - JPMC, Carwale, Indus Valley Partners, Deutsche Bank"




        return render_template("results.html",a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,a10=a10,a11=a11,a12=a12,a13=a13,a14=a14,a15=a15,a16=a16,a17=a17,a18=a18,a19=a19,a20=a20,a21=a21,a22=a22,y_pred=y_pred,y_pred1=y_pred1,s1=s1)


if __name__ == '__main__':
   app.run(debug = True)