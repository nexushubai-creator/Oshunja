#!/usr/bin/env python3
"""
Reformats How It Works sections to use numbered steps and info boxes like Botox page.
"""

import os
import re

# Define procedure-specific content with proper formatting
FORMATTED_CONTENT = {
    'ozempic.html': {
        'steps': [
            ('Initial Consultation', 'Comprehensive medical assessment including review of weight history, current medications, and metabolic health. We discuss your weight loss goals and determine if Ozempic is appropriate for you.'),
            ('Baseline Testing', 'Lab work to assess glucose levels, kidney function, and other metabolic markers. Documentation of starting weight and measurements for progress tracking.'),
            ('Treatment Initiation', 'Begin with lowest starter dose (0.25mg weekly) for 4 weeks. Our team teaches you proper injection technique for at-home administration.'),
            ('Dose Titration & Monitoring', 'Gradual dose increases every 4 weeks as tolerated, with regular check-ins to monitor progress, manage side effects, and adjust dosing for optimal results.')
        ],
        'info': [
            'Once-weekly subcutaneous injection', 
            'Gradual dose escalation minimizes side effects',
            'Ongoing medical supervision and support',
            'Nutritional guidance provided throughout treatment'
        ]
    },
    
    'mounjaro.html': {
        'steps': [
            ('Medical Evaluation', 'Thorough assessment of your metabolic health, weight history, and treatment goals. Discussion of Mounjaro\'s dual mechanism and expected outcomes.'),
            ('Lab Work & Clearance', 'Comprehensive testing including glucose, kidney function, and thyroid. Medical clearance ensures safe treatment initiation.'),
            ('First Injection', 'Start with 2.5mg weekly dose. Training provided for at-home injections using the convenient auto-injector pen.'),
            ('Progressive Optimization', 'Increase dose every 4 weeks based on response and tolerance. Regular monitoring ensures optimal weight loss while minimizing side effects.')
        ],
        'info': [
            'Once-weekly injection with easy-to-use pen',
            'Dual GIP/GLP-1 mechanism for enhanced results',
            'Regular medical monitoring and adjustments',
            'Comprehensive nutritional support included'
        ]
    },
}

def check_needs_reformatting(filepath):
    """Check if page needs reformatting."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if it has the simple paragraph format instead of process-steps
        if '<div class="process-steps">' in content:
            return False  # Already formatted
        
        if 'How It Works & What To Expect' in content and not '<div class="process-steps">' in content:
            return True  # Needs formatting
        
        return False
    except:
        return False

# First, let's just count how many need reformatting
base_dir = '/home/jmatthewlee/claude-test/pages/procedures'
needs_formatting = []

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            if check_needs_reformatting(filepath):
                needs_formatting.append(filepath)

print(f"Found {len(needs_formatting)} pages needing formatted structure")
for path in needs_formatting[:10]:
    print(f"  - {os.path.relpath(path, '/home/jmatthewlee/claude-test')}")

if len(needs_formatting) > 10:
    print(f"  ... and {len(needs_formatting) - 10} more")
