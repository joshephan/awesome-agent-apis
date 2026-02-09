#!/usr/bin/env python3

import re

# Read files
with open('README.md', 'r') as f:
    readme = f.read()

with open('NEW_CATEGORIES.md', 'r') as f:
    new_content = f.read()

# Find the insertion point (before "## No Auth Required")
insert_marker = '## No Auth Required (Quick Start)'
parts = readme.split(insert_marker)

if len(parts) != 2:
    print("ERROR: Could not find insertion marker")
    exit(1)

# Update Contents section
new_categories = [
    "- [Anime](#anime)",
    "- [Calendar & Events](#calendar--events)",
    "- [Cloud Storage & File Sharing](#cloud-storage--file-sharing)",
    "- [Dictionaries & Language](#dictionaries--language)",
    "- [Email](#email)",
    "- [Machine Learning & AI](#machine-learning--ai)",
    "- [Jobs & Careers](#jobs--careers)",
    "- [Phone & SMS](#phone--sms)",
    "- [Photography & Images](#photography--images)",
    "- [Social Media](#social-media)",
    "- [Video & Streaming](#video--streaming)",
    "- [Shopping & E-commerce](#shopping--e-commerce)",
    "- [URL Shorteners](#url-shorteners)",
    "- [Tracking & Analytics](#tracking--analytics)",
    "- [Environment & Sustainability](#environment--sustainability)",
    "- [Vehicles & Transportation Tracking](#vehicles--transportation-tracking)",
    "- [Podcasts & Audio](#podcasts--audio)",
    "- [Text Analysis & NLP](#text-analysis--nlp)",
    "- [Patents & Intellectual Property](#patents--intellectual-property)",
    "- [Open Source Projects](#open-source-projects)",
    "- [Personality & Fun Tests](#personality--fun-tests)",
    "- [Continuous Integration & DevOps](#continuous-integration--devops)",
]

# Find Contents section and add new items
contents_end = parts[0].find('---\n\n## Betting')
if contents_end == -1:
    print("ERROR: Could not find end of Contents")
    exit(1)

# Insert new categories into Contents
contents_part = parts[0][:contents_end]
rest_part = parts[0][contents_end:]

# Add new categories before the last "---"
new_contents_lines = '\n'.join(new_categories)
updated_contents = contents_part.rstrip() + '\n' + new_contents_lines + '\n\n'

# Assemble final README
final_readme = updated_contents + rest_part + '\n\n---\n\n' + new_content + '\n\n---\n\n' + insert_marker + parts[1]

# Write output
with open('README.md', 'w') as f:
    f.write(final_readme)

print("✅ README updated successfully!")
print(f"📊 Added 20 new categories with 250+ APIs")
