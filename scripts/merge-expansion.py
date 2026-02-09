#!/usr/bin/env python3
"""
Merge EXPANSION_BATCH_2.md into README.md
Adds APIs to existing categories
"""

import re

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def extract_apis_from_expansion(content):
    """Extract APIs grouped by category"""
    apis = {}
    current_category = None
    
    lines = content.split('\n')
    for line in lines:
        if line.startswith('### ') and '(Expansion)' in line:
            # Extract category name
            current_category = line.replace('### ', '').replace(' (Expansion)', '').strip()
            apis[current_category] = []
        elif line.startswith('| [') and current_category:
            # API entry
            apis[current_category].append(line)
    
    return apis

def insert_apis_into_readme(readme, apis_by_category):
    """Insert APIs into their respective categories in README"""
    
    for category, apis in apis_by_category.items():
        # Find the category in README
        # Try different patterns
        patterns = [
            f'## {category}\n',
            f'## {category.replace("&", "&amp;")}\n',
            f'## {category} & ',
        ]
        
        category_found = False
        for pattern in patterns:
            if pattern in readme:
                # Find the end of the table (before next ##)
                start_idx = readme.find(pattern)
                if start_idx == -1:
                    continue
                    
                # Find the next section or ---
                next_section_idx = readme.find('\n---\n', start_idx + len(pattern))
                if next_section_idx == -1:
                    next_section_idx = readme.find('\n## ', start_idx + len(pattern))
                
                if next_section_idx == -1:
                    continue
                
                # Insert APIs before the section end
                insert_point = next_section_idx
                
                # Add newlines for formatting
                apis_text = '\n'.join(apis) + '\n'
                
                readme = readme[:insert_point] + apis_text + readme[insert_point:]
                print(f"✅ Added {len(apis)} APIs to {category}")
                category_found = True
                break
        
        if not category_found:
            print(f"⚠️  Category not found: {category}")
    
    return readme

def main():
    print("Reading files...")
    readme = read_file('README.md')
    expansion = read_file('EXPANSION_BATCH_2.md')
    
    print("Extracting APIs from expansion...")
    apis = extract_apis_from_expansion(expansion)
    
    print(f"Found {len(apis)} categories to expand")
    for cat, api_list in apis.items():
        print(f"  - {cat}: {len(api_list)} APIs")
    
    print("\nMerging into README...")
    updated_readme = insert_apis_into_readme(readme, apis)
    
    print("\nWriting updated README...")
    write_file('README.md', updated_readme)
    
    # Count total APIs
    total_apis = updated_readme.count('\n| [')
    print(f"\n🎉 Success! Total APIs in README: {total_apis}")

if __name__ == '__main__':
    main()
