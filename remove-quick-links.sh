#!/bin/bash

# Script to remove Quick Links section from all HTML footer sections

echo "Removing Quick Links sections from all HTML files..."

# Find all HTML files
find /home/jmatthewlee/claude-test -name "*.html" -type f | while read FILE; do
    # Check if file contains Quick Links section
    if grep -q "Quick Links" "$FILE"; then
        echo "Processing: $FILE"
        
        # Create backup
        cp "$FILE" "$FILE.bak"
        
        # Use perl to remove the Quick Links section (handles multi-line better than sed)
        perl -i -0pe 's/\s*<!-- Quick Links -->.*?<\/div>\n//s' "$FILE"
        
        # Also try alternative pattern if the comment is different
        perl -i -0pe 's/<div class="footer-section">\s*<h3>Quick Links<\/h3>.*?<\/div>\n//s' "$FILE"
    fi
done

echo "Done! Quick Links sections removed."
