#!/bin/bash

# Script to add AI Chat and WhatsApp floating buttons to all HTML pages

CHAT_BUTTON='    <!-- AI Chat Floating Button -->
    <button class="chat-float virtual-consult-trigger" aria-label="Start AI Chat Consultation">
        🤖
    </button>

    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/18764422327" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">
        💬
    </a>'

echo "Adding floating chat buttons to all HTML pages..."

# Find all HTML files that don't already have the chat-float class
find /home/jmatthewlee/claude-test -name "*.html" -type f | while read FILE; do
    # Skip if file already has chat-float button
    if grep -q "chat-float" "$FILE"; then
        echo "Skipping (already has chat button): $FILE"
        continue
    fi
    
    # Check if file has a </body> tag
    if grep -q "</body>" "$FILE"; then
        echo "Adding buttons to: $FILE"
        
        # Insert buttons before </body> tag
        sed -i '/<\/body>/i\    <!-- AI Chat Floating Button -->\n    <button class="chat-float virtual-consult-trigger" aria-label="Start AI Chat Consultation">\n        🤖\n    </button>\n\n    <!-- WhatsApp Floating Button -->\n    <a href="https://wa.me/18764422327" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">\n        💬\n    </a>\n' "$FILE"
    fi
done

echo "Done! Floating chat buttons added to all pages."
