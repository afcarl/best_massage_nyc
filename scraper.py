import lxml.html
import requests
import grequests
import pickle
from sys import argv

domains = pickle.load("sites_to_scrape")
