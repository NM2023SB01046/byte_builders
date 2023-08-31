from flask import Flask, request, jsonify
import pickle
import numpy as np
import seaborn as sns

App_createo2 = pickle.load(open('App_createo@2.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello user!"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gender = int(request.form.get('gender'))
        ssc_p = float(request.form.get('ssc_p'))
        hsc_p = float(request.form.get('hsc_p'))
        degree_p = float(request.form.get('degree_p'))
        workex = int(request.form.get('workex'))
        etest_p = float(request.form.get('etest_p'))
        specialisation = int(request.form.get('specialisation'))
        mba_p = float(request.form.get('mba_p'))
        commerce = int(request.form.get('Commerce',0))
        science = int(request.form.get('Science',0))
        comm_mgmt = int(request.form.get('Comm&Mgmt',0))
        sci_tech = int(request.form.get('Sci&Tech',0))

        input_query = np.array([[gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p,
                                 commerce, science, comm_mgmt, sci_tech]])

        response = App_createo2.predict(input_query)[0]
        return jsonify({'applicant is placed': str(response)})

    return '''
    <form method="post" action="/predict">
        <label for="gender">Gender:</label>
        <select id="gender" name="gender">
            <option value="0">Male</option>
            <option value="1">Female</option>
        </select><br><br>

        <label for="ssc_p">Secondary Exam Percentage:</label>
        <input type="number" id="ssc_p" name="ssc_p"><br><br>

        <label for="hsc_p">Higher Secondary Exam Percentage:</label>
        <input type="number" id="hsc_p" name="hsc_p"><br><br>

        <label for="degree_p">Degree Percentage:</label>
        <input type="number" id="degree_p" name="degree_p"><br><br>

        <label for="workex">Work Experience:</label>
        <select id="workex" name="workex">
            <option value="0">No</option>
            <option value="1">Yes</option>
        </select><br><br>

        <label for="etest_p">Entrance Exam Percentage:</label>
        <input type="number" id="etest_p" name="etest_p"><br><br>

        <label for="specialisation">Master's Specialisation:</label>
        <select id="specialisation" name="specialisation">
            <option value="0">Market & HR</option>
            <option value="1">Market & Finance</option>
        </select><br><br>

        <label for="mba_p">MBA Percentage:</label>
        <input type="number" id="mba_p" name="mba_p"><br><br>

        <label for="Commerce">Commerce:</label>
        <input type="checkbox" id="Commerce" name="Commerce" value="1"><br><br>

        <label for="Science">Science:</label>
        <input type="checkbox" id="Science" name="Science" value="1"><br><br>

        <label for="Comm&Mgmt">Comm&Mgmt:</label>
        <input type="checkbox" id="Comm&Mgmt" name="Comm&Mgmt" value="1"><br><br>

        <label for="Sci&Tech">Sci&Tech:</label>
        <input type="checkbox" id="Sci&Tech" name="Sci&Tech" value="1"><br><br>

        <input type="submit" value="Predict">
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
