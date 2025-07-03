from django.shortcuts import render
from .forms import MessageForm
import pickle

# Load the model and vectorizer using pickle
with open(r'C:\Users\hp\OneDrive\Desktop\Email spam detetcion\Models\spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open(r'C:\Users\hp\OneDrive\Desktop\Email spam detetcion\Models\vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def predict_view(request):
    result = None
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['text']
            message_vector = vectorizer.transform([message])
            prediction = model.predict(message_vector)[0]
            result = "Spam" if prediction == 1 else "Not Spam"

    return render(request, 'Detector/predict.html', {'form': form, 'result': result})



