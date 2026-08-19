import json
import re

def clean_notebook_full(path):
    """Nettoie les cles API dans le code source ET dans les outputs/traceback des notebooks."""
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    groq_pattern = r'gsk_[A-Za-z0-9]+'
    replacement = 'GROQ_API_KEY_REMOVED'
    
    changes_source = 0
    changes_output = 0
    
    for cell in nb['cells']:
        # Nettoyer le code source
        if cell['cell_type'] == 'code':
            new_source = []
            for line in cell['source']:
                new_line = re.sub(groq_pattern, replacement, line)
                if new_line != line:
                    changes_source += 1
                new_source.append(new_line)
            cell['source'] = new_source
            
            # Nettoyer les outputs (stdout, stderr, traceback, text, etc.)
            if 'outputs' in cell:
                for output in cell['outputs']:
                    # Nettoyer 'text' (stdout/stderr)
                    if 'text' in output:
                        new_text = []
                        for line in output['text']:
                            new_line = re.sub(groq_pattern, replacement, line)
                            if new_line != line:
                                changes_output += 1
                            new_text.append(new_line)
                        output['text'] = new_text
                    
                    # Nettoyer 'traceback'
                    if 'traceback' in output:
                        new_tb = []
                        for line in output['traceback']:
                            new_line = re.sub(groq_pattern, replacement, line)
                            if new_line != line:
                                changes_output += 1
                            new_tb.append(new_line)
                        output['traceback'] = new_tb
                    
                    # Nettoyer 'evalue' (message d'erreur)
                    if 'evalue' in output:
                        new_evalue = re.sub(groq_pattern, replacement, output['evalue'])
                        if new_evalue != output['evalue']:
                            changes_output += 1
                        output['evalue'] = new_evalue
                    
                    # Nettoyer les data (text/plain dans execute_result)
                    if 'data' in output:
                        for key in output['data']:
                            if isinstance(output['data'][key], list):
                                new_data = []
                                for line in output['data'][key]:
                                    new_line = re.sub(groq_pattern, replacement, line)
                                    if new_line != line:
                                        changes_output += 1
                                    new_data.append(new_line)
                                output['data'][key] = new_data
                            elif isinstance(output['data'][key], str):
                                new_val = re.sub(groq_pattern, replacement, output['data'][key])
                                if new_val != output['data'][key]:
                                    changes_output += 1
                                output['data'][key] = new_val
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    
    print(f'{path}: {changes_source} remplacement(s) source, {changes_output} remplacement(s) output')

clean_notebook_full('test.ipynb')
clean_notebook_full('testin.ipynb')
print('Nettoyage complet termine.')
