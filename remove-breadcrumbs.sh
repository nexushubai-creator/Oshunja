#!/bin/bash

# Script to remove breadcrumb navigation from all procedure pages

echo "Removing breadcrumbs from procedure pages..."

# Find all procedure HTML files
find ./pages/procedures -name "*.html" | while read -r file; do
    echo "Processing: $file"
    
    # Use sed to remove the breadcrumb nav section (5 lines)
    # Match from <nav class="breadcrumb"> to </nav>
    sed -i '/<nav class="breadcrumb">/,/<\/nav>/d' "$file"
done

echo "Done! Breadcrumbs removed from all procedure pages."
