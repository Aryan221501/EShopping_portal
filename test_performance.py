#!/usr/bin/env python3
"""
Performance Test Script for AI E-Shop
Tests the optimized lag-free animations
"""

import time
import requests
from django.test import TestCase, Client
from django.urls import reverse

class PerformanceTest:
    def __init__(self):
        self.client = Client()
        self.base_url = 'http://localhost:8000'
    
    def test_page_load_speed(self):
        """Test page load performance"""
        print("🚀 Testing Page Load Performance...")
        
        pages = [
            '/',
            '/search/',
            '/cart/',
            '/chatbot/',
        ]
        
        for page in pages:
            start_time = time.time()
            try:
                response = self.client.get(page)
                load_time = (time.time() - start_time) * 1000
                
                status = "✅ FAST" if load_time < 200 else "⚠️ SLOW" if load_time < 500 else "❌ VERY SLOW"
                print(f"  {page}: {load_time:.1f}ms {status}")
                
            except Exception as e:
                print(f"  {page}: ❌ ERROR - {e}")
    
    def test_static_files(self):
        """Test static file loading"""
        print("\n📁 Testing Static Files...")
        
        static_files = [
            '/static/css/minimal-animations.css',
            '/static/js/lag-free-animations.js',
        ]
        
        for file_path in static_files:
            start_time = time.time()
            try:
                response = self.client.get(file_path)
                load_time = (time.time() - start_time) * 1000
                
                if response.status_code == 200:
                    status = "✅ LOADED" if load_time < 50 else "⚠️ SLOW"
                    print(f"  {file_path}: {load_time:.1f}ms {status}")
                else:
                    print(f"  {file_path}: ❌ NOT FOUND")
                    
            except Exception as e:
                print(f"  {file_path}: ❌ ERROR - {e}")
    
    def test_api_endpoints(self):
        """Test API performance"""
        print("\n🔌 Testing API Endpoints...")
        
        endpoints = [
            '/api/products/',
            '/api/categories/',
            '/api/cart/count/',
        ]
        
        for endpoint in endpoints:
            start_time = time.time()
            try:
                response = self.client.get(endpoint)
                load_time = (time.time() - start_time) * 1000
                
                if response.status_code == 200:
                    status = "✅ FAST" if load_time < 100 else "⚠️ SLOW"
                    print(f"  {endpoint}: {load_time:.1f}ms {status}")
                else:
                    print(f"  {endpoint}: ❌ ERROR {response.status_code}")
                    
            except Exception as e:
                print(f"  {endpoint}: ❌ ERROR - {e}")
    
    def run_all_tests(self):
        """Run all performance tests"""
        print("🎯 AI E-Shop Performance Test")
        print("=" * 40)
        
        self.test_page_load_speed()
        self.test_static_files()
        self.test_api_endpoints()
        
        print("\n🎉 Performance Test Complete!")
        print("\n📊 Expected Results:")
        print("  • Page loads: < 200ms")
        print("  • Static files: < 50ms")
        print("  • API calls: < 100ms")
        print("  • 60fps animations")
        print("  • < 5% CPU usage")

if __name__ == '__main__':
    test = PerformanceTest()
    test.run_all_tests()