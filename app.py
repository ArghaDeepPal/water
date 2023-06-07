import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    li=[]
    for x in request.form.values():
        li.append(x)
    state=li[len(li)-1].upper()
    del li[len(li)-1]
    do1=float(li[0])
    do2=float(li[1])
    ph1=float(li[2])
    ph2=float(li[3])
    c1=float(li[4])
    c2=float(li[5])
    bod1=float(li[6])
    bod2=float(li[7])
    n1=float(li[8])
    n2=float(li[9])
    fc1=float(li[10])
    fc2=float(li[11])
    tc1=float(li[12])
    tc2=float(li[13])
    float_features = [float(x) for x in li]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    dic = {
    "UTTAR PRADESH": "Wheat, Barley,Poppy ,Sugarcane ,Potato ,Sesame ,Mango  ,Rapeseed ,Linseed ,Mustard ,Hemp ,Ginger ,Rice ,Pulses" ,
    "PUNJAB":"Wheat ,Rice ,Orange ,Maize ,Barley ,Pulses ,Rapeseed ,Mustard ,Sunflower ,Sugarcane ,Cotton",
    "HARYANA":"Wheat ,Sugarcane ,Barley ,Jowar ,Bajra ,Gram ,Rice ,Mustard ,Cotton",
    "MADHYA PRADESH":"Gram ,Wheat ,Maize ,Jower ,Tur ,Urad ,Hemp ,Linseed ,Garlic ,Moong ,Tobacco , Soybean ,Guava ,Groundnut ,Mustard ,Cotton ,Sugarcane",
    "TAMIL NADU":"Gram ,Rice ,Coconut ,Groundnut ,Cashew Nut ,Pepper ,Banana ,Cassava",
    "MAHARASHTRA":"Barley ,Bajra ,Sugarcane ,Sunflower ,Cotton ,Tobacco  ,Mosambi ,Pomegranate ,Onion ,Cashew nut ,Rice ,Jowar ,Wheat ,Pulses ,Grapes ,Groundnut ,Soybean",
    "RAJASTHAN":"Barley ,Bajra ,Rapeseed ,Mustard ,Sesame ,Soyabean ,Wheat ,Sugarcane ,Jowar ,Maize ,Chili ,Cotton ,Mango ,Rice ,Pulses",
    "GUJARAT":"Bajra ,Rice ,Tobacco ,Wheat ,Jowar ,Maize ,Turmeric ,Gram ,Cotton ,Groundnut ,Dates ,Sugarcane",
    "WEST BENGAL":"Rice ,Jute ,Tea ,Potatoes ,Oilseeds ,Betel ,Vine ,Tobacco ,Wheat ,Barley ,Maize",
    "ANDHRA PRADESH":"Rice ,Groundnut ,Turmeric ,Tobacco ,Chilli ,Maize ,Pulses ,Cashew Nuts ,Papaya ,Sapota" ,
    "ASSAM":"Tea ,Bamboo" ,
    "SIKKIM":"Large Cardamom, Tea" ,
    "CHHATTISGARH":"Rice ,Maize ,Wheat ,Niger ,Groundnut ,Pulses",
    "BIHAR":"Rice ,Wheat ,Maize ,Pulses ,Sugarcane ,Litchi ,Jute ,Litchis" ,
    "JHARKHAND":"Rice ,Ragi ,Maize ,Wheat ,Program ,Niger ,Fruits" ,
    "ODISHA":"Turmeric, Rice, Jute,Oil Seeds, Mustard" ,
    "HIMACHAL PRADESH":"Potato ,Poppy ,Ginger ,Soybean ,Oilseeds, Pulse" ,
    "JAMMU AND KASHMIR":"Wheat ,Maize ,Saffron ,Barley ,Bajra ,Jowar ,Gram , " "Apple ,Walnuts"  ,
    "KARNATAKA":"Paddy ,Jowar ,Silk ,Rubber ,Ragi ,Coffee ,Pepper ,Maize ,Sunflower ,Pineapple ,Sugarcane ,Cotton ,Tobacco ,Areca Nut" ,
    "KERALA":"Coconut ,Silk ,Rubber ,Coffee ,Tea ,Ginger ,Cashew Nuts ,Black Pepper ,Small Cardamom"
    }
    FISH=['Catla' , 'Rohu', 'Mrigal', 'Reba' ,'Bata' ,'Calbasu','Pengba', 'Common Carp', 'Grass Carp', 'Silver Carp', 'Magur', 'Singhi', 'Padba Catfish', 'Chital', 'Bronze Featherback','Mola Carplet', 'Climbing Perch', 'Ticto Barb', 'Pool Barb', 'Striped Murrel', 'Nile Tilapia', 'Red Tilapia', 'Golden Mahseer', 'Deccan Mahseer', 'Goldspot Mullet', 'Milkfish', 'Pearlspot', 'Long Whiskers Catfish', 'Striped Dwarf Catfish', 'Silver Pompano' ]
    pH_Min=[7.0, 6.5, 6.0, 6.5, 6.0, 6.5, 6.5, 7.0, 7.0, 6.5, 6.5, 7.0, 6.5, 6.8, 6.5, 6.5, 6.5, 6.0, 6.0, 6.5, 7.0, 7.0,6.5 , 6.5, 7.0, 7.0, 6.5, 6.0, 6.0, 7.0]
    pH_Max=[8.5, 8.5, 9.0, 9.0, 8.0, 8.5, 7.5, 8.0, 8.5, 8.0, 7.5, 8.0, 7.5, 7.5, 7.5, 7.5, 7.5, 8.0, 8.0, 7.5, 8.5, 8.5, 8.0, 7.5, 8.5, 8.5, 8.5, 8.0, 8.0, 9.0]
    note=""
    noteseg=""
    suggestion=""
    if output=="A":#add notes
        s="Drinking WaterSource without conventional treatment but after disinfection"
        f=0
        if tc2>50:
            f=1
            noteseg=noteseg+"Higher than expected Total Coliform. "
        if ph1<6.5:
            f=1
            noteseg=noteseg+"Lower than expected minimum pH. "
        if ph2>8.5:
            f=1
            noteseg=noteseg+"Higher than expected maximum pH. "
        if do1<6:
            f=1
            noteseg=noteseg+"Lower than expected minimum Dissolved Oxygen. "
        if bod2>2:
            f=1
            noteseg=noteseg+"Greater than expected Biochemical Oxygen Demand. "
        if f==1:
            note="Note: "+noteseg;
    elif output=="B":#add notes
        s="Outdoor bathing (Organised)"
        f=0
        if tc2>500:
            f=1
            noteseg=noteseg+"High Total Coliform. "
        if ph1<6.5:
            f=1
            noteseg=noteseg+"Lower than expected minimum pH. "
        if ph2>8.5:
            f=1
            noteseg=noteseg+"Higher than expected maximum pH. "
        if do1<5:
            f=1
            noteseg=noteseg+"Lower than expected minimum Dissolved Oxygen. "
        if bod2>3:
            f=1
            noteseg=noteseg+"Greater than expected Biochemical Oxygen Demand. "
        if f==1:
            note="Note: "+noteseg;
    elif output=="C":#add notes
        s="Drinking water source after conventional treatment and disinfection. "
        f=0
        if tc2>5000:
            f=1
            noteseg=noteseg+"High Total Coliform."
        if ph1<6:
            f=1
            noteseg=noteseg+"Lower than expected minimum pH. "
        if ph2>9:
            f=1
            noteseg=noteseg+"Higher than expected maximum pH. "
        if do1<4:
            f=1
            noteseg=noteseg+"Lower than expected minimum Dissolved Oxygen. "
        if bod2>3:
            f=1
            noteseg=noteseg+"Greater than expected Biochemical Oxygen Demand. "
        if f==1:
            note="Note: "+noteseg;
    elif output=="D": #add notes and fish
        s="Propagation of Wild life and Fisheries."
        f=0
        if ph1<6.5:
            f=1
            noteseg=noteseg+"Lower than expected minimum pH. "
        if ph2>8.5:
            f=1
            noteseg=noteseg+"Higher than expected maximum pH. "
        if do1<4:
            f=1
            noteseg=noteseg+"Lower than expected minimum Dissolved Oxygen. "
        if bod2>2:
            f=1
            noteseg=noteseg+"Greater than expected Biochemical Oxygen Demand. "
        if f==1:
            note="Note: "+noteseg;
        fs=""
        f2=0
        for i in range(len(FISH)):
            if ph1>=pH_Min[i] and ph2<=pH_Max[i]:
                f2=1
                fs=fs+FISH[i]+", "
        if f2==1:
            suggestion="Fish suggested: "+fs
            suggestion=suggestion[:-2]
    elif output=="E": #add notes and crops 
        s="Irrigation, Industrial Cooling, Controlled Waste disposal. "
        f=0
        if ph1<6.5:
            f=1
            noteseg=noteseg+"Lower than expected minimum pH. "
        if ph2>8:
            f=1
            noteseg=noteseg+"Higher than expected maximum pH. "
        if c2>2250:
            noteseg=noteseg+"Higher than expected Electrical Conductivity. "
        if f==1:
            note="Note: "+noteseg;
        suggestion="Crops suggested: "+dic[state]
    return render_template('index.html', prediction_text=f"Class predicted: {output}. \n Best use: {s} ",note=f"\n{note}",suggestion=f"{suggestion}")

@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)