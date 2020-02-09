var symptoms = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
    'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
    'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
    'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
    'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
    'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
    'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
    'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
    'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
    'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
    'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
    'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
    'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
    'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
    'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
    'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
    'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
    'yellow_crust_ooze'];
$(function() {
    $("#symptom").autocomplete({
        source: symptoms,
        delay: 500,
        minLength:2
    });
});


var inputs = document.getElementById('symptom');
var addButton = document.getElementById('addButton');
const submitButton = document.getElementById('submitButton');

const container = document.getElementById('chipp');
const form1 =  document.getElementById('searchForm');
form1.addEventListener('submit', function(event){
    event.preventDefault();
});

class item{
    constructor(itemName){
        this.createDiv(itemName);
    }
    createDiv(itemName){

        let itemChip = document.createElement('div');
        itemChip.classList.add('chip');

        let deleteButton = document.createElement('span');
        deleteButton.classList.add('deleteButton')
        deleteButton.innerHTML= "&#10006";

        container.appendChild(itemChip);

        itemChip.textContent=itemName;
        itemChip.appendChild(deleteButton);

        deleteButton.addEventListener('click', () => this.remove(itemChip));

    }
    remove(item){
        if(deleteSymptom(item.textContent))
        {
            container.removeChild(item);
        }
    }
}
symptomList = [];

function deleteSymptom(sympt)
{
    sympt.toString();
    var sympt = sympt.slice(0,-1);
    for(var i=0;i<symptomList.length;i++)
    {
        if(symptomList[i] == sympt)
        {
            symptomList.splice(i,1);
            return true;
        }

    }
    return false;
}

function addChips(){
    inputValue = inputs.value;
    if(inputValue.length >= 2 && isUnique(inputValue) && isSymptom(inputValue))
    {
        new item(inputValue);
        symptomList.push(inputValue);
        inputs.value = "";
    }
    else{
        inputs.value = "";
    }
}

function submitSymptoms(){
    if(symptomList.length > 0)
    {
        alert(symptomList);
    }
    else{
        alert("Please add atleast 3 symotoms !!")
    }
}

function isUnique(val)
{
    for(var i=0;i<symptomList.length;i++)
    {
        if(symptomList[i] == val) {
            alert("This symptom is already added !!");
            return false
        };
    }
    return true;
}

function meetLength(current, expected)
{

}

function isSymptom(sympt){
    for(var i=0;i<symptoms.length;i++)
    if(symptoms[i] == sympt){
        return true;
    }
    return false;
}

addButton.addEventListener('click', addChips);
submitButton.addEventListener('click', submitSymptoms);
