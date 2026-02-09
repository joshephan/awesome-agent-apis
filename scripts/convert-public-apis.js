#!/usr/bin/env node

/**
 * Convert public-apis format to awesome-agent-apis format
 * Reads from public-apis README and converts to our format with emoji indicators
 */

const fs = require('fs');
const https = require('https');

// Auth type converter
function convertAuth(auth) {
  if (auth === 'No' || auth === 'no' || auth === '') return '🟢 No';
  if (auth === 'apiKey' || auth === '`apiKey`') return '🟡 API Key';
  if (auth === 'OAuth' || auth === '`OAuth`') return '🔴 OAuth';
  if (auth === 'X-Mashape-Key') return '🟡 API Key';
  return `🟡 ${auth}`;
}

// HTTPS converter
function convertHTTPS(https) {
  if (https === 'Yes' || https === 'yes') return '✅';
  return '❌';
}

// Parse table rows
function parseTableRow(line) {
  const parts = line.split('|').map(s => s.trim()).filter(s => s);
  if (parts.length < 4) return null;
  
  // Extract API name and URL from markdown link
  const apiMatch = parts[0].match(/\[(.*?)\]\((.*?)\)/);
  if (!apiMatch) return null;
  
  return {
    name: apiMatch[1],
    url: apiMatch[2],
    description: parts[1],
    auth: convertAuth(parts[2]),
    https: convertHTTPS(parts[3]),
    // Agent-friendly defaults to ✅ for now
    agentFriendly: '✅'
  };
}

// Convert section to markdown table
function convertSection(lines, startIdx) {
  const apis = [];
  let i = startIdx;
  
  // Skip header lines
  while (i < lines.length && !lines[i].includes('|:---|:---|:---|:---|:---|')) {
    i++;
  }
  i++; // Skip the separator line
  
  // Parse data rows
  while (i < lines.length && lines[i].startsWith('|')) {
    const api = parseTableRow(lines[i]);
    if (api) apis.push(api);
    i++;
  }
  
  return apis;
}

// Main function
async function main() {
  console.log('Downloading public-apis README...');
  
  // Download the file
  const url = 'https://raw.githubusercontent.com/public-apis/public-apis/master/README.md';
  
  https.get(url, (res) => {
    let data = '';
    
    res.on('data', (chunk) => {
      data += chunk;
    });
    
    res.on('end', () => {
      console.log('Processing data...');
      const lines = data.split('\n');
      
      // Find all sections
      const categories = {};
      let currentCategory = null;
      
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        
        // Detect category headers (### Animals)
        if (line.startsWith('### ') && !line.includes('Index')) {
          currentCategory = line.replace('### ', '').trim();
          const apis = convertSection(lines, i + 1);
          if (apis.length > 0) {
            categories[currentCategory] = apis;
          }
        }
      }
      
      // Output as JSON for easy processing
      console.log('Found categories:', Object.keys(categories).length);
      console.log('Total APIs:', Object.values(categories).reduce((sum, apis) => sum + apis.length, 0));
      
      fs.writeFileSync('./public-apis-converted.json', JSON.stringify(categories, null, 2));
      console.log('Saved to public-apis-converted.json');
    });
  });
}

main();
