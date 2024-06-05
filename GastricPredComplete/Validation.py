# GastricPredComplete/Validation.py

import os
import pandas as pd
import joblib

def predict(df, model_type):
    selected_genes = [
        'ADAP1', 'BMP3', 'FRG1HP', 'IFNA10', 'NT5C3B', 'PLEKHB2', 'RIIAD1', 'SCGB3A1', 'SLC6A15',
        'TNNC1', 'WFDC3', 'ZBTB8A', 'ZNF432'
    ]
    # Select features from dataframe
    df_selected = df[selected_genes]
    
    # Construct model path
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_type.lower()}.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model '{model_type}' not found. Ensure the model file exists at {model_path}.")
    
    # Load the model
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(df_selected)
    
    # Add predictions to dataframe
    df['Prediction'] = ['Cancer' if pred == 1 else 'Normal' for pred in y_pred]
    
    # Save predictions to CSV file
    df.to_csv('predictions.csv', index=False)
    
    # Print diagnosis
    count_cancer = y_pred.sum()
    count_normal = len(y_pred) - count_cancer
    percentage_cancer = count_cancer / len(y_pred)
    percentage_normal = count_normal / len(y_pred)
    
    if percentage_cancer > 0.6:
        print(f"Gastric Cancer patient detected, {percentage_cancer*100:.2f}%")
    else:
        print(f"Normal patient detected, {percentage_normal*100:.2f}%")
