import torch
import torch.nn as nn
import torch.nn.functional as F
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize model architecture
class NN(nn.Module):
    def __init__(self):
        super(NN, self).__init__()
        self.layer1 = nn.Linear(in_features=1, out_features=8)
        self.layer2 = nn.Linear(in_features=8, out_features=1)
        
    def forward(self, x):
        x = F.relu(self.layer1(x))
        x = self.layer2(x)
        return x

# Initalize model and assign pre-trained model weights    
model = NN()
model.load_state_dict(torch.load('Model_weights/NN_test.pth', weights_only=False))

'''
    The function predict() is incharge of:
        - extracting the user input from the text box
        - mapping it to a numerical value (month)
        - normalizing the numerical value
        - getting a prediction
        - "denormalizing" the output so that it is not between 0 and 1
        - displaying the prediction to the user
'''
def predict(user_input):
    user_input = user_input.lower()
    month_dict = {
        'january':13,
        'february': 14,
        'march': 15,
        'april': 16,
        'may': 17,
        'june': 18,
        'july': 19,
        'august': 20,
        'september': 21,
        'october': 22,
        'november': 23,
        'december': 24
    }
    # Min Max values for denormilization   
    Month_min = 1
    Month_max = 24  
    Receipt_min = 220033460
    Receipt_max = 309948684
    
    if user_input in month_dict:
        month_value = month_dict[user_input]
        model_input = [(month_value - Month_min) / (Month_max - Month_min)]
    else:
        return 'Please check the month entered'

    prediction = model.forward(torch.FloatTensor(model_input)).item()
    prediction_denorm = prediction * (Receipt_max - Receipt_min) + Receipt_min # Denormalize the normalized prediction
    prediction_formatted = "{:,}".format(round(prediction_denorm))
    out_text = f'Predicted ' + str(prediction_formatted) + ' receipts for ' + user_input
    return out_text

# this function creates a local host address and renders the web page
@app.route('/')
def load():
    return render_template('web_app.html')

# this function extracts the user input, run an infrence using predict() and sends back the predicted value
@app.route('/get_post', methods=['POST'])
def get_post():
    user_input = request.form['user_input']
    output = predict(user_input)
    return render_template('web_app.html', output=output)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000)