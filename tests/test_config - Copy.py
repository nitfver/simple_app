import json
import logging
import os
import joblib
import pytest
#from prediction_service.prediction import form_response, api_response
#import prediction_service

def test_generic():
    a= 2
    b= 2
    assert a==b
