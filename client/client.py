#!/usr/bin/env python3
import requests
import time
import sys

NGINX_URL = "http://nginx:80"
AUTH_HEADER = {"x-pretest": "valid-token"}  # Valid token

def send_request_with_auth_header():
    """Send a request to nginx with auth header"""
    try:
        response = requests.get(NGINX_URL, headers=AUTH_HEADER)
        print(f"Request with valid auth header - Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error sending request with auth header: {e}")

def send_request_without_auth_header():
    """Send a request to nginx without auth header"""
    try:
        response = requests.get(NGINX_URL)
        print(f"Request without auth header - Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error sending request without auth header: {e}")

def send_request_with_invalid_auth_header():
    """Send a request to nginx with invalid auth header"""
    try:
        response = requests.get(NGINX_URL, headers={"x-pretest": "invalid-token"})
        print(f"Request with invalid auth header - Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error sending request with invalid auth header: {e}")

if __name__ == "__main__":
    print("Starting client...")
    
    # Wait for services to be ready
    time.sleep(5)
    
    # Send requests
    print("\nSending request with valid auth header:")
    send_request_with_auth_header()
    
    print("\nSending request without auth header:")
    send_request_without_auth_header()
    
    print("\nSending request with invalid auth header:")
    send_request_with_invalid_auth_header() 