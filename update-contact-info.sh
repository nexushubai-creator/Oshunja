#!/bin/bash

# Script to update all contact information throughout the site

# Define the search and replace patterns
OLD_PHONE_1="+1876XXXXXXX"
OLD_PHONE_2="+1 (876) XXX-XXXX"
OLD_EMAIL="info@oshunja.com"
OLD_ADDRESS="Your Street Address<br>Kingston, Jamaica"

NEW_PHONE="+18764422327"
NEW_PHONE_DISPLAY="(876) 442-2327"
NEW_EMAIL="support@oshunja.com"
NEW_ADDRESS="Andrews Memorial Hospital<br>27 Hope Road<br>Kingston, Jamaica"

# Find all HTML files
FILES=$(find /home/jmatthewlee/claude-test -name "*.html" -type f)

echo "Updating contact information in HTML files..."

for FILE in $FILES; do
    # Skip if file doesn't exist
    if [ ! -f "$FILE" ]; then
        continue
    fi
    
    # Create a backup
    cp "$FILE" "$FILE.bak"
    
    # Replace phone numbers
    sed -i "s|tel:$OLD_PHONE_1|tel:$NEW_PHONE|g" "$FILE"
    sed -i "s|wa.me/$OLD_PHONE_1|wa.me/$NEW_PHONE|g" "$FILE"
    sed -i "s|$OLD_PHONE_2|$NEW_PHONE_DISPLAY|g" "$FILE"
    
    # Replace email
    sed -i "s|mailto:$OLD_EMAIL|mailto:$NEW_EMAIL|g" "$FILE"
    sed -i "s|$OLD_EMAIL|$NEW_EMAIL|g" "$FILE"
    
    # Replace address (more complex, handle line by line)
    sed -i "s|Your Street Address<br>Kingston, Jamaica|Andrews Memorial Hospital<br>27 Hope Road<br>Kingston, Jamaica|g" "$FILE"
    
    echo "Updated: $FILE"
done

echo "Done! Updated all HTML files."
echo "Backup files created with .bak extension"
