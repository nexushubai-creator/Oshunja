#!/bin/bash

# Script to add fade-in animation classes to all procedure pages
# This adds the "fade-in-element" class to major content sections

echo "Adding fade-in animations to procedure pages..."

# Find all procedure HTML files
find ./pages/procedures -name "*.html" | while read -r file; do
    echo "Processing: $file"
    
    # Create backup
    cp "$file" "$file.bak"
    
    # Add fade-in-element class to major sections
    sed -i 's/<section class="procedure-section">/<section class="procedure-section fade-in-element">/g' "$file"
    sed -i 's/<section class="procedure-section section-alt">/<section class="procedure-section section-alt fade-in-element">/g' "$file"
    
    # Add fade-in-element to quick info bar
    sed -i 's/<div class="procedure-quick-info">/<div class="procedure-quick-info fade-in-element">/g' "$file"
    
    # Add fade-in-element to process steps
    sed -i 's/<div class="process-step">/<div class="process-step fade-in-element">/g' "$file"
    
    # Add fade-in-element to benefit cards
    sed -i 's/<div class="benefit-card">/<div class="benefit-card fade-in-element">/g' "$file"
    
    # Add fade-in-element to info boxes
    sed -i 's/<div class="info-box">/<div class="info-box fade-in-element">/g' "$file"
    sed -i 's/<div class="warning-box">/<div class="warning-box fade-in-element">/g' "$file"
    sed -i 's/<div class="combo-note">/<div class="combo-note fade-in-element">/g' "$file"
    
    # Add fade-in-element to recovery phases
    sed -i 's/<div class="recovery-phase">/<div class="recovery-phase fade-in-element">/g' "$file"
    
    # Add fade-in-element to candidate boxes
    sed -i 's/<div class="candidate-box/<div class="candidate-box fade-in-element/g' "$file"
    
    # Add fade-in-element to timeline boxes
    sed -i 's/<div class="timeline-box">/<div class="timeline-box fade-in-element">/g' "$file"
    
    # Add fade-in-element to FAQ items
    sed -i 's/<details class="faq-item">/<details class="faq-item fade-in-element">/g' "$file"
    
    # Add fade-in-element to CTA sections
    sed -i 's/<section class="procedure-cta">/<section class="procedure-cta fade-in-element">/g' "$file"
done

echo "Done! Fade-in classes added to all procedure pages."
echo "Backup files created with .bak extension"
